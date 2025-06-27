from matplotlib import pyplot as plt
from measurement import Measurement
from member import Member
from subscription import Subscription
from colorama import Fore, Style, init
from datetime import datetime
from tabulate import tabulate

init(autoreset=True)

gym_members = dict()

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

while True:
    menu = Fore.CYAN + '''
------------------------------------
------- Gym Member System ----------
------------------------------------
1- Add new gym member
2- Display all members
3- Delete a member
4- Search for a member
5- Add subscription to a member
6- Add body measurement
7- Display all subscriptions
8- Display all measurements
9- Exit
------------------------------------
'''
    choice = input(menu + Fore.YELLOW + "\nChoose an option: ").strip()

    if choice == '1':
        add_member()

    elif choice == '2':
        if not gym_members:
            print(Fore.RED + "No members found.")
        else:
            # for member in gym_members.values():
            #     member.display()
            print(Fore.CYAN + "\n\n--- All Members ---\n")
            
            headers = ["ID", "Name", "Birth Date", "Age", "Username", "Password", "Status"]
            
            table = [m.to_list() for m in gym_members.values()]
            
            print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
            
    elif choice == '3':
        delete_id = input("Enter the member ID to delete: ").strip()
        if delete_member(delete_id):
            print(Fore.GREEN + "Deleted Successfully!")
        else:
            print(Fore.RED + "Not found. Try Again!")

    elif choice == '4':
        search_id = input("Enter the member ID to search: ").strip()
        member = search_member(search_id)
        if member is None:
            print(Fore.RED + "Not found.")
        else:
            print(Fore.CYAN + "--- Member Found ---")
            member.display()

    elif choice == '5':
        print(Fore.YELLOW + "Feature not implemented yet.")
    elif choice == '6':
        print(Fore.YELLOW + "Feature not implemented yet.")
    elif choice == '7':
        print(Fore.YELLOW + "Feature not implemented yet.")
    elif choice == '8':
        member_id = input("Enter member ID to plot BMI history: ").strip()
        member = search_member(member_id)

        if member is None:
            print(Fore.RED + "Member not found.")
        else:
            measurements = member.get_measurement()
            if not measurements:
                print(Fore.RED + "No measurements found for this member.")
            else:
                dates = [m.get_date() for m in measurements]
                bmis = [m.get_bmi() for m in measurements]

                plt.clear_data()
                plt.plot(dates, bmis, marker='dot')
                plt.title(f"{member.get_name()}'s BMI Progress")
                plt.xlabel("Date")
                plt.ylabel("BMI")
                plt.show()
    elif choice == '9':
        print(Fore.GREEN + "Thank You. Stay healthy!")
        break
    else:
        print(Fore.RED + "Invalid choice. Try again.")
