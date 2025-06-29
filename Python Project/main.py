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

def new_subsicribe(member : Member):
    menu = '''
    Choose your subsicribtion :
    1- Silver
    2- Gold
    3- Diamond
    '''
    choice = input(menu)
    category = int(choice)
    subscribe_type = input("Enter your subsicribe type: ")
    start_date = datetime.now()
    end_date = int(input("Enter the number of months: ")) * 30
    menu2 = '''
    payment type :
    1- Cash
    2- Card
    '''
    payment_type = int(input(menu2))
    amount_paid = float(input("amount paid : "))
    
    
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
                s.get_category(),
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
------------------------------------
1- Add new subscribtion
2- Display all subscribtions
3- Pend subsicribe
4- Back to main menu
------------------------------------
'''
                x = input(submenu + Fore.YELLOW + "\nChoose an option: ").strip()
                if x == '1':
                    sub = new_subsicribe()
                    member.new_subsicribe(sub)
                    print(Fore.GREEN + "subscribtions added successfully.")
                elif x == '2':
                    member.display_subscribtions_history()

                elif x == '3':
                    member.pend_subscribtions()
                elif x == '4':
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
