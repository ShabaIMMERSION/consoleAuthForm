import sqlite3 as sql3

db = sql3.connect('users.db')

cursor = db.cursor()

print('Hello! My name is AuthShabby and I will help you with registration.')
op = input('Input number of operation. \n'
           '1. - Registration\n'
           '2. - Show data your private data\n'
           'Input here <<< ')

if op == '1' or op == '1.':
    print('OK. Lets begin.')
    username = input('Input your username firstly <<< ')
    email = input('Input your email <<< ')
    password = input('Input your password <<< ')
    cursor.execute(f'''INSERT INTO usersTable(Username, UserEmail, UserPassword) VALUES (
        '{username}',
        '{email}',
        '{password}'
    )''')

elif op == '2' or op == '2.':
    print('OK. Lets begin.')
    username = input('Please, input your username <<< ')
    cursor.execute(f'''SELECT * FROM usersTable WHERE Username = '{username}' ''')
    data = cursor.fetchall()
    print(f"ID: {data[0][0]}")
    print(f"Username: {data[0][1]}")
    print(f"User e-mail: {data[0][2]}")
    print(f"User password: {data[0][3]}")

db.commit()
