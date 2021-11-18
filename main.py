import sqlite3

try:
    connection = sqlite3.connect('C:/Users/aceth/Desktop/App.db') # Path to the database file to edit.

    #AddQuery = '''INSERT INTO Users (Username, Email, Pass, Birthday, createdDateTime)
    #      VALUES ('acethegenie', 'SomeEmail@something.com', 'RanDomPasSW0RD1234!', '1999-02-16', '');'''

    #UpdateQuery = '''Update Users set createdDateTime = '2021-11-18'
    #                WHERE Username = 'acethegenie';''' # insert code here in the morning

    #DeleteQuery = '''DELETE from Users
    #                    where Username = 'ironspider';''' # insert code here in the morning

    #SelectQuery = '''SELECT * FROM Users'''

    connect_cursor = connection.cursor()

    buffer = ""

    while True:
        line = input("Input an SQL Command: ")
        if line == "":
            break
        buffer += line
        try:
            connect_cursor.execute(buffer)
            connection.commit()

            if buffer.startswith("SELECT"):
                connect_cursor.execute(buffer)
                for row in connect_cursor.fetchall():
                    print(row)
        except sqlite3.Error as e:
            print("An error occurred: ", e.args[0])
        buffer = ""

    print("Updated the Data within the .db file")

    connect_cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if connection:
        connection.close()
        print("sqlite connection is closed")