from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from colorama import Fore

class Subscribtion:
    def __init__(self, subscribe_type, start_date, duration_months, payment_type, amount_paid):
        self.__subscribe_type = subscribe_type
        self.__start_date = start_date

        if type(duration_months) == int:
            self.__end_date = start_date + timedelta(days=(30 * duration_months))
        else:
            self.__end_date = duration_months    

        self.__payment_type = payment_type
        self.__amount_paid = amount_paid
        self.__membership_activation = "activate"

    def set_status(self, new_status):
        self.__membership_activation = new_status

    def get_status(self):
        return self.__membership_activation

    def pend_subscribtions(self):
        self.set_status("suspend")
        self.__pend_date = datetime.now()

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

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_start_date(self, start_date, duration_months):
        self.__start_date = start_date
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = start + relativedelta(months=duration_months)
        self.__end_date = end.strftime("%Y-%m-%d")

    
    def set_payment_type(self, payment_type):
        self.__payment_type = payment_type

    def set_amount_paid(self, amount):
        self.__amount_paid = amount

    def to_dict(self):
        return {
            "subscribe_type": self.__subscribe_type,
            "start_date": self.__start_date.strftime("%Y-%m-%d"),
            "end_date": self.__end_date.strftime("%Y-%m-%d"),
            "payment_type": self.__payment_type,
            "amount_paid": self.__amount_paid,
            "status": self.__membership_activation
        }
