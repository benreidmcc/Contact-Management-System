import sqlite3
db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
cursor = db.cursor()

def print_current():    #function that prints the current table
    cursor.execute("SELECT * FROM contacts")
    for name, phone, email in cursor:
        print(name)
        print(phone)
        print(email)
        print("-" * 20)

def add_entry():        #function that lets you add to a table
    add_name = input("Add name: ")
    while True:
        try:
            add_phone = int(input("Add phone: "))
        except ValueError:
            print ("That is not a valid phone number.")
            continue
        add_email = input("Add email: ")
        db.execute(f"INSERT INTO contacts(name, phone, email) VALUES('{add_name}', '{add_phone}', '{add_email}')")
        print_current()
        break

def select_entry():     #function that lets you select from a table
    selected_entry = input("Type a coloumn, an entry or 'all':")
    if selected_entry == ("all"):
        cursor.execute("SELECT * FROM contacts")    #all
        for name, phone, email in cursor:
            print(name)
            print(phone)
            print(email)
            print("-" * 20)
    elif selected_entry == ("name"):
        cursor.execute(f"SELECT {selected_entry} FROM contacts")    #coloumn
        for name in cursor:
            print(name)
            print("-" * 20)
    elif selected_entry == ("phone"):
        cursor.execute(f"SELECT {selected_entry} FROM contacts")    #coloumn
        for phone in cursor:
            print(phone)
            print("-" * 20)
    elif selected_entry == ("email"):
        cursor.execute(f"SELECT {selected_entry} FROM contacts")    #coloumn
        for email in cursor:
            print(email)
            print("-" * 20)
    else:
        cursor.execute(f"SELECT * FROM contacts WHERE name = '{selected_entry}' OR phone = '{selected_entry}' OR email = '{selected_entry}'") #sqlite3.OperationalError: no such column: betty
        for name, phone, email in cursor:   #entry
            print(name)
            print(phone)
            print(email)
            print("-" * 20)

def update_entry():     #function that lets you update one entry in a table
    current_entry = input("What entry do you want replaced?: ")     
    updated_entry = input("What should it be replaced with?: ")
    db.execute(f"UPDATE contacts SET name = '{updated_entry}' WHERE name = '{current_entry}'") 
    db.execute(f"UPDATE contacts SET phone = '{updated_entry}' WHERE phone = '{current_entry}'") 
    db.execute(f"UPDATE contacts SET email = '{updated_entry}' WHERE email = '{current_entry}'")
    print_current() 
                                    
def delete_entry():     #function that removes entrys from a list
    deleted_entry = input("What entry do you want deleted?: ")      
    db.execute(f"DELETE FROM contacts WHERE name = '{deleted_entry}' OR phone = '{deleted_entry}' OR email = '{deleted_entry}'")
    print_current()

def run_db():           #function that user can use CRUD commands continuously to a table until they decide to end the loop
    while True:
        user_choice = input("Please input from add, select, update, delete or end: ")
        if user_choice == ("add"):
            add_entry()
            continue
        elif user_choice == ("select"):
            select_entry()
        elif user_choice == ("update"):
            update_entry()
            continue
        elif user_choice == ("delete"):
            delete_entry()
            continue
        elif user_choice == ("end"):
            print_current()
            print ("Changes commited.")
            break
        else:
            print ("Invalid choice.")
            continue

run_db()

cursor.close()
db.commit()
db.close()