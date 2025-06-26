
gym_members = []


def add_member():
    name = input("Enter member name: ")
    member = {
        'name': name,
        'membership_status': "Active"
    }
    gym_members.append(member)

    file = open("gym_members.txt", "a", encoding="utf-8")
    file.write(name + "\n")
    file.close()

    
def display_members():
    for index, member in enumerate(gym_members, start=1):
        print(f"{index} - {member['name']} ({member['membership_status']})")

    with open("gym_members.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print("\nAll Gym Members:\n" + content)

def delete_member():
    delete_member = input("write the member number to delete : ") 
    if delete_member.isdigit():
        delete_member = int(delete_member)
        for index, item in enumerate(gym_members, start=1): 
            if index == delete_member:
                gym_members.pop(index - 1)
                print(f"Member: {item['name']} deleted !")

                file = open("gym_members.txt", "w", encoding="utf-8")
                for member in gym_members:
                    file.write(member['name'] + " - Active\n")
                file.close()

                return
    else:
        print("Invalid input")
        return
    print("member not found! try again!")

def search_member():
    search_name = input("Enter the member name to search: ")
    for member in gym_members:
        if member['name'].lower() == search_name.lower():
            print(f"Member found: {member['name']} ({member['membership_status']})")
            return
    print("Member not found. Try again!")
while True:
    menu = '''
    1- Add new gym member.
    2- Display all members.
    3- Remove a member.
    4- Search for a member.
    5- Exit.
    '''
    choice = input(menu + "\nChoose an option: ")

    if choice == '1':
        add_member()
    elif choice == '2':
        display_members()
    elif choice == '3':
        delete_member()
    elif choice == '4':
        search_member()
    elif choice == '5':
        print("Goodbye! Stay healthy 💪")
        break
    else:
        print("Invalid choice, please try again.")
    