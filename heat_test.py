import subprocess
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls


class RPiHeat:

    def __init__(self):
        pass

    def plotly_heat_report(self, traces, username, api_key):
        tls.set_credentials_file(username=username,
                                 api_key=api_key)
        data = Data(traces)
        plot_url = py.plot(data)
        return plot_url

    def build_trace(self, x, y):
        trace = Scatter(x = x,
                        y = y)
        return trace

    def record_heat(self, heat_data):
        fo = open('heat_data.txt', 'a')
        fo.write('%s,' %(heat_data))
        fo.close()

    def get_temp_c(self):
        temp_c = subprocess.check_output(["vcgencmd", "measure_temp"]).split("'")[0].split("=")[1]
        return temp_c

    def c_2_f(self, temp_c):
        temp_f = "{0:.2f}".format(temp_c * 1.8 + 32.0)
        return temp_f


if __name__ == "__main__":
    rpi_heat = RPiHeat()

    temp_c = rpi_heat.get_temp_c()
    temp_f = rpi_heat.c_2_f(temp_c)

    rpi_heat.record_heat(temp_f)
