import sqlite3
from faker import Faker
import pandas as pd

# Create a Faker generator
fake = Faker()

# Connect to your SQLite database
conn = sqlite3.connect('ECommerceDB.sqlite')
cursor = conn.cursor()

# Add a LastName column to the Customers table
cursor.execute('ALTER TABLE Customers ADD COLUMN LastName TEXT')

# Generate and insert last names for each customer
cursor.execute('SELECT CustomerID FROM Customers')
customer_ids = cursor.fetchall()

for customer_id in customer_ids:
    # Generate a random last name
    last_name = fake.last_name()
    
    # Update the customer row with the new last name
    cursor.execute('UPDATE Customers SET LastName = ? WHERE CustomerID = ?', (last_name, customer_id[0]))

# Commit the changes
conn.commit()

# Close the connection
conn.close()



############################################################
############################################################
# We test if it realy has new data

# Connect to your SQLite database
conn = sqlite3.connect('ECommerceDB.sqlite')

# SQL Query for Top 5 Customers by Total Spend
query_top_customers = """
SELECT 
    T.CustomerID,
    C.Country,
    C.LastName, 
    SUM(T.Quantity * T.UnitPrice) AS TotalSpent
FROM 
    Transactions T
JOIN
    Customers C ON T.CustomerID = C.CustomerID
GROUP BY 
    T.CustomerID
ORDER BY 
    TotalSpent DESC
LIMIT 5;
"""

# Execute the query and fetch results
top_customers = pd.read_sql_query(query_top_customers, conn)

# Display the results
print(top_customers)

# Close the connection
conn.close()
