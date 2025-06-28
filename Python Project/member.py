from datetime import datetime

from measurement import Measurement
from subscription import Subscription

from tabulate import tabulate
from colorama import Fore

class Member:
    def __init__(self, member_id, name, birth_date, username, password):
        self.__name = name
        self.__username = username
        self.__member_id = member_id
        self.__birth_date = birth_date
        self.__age = self.__calculate_age()
        self.__password = password
        self.__membership_status = "Active"
        self.__subscription = []
        self.__measurement = []

    def __calculate_age(self):
        birth = datetime.strptime(self.__birth_date, "%Y-%m-%d")
        today = datetime.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def new_subsicribe(self , subsicription  : Subscription ):
        self.__subscription.append(subsicription)
    
    
    def new_measurement(self , measurement : Measurement ):
        self.__measurement.append(measurement)
    
    # def display_measurement_history(self):
    #     for m in self.__measurement :
    #         m.display()
        
    def display_subscription_history(self):
        if not self.__subscription:
            print(Fore.YELLOW + "No subscriptions found.")
            return
        
        table = []
        for s in self.__subscription:
            table.append([
                s.get_category(),
                s.get_start_date(),
                s.get_end_date(),
                s.get_payment_type(),
                s.get_amount_paid()
            ])

        headers = ["Category", "Start Date", "End Date", "Payment Type", "Amount Paid"]
        table_str = tabulate(table, headers=headers, tablefmt="fancy_grid")
        print(Fore.YELLOW + table_str)
        
    def display_measurement_history(self):
        if not self.__measurement:
            print(Fore.YELLOW + "No measurements found.")
            return

        table = []
        for m in self.__measurement:
            table.append([
                m.get_height_cm(),
                m.get_weight_kg(),
                m.get_bmi(),
                m.get_date()
            ])
        
        headers = ["Height (cm)", "Weight (kg)", "BMI", "Date"]
        table_str = tabulate(table, headers=headers, tablefmt="fancy_grid")
        print(Fore.YELLOW + table_str)    
    
        
    # def display(self):
    #     print("------ Member Information ------")
    #     print(f"ID: {self.get_member_id()}")
    #     print(f"Name: {self.get_name()}")
    #     print(f"Birth Date: {self.get_birth_date()}")
    #     print(f"Age: {self.get_age()}")
    #     print(f"Username: {self.get_username()}")
    #     print(f"Password: {self.get_password()}")
    #     print(f"Membership Status: {self.get_membership_status()}")
    
    def display(self):
        table = [[
            self.get_member_id(),
            self.get_name(),
            self.get_birth_date(),
            self.get_age(),
            self.get_username(),
            self.get_membership_status()
        ]]
        headers = ["ID", "Name", "Birth Date", "Age", "Username", "Status"]
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
   
    def to_list(self):
        return [
            self.__member_id,
            self.__name,
            self.__birth_date,
            self.__age,
            self.__username,
            self.__membership_status
        ]

    def get_member_id(self):
        return self.__member_id

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def get_age(self):
        return self.__age

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_membership_status(self):
        return self.__membership_status

    def get_subscription(self):
        return self.__subscription

    def get_measurement(self):
        return self.__measurement

    def set_subscription(self, subscription):
        self.__subscription = subscription

    def set_measurement(self, measurement):
        self.__measurement = measurement