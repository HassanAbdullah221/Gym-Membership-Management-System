from member import Member
from subscription import Subscribtion
from datetime import datetime, timedelta
from colorama import Fore, Style, init
from tabulate import tabulate
from __init__ import SILVER_PRICE, GOLD_PRICE, DIAMOND_PRICE
import json


init(autoreset=True)

gym_members = dict()

def load_memebrs():
    global gym_members

    with open('gym_data.json', 'r') as file:
        data = json.load(file)

    
    for member in data:
        loaded_member = Member(member["member_id"], member["name"], member["birth_date"])

        for sub in member["subscriptions"]:
            loaded_sub = Subscribtion(sub["subscribe_type"], datetime.strptime(sub["start_date"], "%Y-%m-%d"), datetime.strptime(sub["end_date"], "%Y-%m-%d"), sub["payment_type"], sub["amount_paid"])
            loaded_member.new_subscribe(loaded_sub)
            
        
        gym_members[member["member_id"]] = loaded_member



def add_member():
    print(Fore.BLUE + "------ Add New Gym Member ------")
    while True:
        member_id = input(Fore.YELLOW + "Enter member ID (4 numbers): ").strip()
        if not member_id.isdigit() or len(member_id) != 4:
            print(Fore.RED + "ID must be exactly 4 numbers .")
            continue
        if search_member(member_id) is not None:
            print(Fore.RED + "ID already exists. Try again!")
            continue
        break

    while True:
        name = input(Fore.YELLOW + "Enter name: ").strip()
        if name:
            break
        print(Fore.RED + "Name cannot be empty!")

    while True:
        birth_date = input(Fore.YELLOW + "Enter birth date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(birth_date, "%Y-%m-%d")
            break
        except ValueError:
            print(Fore.RED + "Invalid date format! Please enter in YYYY-MM-DD.")


    member = Member(member_id, name, birth_date)
    gym_members[member_id] = member

    age = member.get_age()
    print(Fore.GREEN + "----- Member added successfully ----")
    print(Fore.GREEN + tabulate([[member_id, name, age ,birth_date]], headers=["ID", "Name", "Age" ,"Birth Date"], tablefmt="fancy_grid"))
    save_to_json()

def delete_member(delete_id):
    if delete_id in gym_members:
        del gym_members[delete_id]
        save_to_json()
        return True
    return False


def search_member(search_id):
    return gym_members.get(search_id)


def new_subscribe(member: Member):
    menu = f'''
------------------------------------
Choose your subscription:
1- Silver ({SILVER_PRICE} SAR / month)
2- Gold ({GOLD_PRICE} SAR / month)
3- Diamond ({DIAMOND_PRICE} SAR / month)
------------------------------------
    '''
    try:
        choice = int(input(Fore.BLUE + menu + "\n" + Fore.YELLOW + "Enter your subscription type (1-3): ").strip())
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")
        return

    if choice == 1:
        subscribe_type = "Silver"
        base_price = SILVER_PRICE
    elif choice == 2:
        subscribe_type = "Gold"
        base_price = GOLD_PRICE
    elif choice == 3:
        subscribe_type = "Diamond"
        base_price = DIAMOND_PRICE
    else:
        print(Fore.RED + "Invalid subscription choice. Please choose 1, 2, or 3.")
        return

    try:
        duration_months = int(input(Fore.YELLOW + "Enter number of months: ").strip())
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
    payment_input = input(Fore.BLUE + menu2 + Fore.YELLOW).strip()

    if payment_input == '1':
        payment_type = "Cash"
    elif payment_input == '2':
        payment_type = "Card"
    else:
        print(Fore.RED + "Invalid payment type. Please enter 1 or 2.")
        return

    total_price = base_price * duration_months
    start_date = datetime.now()

    sub = Subscribtion(subscribe_type, start_date, duration_months, payment_type, total_price)
    member.new_subscribe(sub)

    print(Fore.GREEN + "\nSubscription added successfully.\n")
    table = [[
        member.get_member_id(),
        member.get_name(),
        subscribe_type,
        duration_months,
        payment_type,
        total_price
    ]]
    headers = ["Member ID", "Name", "Type", "Months", "Payment", "Total (SAR)"]
    print(Fore.GREEN + tabulate(table, headers=headers, tablefmt="fancy_grid"))
    save_to_json()

def display_all():
    if not gym_members:
        print(Fore.RED + "No data to display.")
        return

    print(Fore.BLUE + "\n==== All Members ====")
    for member in gym_members.values():
        print("------------------------------------" )
        member.display()

    print(Fore.BLUE + "\n==== All Subscriptions ====")
    for member in gym_members.values():
        print("------------------------------------" )
        print(Fore.BLUE + f"Member ID: {member.get_member_id()}")
        member.display_subscribtions_history()

def update_all_statuses():
    for member in gym_members.values():
        if member.get_subscribtions():
            for sub in member.get_subscribtions():
                if datetime.now() > sub.get_end_date():
                    sub.set_status("expired")

def save_to_json(filename="gym_data.json"):
    update_all_statuses() 
    
    data = []
    for m in gym_members.values():
        member_dict = m.to_dict()
        data.append(member_dict)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    # print(Fore.GREEN + f"Data saved to {filename}")

def display_subscribtions_history(self):
       
        if not self.__subscribtions:
            print(Fore.YELLOW + "No subscriptions found for this member.")
            return

        today = datetime.now().date()
        table = []
        for s in self.__subscribtions:
            try:
                end_dt = datetime.strptime(s.get_end_date(), "%Y-%m-%d").date()
            except Exception:
                status = "Unknown"
            else:
                status = "Active" if end_dt >= today else "Expired"

            table.append([
                s.get_subscribe_type(),
                s.get_start_date().date(),
                s.get_end_date().date(),
                s.get_payment_type(),
                s.get_amount_paid(),
                status
            ])

        print(table)
        headers = ["Type", "Start Date", "End Date", "Payment", "Amount Paid", "Status"]
        print(Fore.CYAN + tabulate(table, headers=headers, tablefmt="fancy_grid"))
 
def update_member_info():
    member_id = input(Fore.YELLOW + "Enter the member ID to update: ").strip()

    if not member_id.isdigit() or len(member_id) != 4:
        print(Fore.RED + "Invalid ID format. Must be 4 digits.")
        return

    member = search_member(member_id)
    if member is None:
        print(Fore.RED + "Member not found.")
        return

    print(Fore.GREEN + "\n--- Current Member Info ---")
    member.display()

    print(Fore.BLUE + "\n--- Update Options ---")
    print("1. Update Member ID")
    print("2. Update Name")
    print("3. Update Birth Date")
    print("4. Cancel")

    choice = input(Fore.YELLOW + "Choose what to update (1-4): ").strip()

    if choice == '1':
        new_id = input(Fore.YELLOW + "Enter new 4-digit Member ID: ").strip()
        if not new_id.isdigit() or len(new_id) != 4:
            print(Fore.RED + "ID must be exactly 4 digits.")
            return
        
        if new_id in gym_members:
            print(Fore.RED + "This ID already exists. Try another one.")
            return
        
        del gym_members[member_id]
        
        member.set_member_id(new_id)
        
        
        gym_members[new_id] = member
        print(Fore.GREEN + "Member ID updated successfully.")

    elif choice == '2':
        
        new_name = input(Fore.YELLOW + "Enter new name: ").strip()
        
        if not new_name:
            print(Fore.RED + "Name cannot be empty.")
            return
        
        member.set_name(new_name)
        print(Fore.GREEN + "Name updated successfully.")

    elif choice == '3':
        
        new_birth = input(Fore.YELLOW + "Enter new birth date (YYYY-MM-DD): ").strip()
        if not new_birth:
            print(Fore.RED + "Birth date cannot be empty.")
            return
        try:
            datetime.strptime(new_birth, "%Y-%m-%d")
        except ValueError:
            print(Fore.RED + "Invalid date format.")
            return
        
        member.set_birth_date(new_birth)
        print(Fore.GREEN + "Birth date updated successfully.")

    elif choice == '4':
        print(Fore.BLUE + "Update cancelled.")
        return

    else:
        print(Fore.RED + "Invalid option.")
        return

    save_to_json()


def dispaly_all(filename="gym_data.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not data:
            print(Fore.RED + "No data found in the JSON file.")
            return

        print(Fore.BLUE + "\n==== Members from JSON File ====\n")

        for member_data in data:
            print("---------------------------")

            member_table = [[
                member_data['member_id'],
                member_data['name'],
                member_data['birth_date'],
                member_data.get('age', 'N/A'),
                member_data.get('membership_activation', 'N/A')
            ]]
            headers = ["ID", "Name", "Birth Date", "Age", "Status"]
            print(Fore.GREEN + tabulate(member_table, headers=headers, tablefmt="fancy_grid"))

            subs = member_data.get("subscriptions", [])
            if subs:
                sub_table = []
                for s in subs:
                    row = [
                        s["subscribe_type"],
                        s["start_date"].date(),
                        s["end_date"].date(),
                        s["payment_type"],
                        s["amount_paid"],
                        s.get("status", "N/A")
                    ]
                    sub_table.append(row)

                sub_headers = ["Type", "Start", "End", "Payment", "Amount", "Status"]
                print(Fore.CYAN + tabulate(sub_table, headers=sub_headers, tablefmt="fancy_grid"))
            else:
                print(Fore.YELLOW + "No subscriptions found.")


    except FileNotFoundError:
        print(Fore.RED + f"{filename} not found.")
    except json.JSONDecodeError:
        print(Fore.RED + "Invalid JSON format.")


load_memebrs()
while True:
    menu = '''
------------------------------------
------- Gym Member System ----------
------------------------------------
1- Add new gym member
2- Display all members
3- Delete a member
4- Update member information
5- Search for a member to manage subscriptions
6- Display Everything in the system
7- Exit
------------------------------------
'''
    choice = input(Fore.BLUE + menu + Fore.YELLOW + "\nChoose an option: ").strip()

    if choice == '1':
        add_member()

    elif choice == '2':
        if not gym_members:
            print(Fore.RED + "No members found.")
        else:
            print(Fore.BLUE + "\n--- All Members ---\n")
            for m in gym_members.values():
                print("------------------------------")
                m.display()

    elif choice == '3':
        delete_id = input(Fore.YELLOW + "Enter the member ID to delete: ").strip()
        if delete_member(delete_id):
            print(Fore.GREEN + "Deleted Successfully!")
        else:
            print(Fore.RED + "Not found. Try Again!")

    elif choice == '4':
        update_member_info() 

    elif choice == '5':
        search_id = input(Fore.YELLOW + "Enter the member ID to search: ").strip()
        member = search_member(search_id)
        if member is None:
            print(Fore.RED + "Not found.")
        else:
            print(Fore.GREEN + "\n--- Member Found ---\n")
            member.display()

            while True:
                submenu = '''
---- Manage Subscriptions ----
1. Add Subscription
2. View Subscription History
3. Suspend Membership
4. Reactivate Membership
5. Back to Main Menu
------------------------------
'''
                x = input(Fore.BLUE + submenu + Fore.YELLOW + "\nChoose an option: ").strip()
                if x == '1':
                    new_subscribe(member)
                elif x == '2':
                    member.display_subscribtions_history()
                elif x == '3':
                    member.pend_subscribtions()
                    save_to_json()
                elif x == '4':
                    member.activate_subsicribtion()
                    save_to_json()
                elif x == '5':
                    break
                else:
                    print(Fore.RED + "Invalid option. Try again.")

    elif choice == '6':
        display_all()

    elif choice == '7':
        print(Fore.GREEN + "Thank You. Stay healthy!")
        break

    else:
        print(Fore.RED + "Invalid choice. Try again.")
