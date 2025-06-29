from datetime import datetime , timedelta
from tabulate import tabulate
from colorama import Fore

from subscription import Subscribtion

PEND_LIMIT = 60 


class Member:
    def __init__(self, member_id, name, birth_date,  password):
        self.__name = name
        self.__member_id = member_id
        self.__birth_date = birth_date
        self.__age = self.__calculate_age()
        self.__password = password
        self.__membership_activation = True
        self.__subscribtions = []
        self.__pend_credit = PEND_LIMIT

    def pend_subscribtions(self):
        self.__membership_activation = False
        self.__pend_date = datetime.now()
       
    def activate_subsicribtion(self):
        self.__membership_activation = True
        current_subsicribtion = self.__subscribtions[-1]
        additional_days = datetime.now() - self.__pend_date
        new_date = current_subsicribtion.get_end_date() + timedelta(days= min( additional_days.days, self.__pend_credit ) )
        self.__pend_credit = self.__pend_credit - additional_days.days
        current_subsicribtion.set_end_date(new_date)
        
            
    

    def __calculate_age(self):
        birth = datetime.strptime(self.__birth_date, "%Y-%m-%d")
        today = datetime.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def new_subsicribe(self, subscribtions: Subscribtion):
        self.__subscribtions.append(subscribtions)

   
    def set_status(self, new_status):
        self.__membership_activation = new_status

    def get_status(self):
        return self.__membership_activation

    def display_subscribtions_history(self):
        if not self.__subscribtions:
            print(Fore.YELLOW + "No subscribtions found.")
            return

        table = []
        for s in self.__subscribtions:
            table.append([
                s.get_category(),
                s.get_start_date(),
                s.get_end_date(),
                s.get_payment_type(),
                s.get_amount_paid()
            ])

        headers = ["Category", "Start Date", "End Date", "Payment Type", "Amount Paid"]
        print(Fore.CYAN + tabulate(table, headers=headers, tablefmt="fancy_grid"))

   
    def display(self):
        table = [[
            self.get_member_id(),
            self.get_name(),
            self.get_birth_date(),
            self.get_age(),
            self.get_membership_status()
        ]]
        headers = ["ID", "Name", "Birth Date", "Age",  "Status"]
        print(Fore.GREEN + tabulate(table, headers=headers, tablefmt="fancy_grid"))

    def to_list(self):
        return [
            self.__member_id,
            self.__name,
            self.__birth_date,
            self.__age,
            self.__membership_activation
        ]

    def get_member_id(self):
        return self.__member_id

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def get_age(self):
        return self.__age

    def get_password(self):
        return self.__password

    def get_membership_status(self):
        return self.__membership_activation

    def get_subscribtions(self):
        return self.__subscribtions

    def set_subscribtions(self, subscribtions):
        self.__subscribtions = subscribtions

   