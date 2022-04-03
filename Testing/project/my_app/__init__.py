import json
import pandas as pd

class App(): #define app 
    def __init__(self, database):

        PATH = "C:/Users/tolga/OneDrive/Masaüstü/python-topics/Testing/project/tests/integration/"

        self.database = PATH + database

        with open(self.database, 'r') as f:
            self.customers = json.load(f)
    
    def get_customer(self, id):
        for customer in self.customers:
            if customer['id'] == id:
                return customer
        