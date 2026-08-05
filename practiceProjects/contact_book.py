contact = {}

def add_contact():
    name = input("enter a name: ").lower()
    if name in contact:
        print("already exist")
    else:    
        number = input("enter a number")
        contact[name] = number
        print("added!")
        
    number = input("enter a number: ")
    


def search_contact():
    name = input("enter name to search: ")
    if name in contact:
        print(f"{name} : {contact[name]}")
    else:
        print("contact not found")
    

def delete_contact():
    name = input("enter name to delete: ")
    if name in contact:
        del contact[name]
        print("contact deleted")
    else:
        print("contact not found")

while True:
    command = input("enter add/serach/delete/show: ").lower()

    if command == "add":
        add_contact()
    elif command == "search":
        search_contact()
    elif command == "delete":
        delete_contact()
    elif command == "show":
        if len(contact) == 0:
            print("no contacts!")
        else:
            for name, number in contact.items():
                print(f"{name} : {number}")

    elif command == "exit":
        print("bye")
        break
    else:
        print("invalid input!")

   

