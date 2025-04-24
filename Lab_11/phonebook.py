


import psycopg2, csv


# db = psycopg2.connect(dbname='lab10', user='postgres', password='12345', host='5432')
db = psycopg2.connect(
    dbname='phonebook',
    user='postgres',
    password='12345',
    host='localhost',  # Или '127.0.0.1'
    port='5432'
)

current=db.cursor()
current.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        person_name VARCHAR(50),
        phone_number VARCHAR(20)
    );
    INSERT INTO phonebook (person_name, phone_number) 
    VALUES
        ('John', '12345678901'),
        ('Jane', '19876543210'),
        ('Mike', '56789012345');

""")


print(''' What do you want?
      "1" if you want to add a new contact or update existing
      "2" if you want to add contacts from .csv file
      "3" if you want to change name or phone of contact
      "0" if you want to see the whole table contacts
      "4" if you want to see first N contacts
      "5" if you want to see all phones of contacts
        
      "6" if you want to change name or phone of contact
      "7" if you want to add many contacts by list
      "8" if you want to see contacts with pagination (LIMIT and OFFSET)
      "9" if you want to delete contact by name or phone''')

req = input("Enter the number ")
if req =='1':
    n = input("Enter name ")
    p = input("Enter phone")
    sql="""
        INSERT INTO phonebook VALUES(%s, %s);
    """
    current.execute(sql,(n, p))

elif req=='2':
    sql="""
        INSERT INTO phonebook VALUES(%s, %s) returning *;
    """
    re = []
    with open ('p_b.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            
            current.execute(sql, row)
            re.append(current.fetchone())
        print(re, "has been added")
elif req=='3':
    w = input("Name or phone")
    if w=='name':
        x = input("Enter new p_n")
        y = input("Enter the new name")
        sql = """
            UPDATE phonebook SET person_name = %s WHERE phone_number = %s;
        """


        current.execute(sql, (y, x))
        print("has been updated")

elif req=='4':
    x = input("Enter the number of contacts")
    sql = """
        SELECT * FROM phonebook;"""
    current.execute(sql)
    re = current.fetchmany(int(x))

    print("has been added")
    for i in range(len(re)):
        print('{0:20}{1:20}'.format(re[i][0], re[i][1]))
elif req == '5':
    sql = """
        SELECT phone_number FROM phonebook
    """
    current.execute(sql)
    results = current.fetchall()
    for i in range(len(results)):
        print(results[i][0])
elif req == '6':
    w = input("Do you want to update name or phone:")
    if w == 'name':
        x = input("Enter the phone_number: ")
        y = input("Enter the new name: ")
        sql = """
            UPDATE phonebook SET person_name = %s WHERE phone_number = %s;
        """
        current.execute(sql, (y, x))
        print("Data has been updated")
    elif w == 'phone':
        x = input("Enter the name: ")
        y = input("Enter the new phone_number: ")
        sql = """
            UPDATE phonebook SET phone_number = %s WHERE person_name = %s;
        """
        current.execute(sql, (y, x))
        print("Data has been updated")
elif req == '7':
#   example of list = [('v', 123), ('xij', 1331), ('hjdh', 222425626)]
    contact = input("Enter the list of contacts:")
    
    cont = []
    for tup in contact.split('), ('):
        tup = tup.replace(')','').replace('(','')
        cont.append(tuple(tup.split(',')))
    print(cont)
    sql="""
        INSERT INTO phonebook VALUES(%s, %s);
    """
    for i in range(len(cont)):
        current.execute(sql, (cont[i][0], cont[i][1]))

elif req == '0':
    sql = """
        SELECT * FROM phonebook
    """
    current.execute(sql)
    results = current.fetchall()
    print('''PHONEBOOK
=========================================
NAME                PHONE
=========================================''')
    for i in range(len(results)):
        print('{0:20}{1:20}'.format(results[i][0], results[i][1]))    
elif req == '8':
    # Pagination function: Get contacts with LIMIT and OFFSET
    page_number = int(input("Enter the page number: "))
    page_size = int(input("Enter the number of contacts per page: "))

    offset = (page_number - 1) * page_size
    sql = """
        SELECT * FROM phonebook LIMIT %s OFFSET %s;
    """
    current.execute(sql, (page_size, offset))
    results = current.fetchall()

    print(f"Displaying page {page_number} with {page_size} contacts per page:")
    if results:
        for record in results:
            print(f'{record[0]:20} {record[1]:20}')
    else:
        print("No records found for this page.")

elif req == '9':
    print("Enter the name or phone:")
    delete = input()
    sql="""
        DELETE FROM phonebook WHERE person_name = %s;
    """
    current.execute(sql, (delete,))
    sql="""
        DELETE FROM phonebook WHERE phone_number = %s;
    """
    current.execute(sql, (delete,))
    print("Contact", delete, "has been deleted")

else:
    print("Request is unidentified")

current.close()
db.commit()
db.close()