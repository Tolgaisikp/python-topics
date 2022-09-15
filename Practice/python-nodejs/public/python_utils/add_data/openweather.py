from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import requests

def getCoor(KE, KB):
    max = [41.505331,28.249859]
    min = [40.752296,29.629558]
    
    if (((KE < max[0]) and (KB > max[1])) and ((KE > min[0]) and (KB < min[1]))):       
        return [KE, KB]
    else:
        return False

def getResponse(url):
    if url != False:
        response = requests.get(url)
        if response.status_code != 204:
            return response.json()
    else:
        return True

def getWeatherUrl(coor,startDate,endDate):
    if coor!=False:
        url = f"https://api.openweathermap.org/data/2.5/air_pollution/history?lat={coor[0]}&lon={coor[1]}&start={startDate}&end={endDate}&appid=badf5af466da97d559bb91d0592b3f86"
    else:
        return False

    return url

def getTimestampFormat(date):
    sdate = date -  timedelta(hours = 4)
    oneDay =  date -  timedelta(hours = 3)
    date_str = str(int(datetime.timestamp(sdate)))
    oneDay_str =  str(int(datetime.timestamp(oneDay)))
    return date_str, oneDay_str

def getCurrentWeather(coor):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={coor[0]}&lon={coor[1]}&appid=badf5af466da97d559bb91d0592b3f86"
    response = requests.get(url)
    temp = response.json()['main']['temp']
    humidity = response.json()['main']['humidity']
    WS = response.json()['wind']['speed']
    WD = response.json()['wind']['deg']
    return {'TEMP_weather':temp - 273.15, 'HUM_weather':humidity, 'WS_weather': WS, 'WD_weather':WD}

def addWeatherCol(data):
    if getCoor(float(data['KE']), float(data['KB'])) != False:
        coor = getCoor(float(data['KE']), float(data['KB']))
    else:
        return False
    
    sDate, eDate = getTimestampFormat(data['time'])
    url = getWeatherUrl(coor = coor,
         startDate=sDate,
         endDate=eDate)
    
    current = getCurrentWeather(coor)

    data['KE'] = float(data['KE'])
    data['KB'] = float(data['KB'])
    columns = ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3', 'TEMP_weather', 'HUM_weather', 'WS_weather', 'WD_weather']
    try:
        weatherAirData = getResponse(url)
        df = pd.DataFrame(weatherAirData['list'])
        components = df.loc[:,"components"].to_list()
        df = pd.DataFrame([{**components[0], **current}])       
        mean = df.mean().round(2).replace({np.nan: None}).to_list()
        for key,value in zip(columns, mean):
            data[key] = value
        
    except:
        mean = [None, None, None, None, None, None, None, None, None, None, None, None]
        for key,value in zip(columns, mean):
            data[key] = value     

    return data
