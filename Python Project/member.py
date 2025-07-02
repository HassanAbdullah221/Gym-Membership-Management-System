# member.py
from datetime import datetime, timedelta
from subscription import Subscribtion
from colorama import Fore, Style
from tabulate import tabulate

PEND_LIMIT = 60

class Member:
    def __init__(self, member_id, name, birth_date):
        self.__name = name
        self.__member_id = member_id
        self.__birth_date = birth_date
        self.__age = self.__calculate_age()
        self.__membership_activation = "activate"
        self.__subscribtions = []
        self.__pend_credit = PEND_LIMIT

    def pend_subscribtions(self):
        
        if self.__membership_activation == 'expired':
            print("Cannot reactivate.")
            return
        
        self.__membership_activation = 'suspend'
        self.pend_date = datetime.now()
        self.__subscribtions[-1].pend_subscribtions()
        print(Fore.YELLOW + "Membership has been suspended.")

    def activate_subsicribtion(self):
        
        if self.__membership_activation == 'expired':
            print("Cannot reactivate.")
            return
        
        self.__membership_activation = 'activate'
        current_sub = self.__subscribtions[-1]
        current_sub.set_status("activate")
        additional_days = datetime.now() - self.pend_date
        extend_days = min(additional_days.days, self.__pend_credit)
        new_date = current_sub.get_end_date() + timedelta(days=extend_days)
        self.__pend_credit -= extend_days
        current_sub.set_end_date(new_date)
        print(Fore.GREEN + f"Membership reactivated")

    def __calculate_age(self):
        birth = datetime.strptime(self.__birth_date, "%Y-%m-%d")
        today = datetime.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def new_subscribe(self, subscription: Subscribtion):
        self.__subscribtions.append(subscription)

    def display(self):
        table = [[
            self.get_member_id(),
            self.get_name(),
            self.get_birth_date(),
            self.get_age(),
        ]]
        headers = ["ID", "Name", "Birth Date", "Age"]
        print(Fore.CYAN + tabulate(table, headers=headers, tablefmt="fancy_grid"))

    def to_list(self):
        return [
            self.__member_id,
            self.__name,
            self.__birth_date,
            self.__age,
            self.__membership_activation
        ]

    def display_subscribtions_history(self):
        if not self.__subscribtions:
            print(Fore.YELLOW + "No subscriptions found for this member.")
            return

        table = []
        for s in self.__subscribtions:
            if datetime.now() > s.get_end_date() and s.get_status() != "expired":
                s.set_status("expired")
            
            row = [
                s.get_subscribe_type(),
                s.get_start_date().date(),
                s.get_end_date().date(),
                s.get_payment_type(),
                s.get_amount_paid(),
                s.get_status()
            ]
            table.append(row)

        headers = ["Type", "Start Date", "End Date", "Payment", "Amount Paid", "Status"]
        print(Fore.MAGENTA + tabulate(table, headers=headers, tablefmt="fancy_grid"))

    # Getters
    def get_member_id(self):
        return self.__member_id

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def get_age(self):
        return self.__age

    def get_membership_status(self):
        if self.__subscribtions:
            all_expired = True
            for sub in self.__subscribtions:
                if datetime.now() > sub.get_end_date():
                    sub.set_status("expired")
                else:
                    all_expired = False
            if all_expired:
                self.__membership_activation = "expired"
        return self.__membership_activation

    
    def get_subscribtions(self):
        return self.__subscribtions


    def set_member_id(self, new_id):
        self.__member_id = new_id

    def set_name(self, new_name):
        self.__name = new_name

    def set_birth_date(self, new_birth):
        self.__birth_date = new_birth
        self.__age = self.__calculate_age()

    def set_subscribtions(self, subscriptions):
        self.__subscribtions = subscriptions
            
    def to_dict(self):
        subscriptions_list = []
        for s in self.__subscribtions:
            sub_dict = s.to_dict()
            subscriptions_list.append(sub_dict)
        member_data = {
            "member_id": self.__member_id,
            "name": self.__name,
            "birth_date": self.__birth_date,
            "age": self.__age,
            "membership_activation": self.__membership_activation,
            "subscriptions": subscriptions_list
        }

        return member_data
