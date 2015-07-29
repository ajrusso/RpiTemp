# RpiTemp
RpiTemp is a Python service that logs a Raspberry Pi's temperature. The temperature is stored in a 
Serialized JSON format in the /opt/RpiTemp/heat_data.txt file. The data can be obtained from a command
leveraged in your code or can be graphically viewed in Ploty Scatter plot.

# Raspbian Install 
- Clone into /opt/ dir
    - git clone https://github.com/ajrusso/RpiTemp
- Configure Settings file
    - Add plotly account info
        - plotly username
        - plotly api_key
- Add Upstart service
    - apt-get install upstart
    - python /opt/RpiTemp/tools/setup_upstart.py
    - service heat_temp start
    
#Generating a Plotly Graph
from heat_test import RpiHeat

rpi_heat = RPiHeat()

url = rpi_heat.plotly_heat_report
