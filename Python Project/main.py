from matplotlib import pyplot as plt
from measurement import Measurement
from member import Member
from subscription import Subscription
from colorama import Fore, Style, init
from datetime import datetime
from tabulate import tabulate

init(autoreset=True)

gym_members = dict()
# Prepopulate test members with full data

# Member 1
test_member = Member("111", "John Doe", "1995-06-15", "john_doe", "pass123")
test_member.new_measurement(Measurement(180, 75, "2024-06-28 10:00:00"))
test_member.new_measurement(Measurement(182, 78, "2025-01-15 14:30:00"))
test_member.new_measurement(Measurement(181, 77, "2025-06-01 09:00:00"))

sub_j1 = Subscription("Silver", "2024-06-01", "", "Card", 300)
sub_j1.set_start_date("2024-06-01", 6)
test_member.new_subsicribe(sub_j1)

sub_j2 = Subscription("Gold", "2025-01-01", "", "Cash", 500)
sub_j2.set_start_date("2025-01-01", 6)
test_member.new_subsicribe(sub_j2)

gym_members["111"] = test_member

# Member 2
test_member1 = Member("101", "Alice Smith", "1990-05-10", "alice", "alicepass")
test_member1.new_measurement(Measurement(165, 60, "2025-01-10 09:00:00"))
test_member1.new_measurement(Measurement(165, 58, "2025-06-10 09:00:00"))
test_member1.new_measurement(Measurement(165, 56, "2025-06-25 10:15:00"))

sub1 = Subscription("Gold", "2025-01-01", "", "Card", 600)
sub1.set_start_date("2025-01-01", 6)
test_member1.new_subsicribe(sub1)

sub1b = Subscription("Diamond", "2025-07-01", "", "Card", 800)
sub1b.set_start_date("2025-07-01", 6)
test_member1.new_subsicribe(sub1b)

gym_members["101"] = test_member1

# Member 3
test_member2 = Member("102", "Bob Johnson", "1985-12-22", "bobby", "secure123")
test_member2.new_measurement(Measurement(180, 85, "2024-12-01 12:00:00"))
test_member2.new_measurement(Measurement(180, 83, "2025-03-01 12:00:00"))

sub2 = Subscription("Silver", "2025-03-01", "", "Cash", 300)
sub2.set_start_date("2025-03-01", 3)
test_member2.new_subsicribe(sub2)

sub2b = Subscription("Gold", "2025-06-01", "", "Card", 500)
sub2b.set_start_date("2025-06-01", 6)
test_member2.new_subsicribe(sub2b)

gym_members["102"] = test_member2

# Member 4
test_member3 = Member("103", "Diana Rose", "1998-08-08", "diana", "rosepass")
test_member3.new_measurement(Measurement(158, 52, "2025-01-05 08:00:00"))
test_member3.new_measurement(Measurement(158, 50, "2025-06-05 08:00:00"))

sub3 = Subscription("Silver", "2025-01-01", "", "Card", 320)
sub3.set_start_date("2025-01-01", 3)
test_member3.new_subsicribe(sub3)

sub3b = Subscription("Gold", "2025-04-01", "", "Cash", 490)
sub3b.set_start_date("2025-04-01", 6)
test_member3.new_subsicribe(sub3b)

gym_members["103"] = test_member3
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

    username = input("Choose a username: ").strip()
    password = input("Choose a password: ").strip()

    member = Member(member_id, name, birth_date, username, password)
    gym_members[member_id] = member

    print(Fore.GREEN + "------------------------------------")
    print(Fore.GREEN + "----- Member added successfully ----")
    print(Fore.GREEN + "------------------------------------")
    print(Fore.GREEN + f"Name: {name}")
    print(Fore.GREEN + f"Username: {username}")
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

def create_measurements():
    try:
        height = float(input("Enter your height: "))
        weight = float(input("Enter your weight: "))

        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive numbers.")

        date = str(datetime.now())
        return Measurement(height, weight, date)

    except ValueError:
        print(Fore.RED + "Invalid input. Height and weight must be numbers greater than 0.")
        return create_measurements()

def create_subscription():
    try:
        category = input("Enter subscription category (Silver, Gold, Diamond): ").strip()
        start_date = datetime.now()
        print(Fore.CYAN + f"Start Date set to today: {start_date.strftime('%Y-%m-%d')}")

        duration_months = int(input("Enter subscription duration (in months): "))
        payment_type = input("Enter payment type (Cash or Card): ").strip()
        amount_paid = float(input("Enter amount paid: "))

        if duration_months <= 0 or amount_paid < 0:
            raise ValueError("Duration must be positive and amount cannot be negative.")

        sub = Subscription(category, start_date, "", payment_type, amount_paid)
        sub.set_start_date(start_date, duration_months)
        return sub

    except ValueError:
        print(Fore.RED + "Invalid input. Please enter valid numbers for duration and amount.")
        return create_subscription()

def display_all_tables():
    if not gym_members:
        print(Fore.RED + "No data to display.")
        return

    print(Fore.CYAN + "\n==== All Members ====\n")
    headers = ["ID", "Name", "Birth Date", "Age", "Username", "Status"]
    member_table = []

    for member in gym_members.values():
        row = member.to_list()
        member_table.append(row)

    print(tabulate(member_table, headers=headers, tablefmt="fancy_grid"))

    print(Fore.BLUE + "\n==== All Measurements ====\n")
    m_headers = ["Member ID", "Height (cm)", "Weight (kg)", "BMI", "Date"]
    m_table = []

    for member in gym_members.values():
        measurements = member.get_measurement()
        for m in measurements:
            row = [
                member.get_member_id(),
                m.get_height_cm(),
                m.get_weight_kg(),
                m.get_bmi(),
                m.get_date()
            ]
            m_table.append(row)

    if len(m_table) > 0:
        print(tabulate(m_table, headers=m_headers, tablefmt="fancy_grid"))
    else:
        print(Fore.YELLOW + "No measurements recorded.")

    print(Fore.MAGENTA + "\n==== All Subscriptions ====\n")
    s_headers = ["Member ID", "Category", "Start Date", "End Date", "Payment Type", "Amount Paid"]
    s_table = []

    for member in gym_members.values():
        subs = member.get_subscription()
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
        print(Fore.YELLOW + "No subscriptions recorded.")

def change_member_status():
    member_id = input(Fore.YELLOW + "Enter the member ID to change status: ").strip()
    member = search_member(member_id)

    if member is None:
        print(Fore.RED + "Member not found.")
    else:
        print(Fore.CYAN + f"Current status: {member.get_status()}")

        while True:
            new_status = input("Enter new status (Active / Inactive / Suspended): ").strip().capitalize()

            if new_status == "Active":
                member.set_status("Active")
                print(Fore.GREEN + "Status updated successfully to 'Active'.")
                break
            elif new_status == "Inactive":
                member.set_status("Inactive")
                print(Fore.GREEN + "Status updated successfully to 'Inactive'.")
                break
            elif new_status == "Suspended":
                member.set_status("Suspended")
                print(Fore.GREEN + "Status updated successfully to 'Suspended'.")
                break
            else:
                print(Fore.RED + "Invalid status. Please enter one of: Active, Inactive, or Suspended.")


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
6- Change member status
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
            headers = ["ID", "Name", "Birth Date", "Age", "Username", "Status"]
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
            print(Fore.GREEN + "--- Member Found ---")
            member.display()
            while True:
                submenu = Fore.BLUE + '''
------------------------------------
1- Add new measurement
2- Add new subscription
3- Display all measurements
4- Display all subscriptions 
5- Back to main menu
------------------------------------
'''
                x = input(submenu + Fore.YELLOW + "\nChoose an option: ").strip()
                if x == '1':
                    measurements = create_measurements()
                    member.new_measurement(measurements)
                    print(Fore.GREEN + "Measurement added successfully.")
                elif x == '2':
                    sub = create_subscription()
                    member.new_subsicribe(sub)
                    print(Fore.GREEN + "Subscription added successfully.")
                elif x == '3':
                    member.display_measurement_history()
                elif x == '4':
                    member.display_subscription_history()
                elif x == '5':
                    break
                else:
                    print(Fore.RED + "Invalid option. Try again.")

    elif choice == '5':
        display_all_tables()
    elif choice == '6':
        change_member_status()

    elif choice == '7':
        print(Fore.GREEN + "Thank You. Stay healthy!")
        break

    else:
        print(Fore.RED + "Invalid choice. Try again.")
