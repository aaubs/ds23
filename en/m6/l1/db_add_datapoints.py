import sqlite3
import pandas as pd

# Transactions data to add
new_transactions = [
    ('936376', '85123A', 8, '2023-12-02 10:30:00', 2.55, 17850),
    ('936377', '71053', 4, '2023-12-02 10:30:00', 3.39, 17850),
    ('936378', '84406B', 6, '2023-12-03 12:05:00', 2.75, 17850),
    ('936379', '84029G', 8, '2023-12-03 12:05:00', 3.39, 17850),
    ('936380', '22752', 3, '2023-12-04 09:00:00', 7.65, 17850),
]

# Connect to the SQLite database
conn = sqlite3.connect('ECommerceDB.sqlite')
cursor = conn.cursor()

# Prepare the SQL insert statement
insert_sql = '''
INSERT INTO Transactions (InvoiceNo, StockCode, Quantity, InvoiceDate, UnitPrice, CustomerID)
VALUES (?, ?, ?, ?, ?, ?)
'''

# Insert each new transaction
for transaction in new_transactions:
    cursor.execute(insert_sql, transaction)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("New transactions added successfully.")



#######################################################
#######################################################
# We print last few transactions by date to see if data were added correctly.

# Connect to your SQLite database
conn = sqlite3.connect('ECommerceDB.sqlite')

# SQL Query for Top 5 Selling Products by Quantity
query_last_transactions = """
SELECT 
    T.*
FROM 
    Transactions T
ORDER BY 
    T.InvoiceDate DESC
LIMIT 5;
"""

# Execute the query and fetch results
top_products_quantity = pd.read_sql_query(query_last_transactions, conn)

# Display the results
print(top_products_quantity)

# Close the connection
conn.close()
