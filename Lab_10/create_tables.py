import psycopg2, csv

db = psycopg2.connect(
    dbname='lab10',
    user='postgres',
    password='12345',
    host='localhost',
    port='5432'
)

cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        person_name VARCHAR(50),
        phone_number VARCHAR(20) UNIQUE
    );
""")

print(''' What do you want?
"1" - Add new contact or update existing
"2" - Add contacts from .csv file
"3" - Change name or phone of a contact
"0" - Show all contacts
"4" - Show first N contacts
"5" - Delete a contact
''')

req = input("Enter the number: ")

if req == '1':
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cursor.execute("""
        INSERT INTO phonebook (person_name, phone_number)
        VALUES (%s, %s)
        ON CONFLICT (phone_number)
        DO UPDATE SET person_name = EXCLUDED.person_name;
    """, (name, phone))
    print("Contact added or updated.")

elif req == '2':
    results = []
    with open('p_b.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            cursor.execute("""
                INSERT INTO phonebook (person_name, phone_number)
                VALUES (%s, %s)
                ON CONFLICT (phone_number)
                DO UPDATE SET person_name = EXCLUDED.person_name
                RETURNING *;
            """, row)
            results.append(cursor.fetchone())
    print("Contacts added or updated:", results)

elif req == '3':
    what = input("Update by 'name' or 'phone': ").strip().lower()
    if what == 'name':
        phone = input("Enter phone number: ")
        new_name = input("Enter new name: ")
        cursor.execute("""
            UPDATE phonebook SET person_name = %s WHERE phone_number = %s;
        """, (new_name, phone))
    elif what == 'phone':
        name = input("Enter contact name: ")
        new_phone = input("Enter new phone number: ")
        cursor.execute("""
            UPDATE phonebook SET phone_number = %s WHERE person_name = %s;
        """, (new_phone, name))
    print("Contact updated.")

elif req == '4':
    n = int(input("Enter the number of contacts: "))
    cursor.execute("SELECT * FROM phonebook LIMIT %s;", (n,))
    results = cursor.fetchall()
    print("\nFirst", n, "contacts:")
    for name, phone in results:
        print(f"{name:20}{phone:20}")

elif req == '0':
    cursor.execute("SELECT * FROM phonebook;")
    results = cursor.fetchall()
    print("\nPHONEBOOK\n" + "="*40)
    print(f"{'NAME':20}{'PHONE':20}")
    print("="*40)
    for name, phone in results:
        print(f"{name:20}{phone:20}")

elif req == '5':
    method = input("Delete by 'name' or 'phone': ").strip().lower()

    if method == 'name':
        name = input("Enter the name of the contact to delete: ")
        cursor.execute("SELECT * FROM phonebook WHERE person_name = %s;", (name,))
        contact = cursor.fetchone()
        if contact:
            cursor.execute("DELETE FROM phonebook WHERE person_name = %s;", (name,))
            print("Contact deleted.")
        else:
            print("No contact found with that name.")

    elif method == 'phone':
        phone = input("Enter the phone number of the contact to delete: ")
        cursor.execute("SELECT * FROM phonebook WHERE phone_number = %s;", (phone,))
        contact = cursor.fetchone()
        if contact:
            cursor.execute("DELETE FROM phonebook WHERE phone_number = %s;", (phone,))
            print("Contact deleted.")
        else:
            print("No contact found with that phone number.")

    else:
        print("Invalid input. Please enter 'name' or 'phone'.")

else:
    print("Unknown request.")

cursor.close()
db.commit()
db.close()
