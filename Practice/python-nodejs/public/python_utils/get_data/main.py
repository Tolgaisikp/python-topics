import mpu
import sys
import json
import numpy as np
import pandas as pd
from datetime import datetime
from pymongo import MongoClient

#Model
client = MongoClient('mongodb://localhost:27017')

#Database
airData = client['airData']

#Collection
outsidesummaries = airData['outsidesummaries']

#Utils
def getPeriodData(data, period):
    if period == 'daily':
        d_freq = '1D'
    if period == 'weekly':
        d_freq = '1W'
    if period == 'monthly':
        d_freq = '1M'
    else:
        return data
    #data['time'] = pd.to_datetime(data['time'].apply(lambda x: x['$date']))
    df_daily = data.groupby(pd.Grouper(key="time", freq=d_freq)).first().reset_index()#1D, 1W, 1M
    df_daily.dropna(inplace = True)
    return df_daily

#GetAirData
def getIstanbulData(KE, KB, KM, sDate, eDate, param, period):
    max = [41.505331,28.249859]
    min = [40.752296,29.629558]
    
    if (((float(KE) < max[0]) and (float(KB) > max[1])) and ((float(KE) > min[0]) and (float(KB) < min[1]))): 
        jsonData = getKmOutsideSum(float(KE), float(KB), KM, sDate, eDate, param, period)
        if period == None:
            return jsonData 
        else:
            return {
                period: jsonData
            }   
    else:
        return {
                'message': 'location outside of istanbul', 
                'status':302,
            }

def getKmOutsideSum(KE, KB, KM, sDate, eDate, param, period):
    if param:
        param = param.strip().split(',')
        tdict = dict(zip(param, [1 for i in range(len(param))]))
        filter = {'_id':0, 'KE':1 , 'KB':1, 'time':1, **tdict}
        lList = list(outsidesummaries.find({'time':{
            '$gte':datetime.strptime(sDate, '%Y-%m-%dT%H:%M:%S'), #YYYY-mm-ddTHH:MM:ss
            '$lte':datetime.strptime(eDate, '%Y-%m-%dT%H:%M:%S')}
            }, filter))

    else:
        lList = list(outsidesummaries.find({'time':{
        '$gte':datetime.strptime(sDate, '%Y-%m-%dT%H:%M:%S'), #YYYY-mm-ddTHH:MM:ss
        '$lte':datetime.strptime(eDate, '%Y-%m-%dT%H:%M:%S')}
        }, {'_id':0, 'RecordId':0, 'PN':0, 'AA':0, 'DT':0 , 'TM':0}))

    df = pd.DataFrame(lList)
    df['distance'] = list(map(mpu.haversine_distance, zip(df['KE'], df['KB']), zip(np.full(len(df.KE), KE), np.full(len(df.KB), KB))))
    
    df = df.sort_values(['distance','time']).reset_index(drop = True)
    df = df[df['distance']<=int(KM)]

    df = getPeriodData(df, period)

    df['time'] = df['time'].apply(lambda x: datetime.strftime(x, '%Y-%m-%dT%H:%M:%S'))
    dList = df.to_dict(orient='records')

    return dList

def main():
    
    ke = sys.argv[1]
    kb = sys.argv[2]
    km = sys.argv[3]
    sDate = sys.argv[4]
    eDate = sys.argv[5]
    param = sys.argv[6]
    period = sys.argv[7]
    
    return getIstanbulData(ke, kb, km, sDate, eDate, param, period)

if __name__ == '__main__':
    
    print(main())