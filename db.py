import sqlite3

# Function to initialize the database
def initialize_database():
    # Connect to the database file or create if not exists
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()

    # Create the BMI data table if it doesn't already exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS bmi_data (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            height REAL NOT NULL,
            weight REAL NOT NULL,
            bmi REAL NOT NULL,
            category TEXT NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Function to insert BMI data into the database
def insert_data(name, height, weight, bmi, category):
    # Connect to the database
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()

    # Insert data into the BMI data table
    c.execute('''
        INSERT INTO bmi_data (name, height, weight, bmi, category)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, height, weight, bmi, category))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Function to retrieve historical BMI data from the database
def get_history():
    # Connect to the database
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()

    # Retrieve all rows from the BMI data table
    c.execute('SELECT * FROM bmi_data')
    rows = c.fetchall()

    # Close the connection and return the retrieved rows
    conn.close()
    return rows
