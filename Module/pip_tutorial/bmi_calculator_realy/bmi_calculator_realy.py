class PersonBMI:
    def __init__(self, age, weight, height, gender):
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.bmi = 0
        
    def calculate_bmi(self):
        if self.gender.upper() == "male".upper():
            self.bmi = self.weight /(self.height/100 * self.height/100)*0.98
            
        elif self.gender.upper() == "female".upper():
            self.bmi = self.weight /(self.height/100 * self.height/100)*0.94
            
        return self.bmi
    
    def conclusions(self):
        
        if self.bmi < 18.5:
            print("Your weight is too low")
        elif self.bmi < 24.9:
            print("Your weight is normal")
        elif self.bmi < 29.9:
            print("Your have an overweight")
        elif self.bmi < 34.9:
            print("1st level overweight")
        elif self.bmi < 39.9:
            print("2nd level overweight")
        else:
            print("3rd level overweight")