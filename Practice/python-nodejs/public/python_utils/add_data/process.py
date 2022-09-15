from datetime import datetime
import pandas as pd
import json

def CreateSummaryModel(airData):
    if (isPure(airData['AA']) and isKEKB(airData)):
        time = getDatetimeFromString(airData['DT'], airData['TM'])
        
        outsideSummaryDict = {
                "RecordId": airData['RecordId'], 
                "PN": airData['RecordId'], 
                "AA": airData['AA'],
                "DT": airData['DT'],
                "TM": airData['TM'],
                "DK": airData['DK'],
                "SD": airData['SD'],
                "ND": airData['ND'],
                "CD": airData['CD'],
                "VD": airData['VD'],
                "PD": airData['PD'],
                "KE": airData['KE'],
                "KB": airData['KB'],
                "time": time.isoformat()}
        
        return outsideSummaryDict

    else:
        pass

def isPure(serialNumber):
    return True if serialNumber[2] == 'S' else False

def isKEKB(data):
    if 'KE' in data.keys():
        return True
    elif 'KE' == 'None':
        return False
    elif 'KE' == '':
        return False
    else:
        return False

def getDatetimeFromString(DT, TM):
    date = DT + TM
    date_time_obj = datetime.strptime(date, '%d%m%Y%H%M%S')
    return date_time_obj

def dateFilter(data, date):
    df = pd.DataFrame(data)
    df['time'] = pd.to_datetime(df['time'])
    interval = pd.to_datetime(date)
    
    df = df[df['time'] >= interval]
    lList = df.to_json(orient = 'records')
    
    return json.loads(lList)

def dataPreparation(df):
    data = df.drop(['Datetime'], axis=1)
    index = df['Datetime']

    testList = []
    df_full = pd.DataFrame([])

    for i in range(0,data.shape[1],4):
        df_loc = pd.concat([index,data.iloc[:,i:i+4]], axis = 1)
        testList.append(data.iloc[:,i:i+4].columns[0])
        df_loc.columns = df_loc.iloc[0]
        df_loc.drop([0],axis=0, inplace=True)
        df_loc['location'] = data.iloc[:,i:i+4].columns[0]
        df_full = pd.concat([df_full, df_loc])

    return df_full.reset_index(drop=True)

def mergeDataFrame(ibb, weather):
      weather_sum = weather.drop(["RecordId", "PN", "AA", "DT", "TM", "DK", "SD", "ND", "CD", "VD", "PD", "KE", "KB", "time", "PM10",
                                  "SO2", "O3", "NO2", "CO", 'TEMP_ibb', 'HUM_ibb', 'NO_ibb', 'WS', 'WD', 'TEMP_weather', 'HUM_weather', 'WS_weather', 'WD_weather'], axis = 1)
      weather_sum.columns = weather_sum.columns.str.upper()
      weather_sum['RecordId'] = weather['RecordId']
      df = ibb.merge(weather_sum, on="RecordId",
          suffixes=('_ibb', '_weather'))

      df['DT'] = df['DT'].astype(str)
      df['TM'] = df['TM'].astype(str)
      df['time'] = df['time'].astype('datetime64')
      df.drop(['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3'], inplace=True, axis=1)
      return df.to_dict(orient='records')

def updateIndexes(key, value, model, recordId):
    try:
        indexList = list(model.find({key:value}))[0]['indexes']
        indexList.append(recordId)
        model.update_one({key:value},
                            { '$set': { "indexes" : indexList} })

    except IndexError:
        data = {key: value,
                "indexes": [recordId]}
        model.insert_one(data)