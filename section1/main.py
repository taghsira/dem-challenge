import pandas as pd
import psycopg2
from psycopg2 import Error
from configparser import ConfigParser

# Read the database connection parameters from the config file
config = ConfigParser()
config.read('config.ini')
host = config['database']['host']
port = config['database']['port']
database = config['database']['database']
user = config['database']['user']
password = config['database']['password']

# Define the file path and sheet name of the Excel file
file_path = 'DEM_Challenge_Section1_DATASET.xlsx'
sheet_name = 'DATA'

# Load the provided Excel file into a pandas DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Transform the data by concatenating the first_name and last_name columns into a new column named full_name
df['full_name'] = df['first_name'] + ' ' + df['last_name']
cols = list(df.columns.values)

# Drop the original first_name and last_name columns
df.drop(['first_name', 'last_name'], axis=1, inplace=True)


print(df)

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    # Create a cursor object
    cur = conn.cursor()

    # Create the target table if it doesn't already exist
    cur.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INT PRIMARY KEY,
                full_name TEXT,
                email TEXT,
                gender TEXT,
                ip_address TEXT
            );
        ''')
    conn.commit()

    # Load the transformed data into the target table
    for _, row in df.iterrows():
        cur.execute('''
                INSERT INTO customers (id, full_name, email, gender, ip_address)
                VALUES (%s, %s, %s, %s, %s)
            ''', (row['id'], row['full_name'], row['email'], row['gender'], row['ip_address']))
    conn.commit()

    # Close the cursor and database connection
    cur.close()
    conn.close()

    print('Data loaded successfully!')

except (Exception, Error) as e:
    print('Error:', e)