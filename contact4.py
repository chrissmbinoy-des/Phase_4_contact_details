import json

file = 'contact4.json'

def display_menu() :

    co = load_contacts()
    while True:
        print('MENU')
        print('----')
        print('1.Add contact')
        print('2.View all contacts')
        print('3.Search contact')
        print('4.Delete a contact')
        print('5.Exit') 
        c = int(input('Enter your choice : '))
        if c==1 :
            add_new_contact(co)
        elif c==2 :
            view_all_contacts(co)
        elif c==3:
            search_contact(co)
        elif c==4:
            delete_contact(co)
        elif c==5:
            print("Saving contacts.....")
            save_contacts(co)
            print('Done!')
            break
        else:
            print("Invalid Input")
        

def add_new_contact(co):

    name = input("Enter name: ").strip()
    no = input("Enter phone number: ").strip()
    try:
        no = int(no)
    except:
        print("Invalid input. Please enter a valid phone number.")
        add_new_contact(co)
        return
    email = input("Enter email: ").strip()

    con = {"name": name, "number": no, "email": email}
    co.append(con)

    print("Saved!!")
    

def view_all_contacts(co):
    
    if not co:
        print("No contacts found.")
    else:
        for i, con in enumerate(co, start=1):
            print(f"{i}. Name: {con['name']}")
            print(f"   Phone: {con['number']}")
            print(f"   Email: {con['email']}")
    

def search_contact(co):
 
    name = input("Enter name to search: ").strip().lower()
    found = [c for c in co if name in c['name'].lower()]
 
    if found:
        for con in found:
            print('Found Contact!!')
            print(f"   Name: {con['name']}")
            print(f"   Phone: {con['number']}")
            print(f"   Email: {con['email']}")
    else:
        print("Contact not found.")

def delete_contact(co):
 
    name = input("Enter name to delete: ").strip().lower()
 
    for con in co:
        if con ['name'].lower() == name:
            co.remove(con)
            print("Contact ", con['name'], "deleted successfully.")
            return
    print("Contact not found.")    
    

def save_contacts(co):
    with open(file, "w") as f:
        json.dump(co, f, indent=4)

def load_contacts():
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
if __name__ == "__main__":
    display_menu()