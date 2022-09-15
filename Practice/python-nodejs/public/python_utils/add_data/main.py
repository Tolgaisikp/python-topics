from datetime import datetime
import json
import sys
import pandas as pd
from pymongo import MongoClient
from sqlalchemy import false

from ibb import addIbbCol
from openweather import addWeatherCol
from process import CreateSummaryModel, updateIndexes, mergeDataFrame

#Model
client = MongoClient('mongodb://localhost:27017')

#Database
SimilarityDB = client['SimilarityDB']
testOutsideSummaries = SimilarityDB['testOutsideSummaries']
testDateIndexes = SimilarityDB['testDateIndexes']
testDeviceIndexes = SimilarityDB['testDeviceIndexes']

def main(rawTestData):
    testData = CreateSummaryModel(rawTestData)

    #Add New Attribute IBB Api
    ibblastData = addIbbCol(testData)

    #Add New Attribute OpenWeatherApi
    weatherlastData = addWeatherCol(testData)

    try:
        lastData = mergeDataFrame(pd.DataFrame([ibblastData]), pd.DataFrame([weatherlastData]))[0]

        lastData['time'] = datetime.strftime(lastData['time'], "%Y-%m-%d %H:%M:%S")
    
        return json.dumps(lastData)
    except:
        return json.dumps(None)
        

if __name__ == '__main__':

    model = json.loads(sys.argv[1])
    data = main(model)

    print(data)