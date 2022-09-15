from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import requests
import mpu

def isIstanbul(KE, KB, km = 5):
    max = [41.505331,28.249859]
    min = [40.752296,29.629558]
    
    if (((KE < max[0]) and (KB > max[1])) and ((KE > min[0]) and (KB < min[1]))):       
        return getNearbyStationId(KE, KB, km)

def getNearbyStationId(targetKE, targetKB, km):
    coor = []
    json_data = getResponse('https://api.ibb.gov.tr/havakalitesi/OpenDataPortalHandler/GetAQIStations')
    for data in json_data:
        data['Location'] = [float(x) for x in data['Location'][7:].replace(')','').split(' ')]

    for data in json_data:
        stationKE, stationKB, stationId = data['Location'][1], data['Location'][0], data['Id']
        coor.append([stationId, (stationKE, stationKB), (targetKE, targetKB)])

    df = pd.DataFrame(coor, columns=['stationId', 'station', 'target'])
    df['distance'] = df.apply(lambda x: mpu.haversine_distance(x.station, x.target), axis=1)
    idx = df['distance'].argmin()
    
    if df.iloc[idx]['distance'] <= km:
            return df.iloc[idx]['stationId']
    else:
        return False

def getResponse(url):
    if url != False:
        response = requests.get(url)
        if response.status_code != 204:
            return response.json()
    else:
        return True

def getIbbUrl(stationId,startDate,endDate):
    if stationId!=False:
        url = f"https://api.ibb.gov.tr/havakalitesi/OpenDataPortalHandler/GetAQIByStationId?StationId={stationId}&StartDate={startDate}&EndDate={endDate}"

    else:
        return False

    return url

def dateFormatChange(date):
    ownFormat = date[:13]
    date = datetime.fromisoformat(ownFormat)
    oneDay =  datetime.fromisoformat(ownFormat) +  timedelta(hours = 1)
    date_str = date.strftime("%d.%m.%Y%%20%H:%M:%S")
    oneDay_str =  oneDay.strftime("%d.%m.%Y%%20%H:%M:%S")
    return date_str, oneDay_str

def addIbbCol(data):
    if isIstanbul(float(data['KE']), float(data['KB'])) != None:
        stationId = isIstanbul(float(data['KE']), float(data['KB']))
    else:
        return False

    sDate, eDate = dateFormatChange(data['time'])
    
    url = getIbbUrl(stationId=stationId,
                startDate=sDate,
                endDate=eDate)
    data['KE'] = float(data['KE'])
    data['KB'] = float(data['KB'])
    data['time'] = datetime.strptime(data['time'], "%Y-%m-%dT%H:%M:%S")
    try:
        ibbAirData = getResponse(url)
        df = pd.DataFrame(ibbAirData)
        aqi = df.loc[:,"AQI"].to_list()
        time = df.loc[:, 'ReadTime'].to_list()
    
        df = pd.DataFrame(aqi).loc[:,:'CO']
        df['time'] = time
        mean = df.loc[:,:'CO'].mean().replace({np.nan: None}).to_list()  + [None, None, None, None, None]
        columns = df.loc[:,:'CO'].columns.to_list() + ["TEMP_ibb", "HUM_ibb", "NO_ibb", "WS", "WD"]
        for key,value in zip(columns, mean):
            data[key] = value
        
    except:
        mean = [None, None, None, None, None, None, None, None, None, None]
        for key,value in zip(columns, mean):
            data[key] = value
    
    return data
