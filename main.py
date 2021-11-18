import sqlite3

try:
    connection = sqlite3.connect('C:/Users/aceth/Desktop/App.db') # Path to the database file to edit.

    AddQuery = '''Code to add shit''' # insert code here in the morning

    UpdateQuery = '''Code to Update Shit''' # insert code here in the morning

    DeleteQuery = '''Code to Delete Shit ''' # insert code here in the morning

    connect_cursor = connection.cursor()

    connect_cursor.execute(AddQuery)
    connect_cursor.execute(UpdateQuery)
    connect_cursor.execute(DeleteQuery)

    connection.commit()

    print("Updated the Data within the .db file")

    connect_cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if connection:
        connection.close()
        print("sqlite connection is closed")