
from datetime import datetime
from matplotlib.dates import relativedelta

class Subscription:
    def __init__(self, category: str, start_date: str, end_date: str, payment_type: str, amount_paid: int):
        self.__category = category
        self.__start_date = start_date
        self.__end_date = end_date
        self.__payment_type = payment_type
        self.__amount_paid = amount_paid

    def get_category(self):
        return self.__category

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_payment_type(self):
        return self.__payment_type

    def get_amount_paid(self):
        return self.__amount_paid

    def set_category(self, category):
        self.__category = category

    def set_start_date(self, start_date: str, duration_months: int):
        self.__start_date = start_date
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = start + relativedelta(months=duration_months)
        self.__end_date = end.strftime("%Y-%m-%d")

    def set_payment_type(self, payment_type):
        self.__payment_type = payment_type

    def set_amount_paid(self, amount):
        self.__amount_paid = amount

