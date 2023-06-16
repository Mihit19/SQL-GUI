import mysql.connector
from tkinter import *
from prettytable import PrettyTable

# Function to execute a SQL query
def execute_query(query):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database=database_name.get()
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute the query
        cursor.execute(query)

        # Commit the changes if the query modifies data
        if query.strip().split()[0].upper() in ['INSERT', 'UPDATE', 'DELETE']:
            connection.commit()

        # Fetch all the rows from the result set
        rows = cursor.fetchall()

        # Get the column names
        columns = [desc[0] for desc in cursor.description]

        # Create a PrettyTable instance
        table = PrettyTable(columns)

        # Add rows to the table
        for row in rows:
            table.add_row(row)

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return str(table)

    except mysql.connector.Error as error:
        return str(error)


# Function to execute a CREATE DATABASE query
def create_database():
    # Get the database name from the entry box
    db_name = create_db_entry.get()

    # Construct the CREATE DATABASE query
    query = f'CREATE DATABASE {db_name}'

    # Execute the query
    result = execute_query(query)

    # Update the result text box
    result_text.delete(1.0, END)
    result_text.insert(END, result)


# Function to execute a CREATE TABLE query
def create_table():
    # Get the table name and schema from the entry boxes
    table_name = create_table_entry.get()
    schema = create_table_schema.get(1.0, END).strip()

    # Construct the CREATE TABLE query
    query = f'CREATE TABLE {table_name} ({schema})'

    # Execute the query
    result = execute_query(query)

    # Update the result text box
    result_text.delete(1.0, END)
    result_text.insert(END, result)


# Function to execute an INSERT INTO query
def insert_data():
    # Get the table name and data from the entry boxes
    table_name = insert_table_entry.get()
    data = insert_data_entry.get()

    # Construct the INSERT INTO query
    query = f'INSERT INTO {table_name} VALUES ({data})'

    # Execute the query
    result = execute_query(query)

    # Update the result text box
    result_text.delete(1.0, END)
    result_text.insert(END, result)


# Function to execute a general query
def execute_general_query():
    # Get the query from the entry box
    query = general_query_entry.get()

    # Execute the query
    result = execute_query(query)

    # Update the result text box
    result_text.delete(1.0, END)
    result_text.insert(END, result)


# Create the GUI window
window = Tk()
window.title('SQL GUI')

# Set the color scheme
window.configure(bg='#dc484c')

# Frames
select_db_frame = LabelFrame(window, text='Select Database', bg='#8B2323')
select_db_frame.pack(padx=10, pady=10, ipadx=10, ipady=10)

create_db_frame = LabelFrame(window, text='Create Database', bg='#8B2323')
create_db_frame.pack(padx=10, pady=10, ipadx=10, ipady=10)

create_table_frame = LabelFrame(window, text='Create Table', bg='#8B2323')
create_table_frame.pack(padx=10, pady=10, ipadx=10, ipady=10)

insert_data_frame = LabelFrame(window, text='Insert Data', bg='#8B2323')
insert_data_frame.pack(padx=10, pady=10, ipadx=10, ipady=10)

general_query_frame = LabelFrame(window, text='Execute General Query', bg='#8B2323')
general_query_frame.pack(padx=10, pady=10, ipadx=10, ipady=10)

result_frame = LabelFrame(window, text='Result', bg='#8B2323')
result_frame.pack(padx=10, pady=10, ipadx=10, ipady=10)

# Labels and Entry Boxes
select_db_label = Label(select_db_frame, text='Database Name:', bg='#8B2323')
select_db_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

database_name = Entry(select_db_frame, width=30)
database_name.grid(row=0, column=1, padx=5, pady=5, sticky=W)

create_db_label = Label(create_db_frame, text='Database Name:', bg='#8B2323')
create_db_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

create_db_entry = Entry(create_db_frame, width=30)
create_db_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

create_table_label = Label(create_table_frame, text='Table Name:', bg='#8B2323')
create_table_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

create_table_entry = Entry(create_table_frame, width=30)
create_table_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

create_table_schema = Text(create_table_frame, width=40, height=6)
create_table_schema.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

insert_table_label = Label(insert_data_frame, text='Table Name:', bg='#8B2323')
insert_table_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

insert_table_entry = Entry(insert_data_frame, width=30)
insert_table_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

insert_data_label = Label(insert_data_frame, text='Data (comma-separated):', bg='#8B2323')
insert_data_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

insert_data_entry = Entry(insert_data_frame, width=30)
insert_data_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

general_query_label = Label(general_query_frame, text='Enter Query:', bg='#8B2323')
general_query_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

general_query_entry = Entry(general_query_frame, width=50)
general_query_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

# Buttons
create_db_button = Button(create_db_frame, text='Create Database', command=create_database)
create_db_button.grid(row=0, column=2, padx=5, pady=5)

create_table_button = Button(create_table_frame, text='Create Table', command=create_table)
create_table_button.grid(row=2, column=0, padx=5, pady=5)

insert_data_button = Button(insert_data_frame, text='Insert Data', command=insert_data)
insert_data_button.grid(row=2, column=0, padx=5, pady=5)

general_query_button = Button(general_query_frame, text='Execute', command=execute_general_query)
general_query_button.grid(row=0, column=2, padx=5, pady=5)

# Result Text Box
result_text = Text(result_frame, width=60, height=10)
result_text.pack(padx=10, pady=10)

# Set the color for the result text box
result_text.configure(bg='white', fg='black')

window.mainloop()
