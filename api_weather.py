from flask import Flask
from data.data import Data
import math


app = Flask(__name__)

@app.route('/weather/london/<string:date>/<string:hour_minute>')
def data_weather_all(date, hour_minute):

    data = Data().get_data_api()
    string_to_find = date[:4] + "-" + date[4:6] + "-" +  date[6:8] + " "
    string_to_find += hour_minute[:2] + ":" + hour_minute[2:4] +":00"

    result = [ item for item in data['list'] if item['dt_txt'] == string_to_find]
    if len(result)> 0:
        celcius = str(math.ceil(result[0]['main']['temp'] - 273.15)) + "C"
        response = {
            "description": result[0]['weather'][0]['description'],
            "temperature": celcius,
            "pressure": str(result[0]['main']['pressure']),
            "humidity": str(result[0]['main']['humidity']) + "%"
            }
        return str(response)
    else:
        return str({
            "status": "error", "message": "No data for " + string_to_find
        })

@app.route('/weather/london/<string:date>/<string:hour_minute>/temperature')
def data_weather_temp(date, hour_minute):
    data = Data().get_data_api()
    string_to_find = date[:4] + "-" + date[4:6] + "-" +  date[6:8] + " "
    string_to_find += hour_minute[:2] + ":" + hour_minute[2:4] +":00"

    result = [ item for item in data['list'] if item['dt_txt'] == string_to_find]
    if len(result)> 0:
        celcius = str(math.ceil(result[0]['main']['temp'] - 273.15)) + "C"
        response = {
            "temperature": celcius

            }
        return str(response)
    else:
        return str({
            "status": "error", "message": "No data for " + string_to_find
        })

@app.route('/weather/london/<string:date>/<string:hour_minute>/pressure')
def data_weather_pres(date, hour_minute):
    data = Data().get_data_api()
    string_to_find = date[:4] + "-" + date[4:6] + "-" +  date[6:8] + " "
    string_to_find += hour_minute[:2] + ":" + hour_minute[2:4] +":00"

    result = [ item for item in data['list'] if item['dt_txt'] == string_to_find]
    if len(result)> 0:
        response = {
            "pressure": str(result[0]['main']['pressure'])

            }
        return str(response)
    else:
        return str({
            "status": "error", "message": "No data for " + string_to_find
        })

@app.route('/weather/london/<string:date>/<string:hour_minute>/humidity')
def data_weather_humid(date, hour_minute):
    #date format: YearMonthDay

    data = Data().get_data_api()
    string_to_find = date[:4] + "-" + date[4:6] + "-" +  date[6:8] + " "
    string_to_find += hour_minute[:2] + ":" + hour_minute[2:4] +":00"

    result = [ item for item in data['list'] if item['dt_txt'] == string_to_find]
    if len(result)> 0:
        response = {
            "humidity": str(result[0]['main']['humidity']) + "%"
            }
        return str(response)
    else:
        return str({
            "status": "error", "message": "No data for " + string_to_find
        })

if __name__ == '__main__':
    app.run()
