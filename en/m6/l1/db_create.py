# dataset from: https://archive.ics.uci.edu/static/public/352/online+retail.zip

import pandas as pd
import sqlite3

# Read the Excel file
df = pd.read_excel('data/Online Retail.xlsx', engine='openpyxl')

# Pre-process DataFrame
df.dropna(inplace=True)

# Prepare DataFrames for Customers, Products, and Transactions tables
customers_df = df[['CustomerID', 'Country']].drop_duplicates(subset=['CustomerID']).astype({'CustomerID': 'int'}).reset_index(drop=True)
products_df = df[['StockCode', 'Description']].drop_duplicates(subset=['StockCode']).astype({'StockCode': 'str'}).reset_index(drop=True)
transactions_df = df[['InvoiceNo', 'StockCode', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID']].copy()
transactions_df['InvoiceDate'] = transactions_df['InvoiceDate'].astype(str)  

# Create SQLite Database and cursor
conn = sqlite3.connect('ECommerceDB.sqlite')
cursor = conn.cursor()

# Enable foreign key support
cursor.execute("PRAGMA foreign_keys = ON;")

# Create Customers table with a primary key
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY,
    Country TEXT
)
''')

# Create Products table with a primary key
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    StockCode TEXT PRIMARY KEY,
    Description TEXT
)
''')

# Create Transactions table with primary key and foreign keys
cursor.execute('''
CREATE TABLE IF NOT EXISTS Transactions (
    TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
    InvoiceNo TEXT,
    InvoiceDate TEXT,
    Quantity INTEGER,
    UnitPrice REAL,
    StockCode TEXT,
    CustomerID INTEGER,
    FOREIGN KEY (StockCode) REFERENCES Products(StockCode),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
)
''')

# Insert Data into Tables
customers_df.to_sql('Customers', conn, if_exists='append', index=False)
products_df.to_sql('Products', conn, if_exists='append', index=False)
transactions_df.to_sql('Transactions', conn, if_exists='append', index=False, chunksize=200)  # Adjust chunksize as necessary

# Example Query: Verify Data
#print(pd.read_sql_query("SELECT * FROM Customers LIMIT 5;", conn))
#print(pd.read_sql_query("SELECT * FROM Products LIMIT 5;", conn))
print(pd.read_sql_query("SELECT * FROM Transactions LIMIT 5;", conn))

# Close Connection
conn.close()
