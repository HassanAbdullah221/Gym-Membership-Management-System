class Measurement:
    def __init__(self, height_cm : float, weight_kg : float, date:str):
        self.__height_cm = height_cm
        self.__weight_kg = weight_kg
        self.__bmi = self.__calculate_bmi()
        self.__date = date 

    def __calculate_bmi(self):
        height_m = self.__height_cm / 100
        return round(self.__weight_kg / (height_m ** 2), 2)

    def get_height_cm(self):
        return self.__height_cm

    def get_weight_kg(self):
        return self.__weight_kg

    def get_bmi(self):
        return self.__bmi

    def get_date(self):
        return self.__date

    def set_height_cm(self, height_cm : float):
        self.__height_cm = height_cm
        self.__bmi = self.__calculate_bmi()  

    def set_weight_kg(self, weight_kg : float):
        self.__weight_kg = weight_kg
        self.__bmi = self.__calculate_bmi()  

    def set_date(self, date):
        self.__date = date
