
from datetime import datetime
from dateutil.relativedelta import relativedelta

SILVER_PRICE = 1000
GOLD_PRICE = 1500 
DIAMOND_PRICE = 1800

class Subscribtion:
    def __init__(self, subscribe_type: int, start_date: str, end_date: str, payment_type: str, amount_paid: int):
        self.__subscribe_type = subscribe_type
        self.__start_date = start_date
        self.__end_date = end_date
        self.__payment_type = payment_type
        self.__amount_paid = amount_paid

    
    def get_subscribe_type(self):
        return self.__subscribe_type

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_payment_type(self):
        return self.__payment_type

    def get_amount_paid(self):
        return self.__amount_paid

    def set_subscribe_type(self, subscribe_type):
        self.__subscribe_type = subscribe_type

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_start_date(self, start_date: str, duration_months: int):
        self.__start_date = start_date
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = start + relativedelta(months=duration_months)
        self.__end_date = end.strftime("%Y-%m-%d")

    def set_payment_type(self, payment_type):
        self.__payment_type = payment_type

    def set_amount_paid(self, amount):
        self.__amount_paid = amount

