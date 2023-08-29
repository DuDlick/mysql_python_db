from config import host, user, password, db_name
import pymysql

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

    print('Connection success')
    print('#' * 20)

    try:
        with connection.cursor() as cursor:
            show_tables = "SHOW TABLES LIKE 'users';"
            cursor.execute(show_tables)
            table_exists = cursor.fetchone()

        if not table_exists:
            with connection.cursor() as cursor:
                create_table = ("CREATE TABLE `users`"
                                "(id int AUTO_INCREMENT,"
                                "name varchar(100),"
                                "password varchar(255),"
                                "phone_number varchar(25),"
                                "email varchar(255),"
                                "PRIMARY KEY (id));")
                cursor.execute(create_table)
                print("Table is created")
        else:
            print('Table already exists')
            print('#' * 20)


        with connection.cursor() as cursor:
            def add_value():
                while True:
                    names = input('Read name: ')
                    passwords = input('Read password: ')
                    phone = input('Read phone number: ')
                    emails = input('Read email address: ')

                    insert_query = "INSERT INTO `users` (name, password, phone_number, email) VALUES (%s, %s, %s, %s);"
                    cursor.execute(insert_query, (names, passwords, phone, emails))
                    connection.commit()
                    finish_text = "*Entered values saved*"
                    print(f"{finish_text}")

            add_value()


    finally:
        cursor.close()
        connection.close()

except Exception as ex:
    print("connection unavailable")
    print(ex)
