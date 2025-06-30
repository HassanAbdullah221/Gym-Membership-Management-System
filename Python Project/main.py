from member import Member
from colorama import Fore, Style, init
from datetime import datetime
from tabulate import tabulate
from dateutil.relativedelta import relativedelta

from subscription import Subscribtion

init(autoreset=True)

gym_members = dict()

## Member 1 (updated to remove 'username')
test_member = Member("111", "John Doe", "1995-06-15", "pass123")

# Add subscribtions to the member
sub_j1 = Subscribtion("Silver", "2024-06-01", "", "Card", 300)
sub_j1.set_start_date("2024-06-01", 6)
test_member.new_subsicribe(sub_j1)

sub_j2 = Subscribtion("Gold", "2025-01-01", "", "Cash", 500)
sub_j2.set_start_date("2025-01-01", 6)
test_member.new_subsicribe(sub_j2)

# Add test member to the dictionary
gym_members["111"] = test_member


def add_member():
    print(Fore.CYAN + "------ Add New Gym Member ------")
    member_id = input("Enter member ID: ").strip()
    
    while search_member(member_id) is not None:
        print(Fore.RED + "ID already exists. Try Again!")
        member_id = input("Enter member ID: ").strip()

    name = input("Enter name: ").strip()

    while True:
        birth_date = input("Enter birth date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(birth_date, "%Y-%m-%d")
            break
        except ValueError:
            print(Fore.RED + "Invalid date format! Please enter in YYYY-MM-DD.")

    password = input("Choose a password: ").strip()

    member = Member(member_id, name, birth_date,  password)
    gym_members[member_id] = member

    print(Fore.GREEN + "------------------------------------")
    print(Fore.GREEN + "----- Member added successfully ----")
    print(Fore.GREEN + "------------------------------------")
    print(Fore.GREEN + f"Name: {name}")
    print(Fore.GREEN + f"ID: {member_id}")
    print(Fore.GREEN + f"Birth Date: {birth_date}")
    print(Fore.GREEN + f"Password: {password}")
    print(Fore.GREEN + "------------------------------------")

def delete_member(delete_id):
    if delete_id in gym_members:
        del gym_members[delete_id]
        return True
    return False

def search_member(search_id):
    return gym_members.get(search_id)

# def new_subsicribe(member : Member):
#     menu = '''
# ------------------------------------
# Choose your subsicribtion :
# 1- Silver (1000 SAR) for one month
# 2- Gold (1500 SAR)  for one month
# 3- Diamond (1800 SAR)  for one month
# ------------------------------------
    
#     '''
#     # choice = input(menu)
#     # category = int(choice)
#     choice = int(input( menu + "\nEnter your subsicribe type: "))
#     if choice == 1:
#         subscribe_type = "Silver"
#         base_price = 1000
#     elif choice == 2:
#         subscribe_type = "Gold"
#         base_price = 1500
#     elif choice == 3:
#         subscribe_type = "Diamond"
#         base_price = 1800
#     else:
#         print(Fore.RED + "Invalid subscription choice.")
#         return
    
#     while True:
#         try:
#             duration_months = int(input("Enter number of months: ").strip())
#             if duration_months <= 0:
#                 raise ValueError
#             break
#         except ValueError:
#             print(Fore.RED + "Please enter a valid positive number.")

#     # start_date = datetime.now()
#     # end_date = int(input("Enter the number of months: ")) * 30
#     menu2 = '''
# payment type :
# 1- Cash
# 2- Card
# Your choice: 
#     '''
#     payment_input = int(input(menu2).strip())
    
#     if payment_input == '1':
#         payment_type = "Cash"
#     elif payment_input == '2':
#         payment_type = "Card"
#     else:
#         print(Fore.RED + "Invalid payment type.")
#         return
    
#     # amount_paid = float(input("amount paid : "))
    
#     total_price = base_price * duration_months
#     start_date = datetime.now().strftime("%Y-%m-%d")

#     sub = Subscribtion(subscribe_type, start_date, "", payment_type, total_price)
#     sub.set_start_date(start_date, duration_months)
#     member.new_subsicribe(sub)
#     print(Fore.GREEN + "subscribtions added successfully.")
#     print(Fore.GREEN + "\n====== Invoice ======")
#     print(f"Subscription Type : {subscribe_type}")
#     print(f"Duration (months) : {duration_months}")
#     print(f"Payment Type      : {payment_type}")
#     print(f"Total Amount      : {total_price} SAR")
#     print("=========================")

def new_subsicribe(member: Member):
    menu = '''
------------------------------------
Choose your subscription:
1- Silver (1000 SAR) for one month
2- Gold (1500 SAR)  for one month
3- Diamond (1800 SAR)  for one month
------------------------------------
    '''
    try:
        choice = int(input(menu + "\nEnter your subscription type (1-3): ").strip())
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")
        return

    if choice == 1:
        subscribe_type = "Silver"
        base_price = 1000
    elif choice == 2:
        subscribe_type = "Gold"
        base_price = 1500
    elif choice == 3:
        subscribe_type = "Diamond"
        base_price = 1800
    else:
        print(Fore.RED + "Invalid subscription choice. Please choose 1, 2, or 3.")
        return

    try:
        duration_months = int(input("Enter number of months: ").strip())
        if duration_months <= 0:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Invalid duration. Please enter a positive number.")
        return

    menu2 = '''
Payment type:
1- Cash
2- Card
Your choice: 
    '''
    payment_input = input(menu2).strip()

    if payment_input == '1':
        payment_type = "Cash"
    elif payment_input == '2':
        payment_type = "Card"
    else:
        print(Fore.RED + "Invalid payment type. Please enter 1 or 2.")
        return

    total_price = base_price * duration_months
    start_date = datetime.now().strftime("%Y-%m-%d")

    sub = Subscribtion(subscribe_type, start_date, "", payment_type, total_price)
    sub.set_start_date(start_date, duration_months)
    member.new_subsicribe(sub)

    print(Fore.GREEN + "\nSubscription added successfully.\n")
    print(Fore.GREEN + "-------------- Invoice ---------------")
    print(Fore.GREEN + f"Member ID           : {member.get_member_id()}")
    print(Fore.GREEN + f"Member Name           : {member.get_name()}")
    print(Fore.GREEN + f"Subscription Type   : {subscribe_type}")
    print(Fore.GREEN + f"Duration (months)   : {duration_months}")
    print(Fore.GREEN + f"Payment Type        : {payment_type}")
    print(Fore.GREEN + f"Total Amount        : {total_price} SAR")
    print(Fore.GREEN + f"Subscription Status : {'Active' if member.get_status() else 'Inactive'}")
    print(Fore.GREEN + "--------------------------------------")

def display_all_tables():
    if not gym_members:
        print(Fore.RED + "No data to display.")
        return

    print(Fore.CYAN + "\n==== All Members ====\n")
    headers = ["ID", "Name", "Birth Date", "Age",  "Status"]
    member_table = []

    for member in gym_members.values():
        row = member.to_list()
        member_table.append(row)

    print(tabulate(member_table, headers=headers, tablefmt="fancy_grid"))

   
    print(Fore.MAGENTA + "\n==== All subscribtions ====\n")
    s_headers = ["Member ID", "Category", "Start Date", "End Date", "Payment Type", "Amount Paid"]
    s_table = []

    for member in gym_members.values():
        subs = member.get_subscribtions()
        for s in subs:
            row = [
                member.get_member_id(),
                s.get_subscribe_type(),
                s.get_start_date(),
                s.get_end_date(),
                s.get_payment_type(),
                s.get_amount_paid()
            ]
            s_table.append(row)

    if len(s_table) > 0:
        print(tabulate(s_table, headers=s_headers, tablefmt="fancy_grid"))
    else:
        print(Fore.YELLOW + "No subscribtions recorded.")


while True:
    menu = Fore.CYAN + '''
------------------------------------
------- Gym Member System ----------
------------------------------------
1- Add new gym member
2- Display all members
3- Delete a member
4- Search for a member
5- Display Everything in the system
7- Exit
------------------------------------
'''
    choice = input(menu + Fore.YELLOW + "\nChoose an option: ").strip()

    if choice == '1':
        add_member()
    elif choice == '2':
        if not gym_members:
            print(Fore.RED + "No members found.")
        else:
            print(Fore.CYAN + "\n\n--- All Members ---\n")
            headers = ["ID", "Name", "Birth Date", "Age",  "Status"]
            table = []
            for m in gym_members.values():
                table.append(m.to_list())
            print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

    elif choice == '3':
        delete_id = input(Fore.YELLOW + "Enter the member ID to delete: ").strip()
        if delete_member(delete_id):
            print(Fore.GREEN + "Deleted Successfully!")
        else:
            print(Fore.RED + "Not found. Try Again!")

    elif choice == '4':
        search_id = input(Fore.YELLOW + "Enter the member ID to search: ").strip()
        member = search_member(search_id)
        if member is None:
            print(Fore.RED + "Not found.")
        else:
            print(Fore.GREEN + "\n--- Member Found ---\n\n")
            member.display()
            while True:
                submenu = Fore.BLUE + '''
---- Manage Subscriptions ----
1. Add Subscription
2. View Subscription History
3. Suspend Membership
4. Reactivate Membership
5. Back to Main Menu
------------------------------
'''
                x = input(submenu + Fore.YELLOW + "\nChoose an option: ").strip()
                if x == '1':
                    new_subsicribe(member)
                elif x == '2':
                    member.display_subscribtions_history()
                elif x == '3':
                    member.pend_subscribtions()
                elif x == '4':
                    member.activate_subsicribtion()
                elif x == '5':
                    break
                else:
                    print(Fore.RED + "Invalid option. Try again.")

    elif choice == '5':
        display_all_tables()
    
    elif choice == '7':
        print(Fore.GREEN + "Thank You. Stay healthy!")
        break

    else:
        print(Fore.RED + "Invalid choice. Try again.")
