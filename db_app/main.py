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
                                "email varchar(255),"
                                "PRIMARY KEY (id));")
                cursor.execute(create_table)
                print("Table is created")
        else:
            print('Table already exists')
            print('#' * 20)

        with connection.cursor() as cursor:
            names = input('Read name: ')
            passwords = (input('Read password: '))
            emails = input('Read email address: ')

            insert_query = "INSERT INTO `users` (name, password, email) VALUES (%s, %s, %s);"
            cursor.execute(insert_query, (names, passwords, emails))
            connection.commit()
            print('Entered values saved')

    finally:
        cursor.close()
        connection.close()

except Exception as ex:
    print("connection unavailable")
    print(ex)
