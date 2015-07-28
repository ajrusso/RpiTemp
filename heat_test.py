import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
from datetime import datetime
import subprocess
import settings
import time
import json


class RPiHeat:

    def __init__(self):
        pass

    def plotly_heat_report(self, traces):
        tls.set_credentials_file(username=settings.username,
                                 api_key=settings.api_key)
        data = Data(traces)
        plot_url = py.plot(data)
        return plot_url

    def _build_trace(self, x, y):
        trace = Scatter(x = x,
                        y = y)
        return trace

    def get_temp_data(self):
        f = open('heat_data.txt', 'r')
        heat_data = json.load(f)
        f.close()
        return heat_data 

    def record_heat(self, heat_data):
        temp_data = self.get_temp_data()
        f = open('heat_data.txt', 'w')
        utcnow = str(datetime.utcnow())
        temp_data['heat_data'].append((heat_data, utcnow))
        json.dump(temp_data, f)
        f.close()

    def get_temp_c(self):
        temp_c = float(subprocess.check_output(["vcgencmd", "measure_temp"]).split("'")[0].split("=")[1])
        return temp_c

    def c_2_f(self, temp_c):
        temp_f = "{0:.2f}".format(temp_c * 1.8 + 32.0)
        return temp_f


if __name__ == "__main__":
    while True:
        rpi_heat = RPiHeat()
        temp_c = rpi_heat.get_temp_c()
        temp_f = rpi_heat.c_2_f(temp_c)
        rpi_heat.record_heat(temp_f)
        time.sleep(60)
