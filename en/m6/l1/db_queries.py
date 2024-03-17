import sqlite3
import pandas as pd



############################################################
############################################################
# 1. We want to know, what was the revenu per country on a specific day. 
# Connect to your SQLite database
conn = sqlite3.connect('ECommerceDB.sqlite')

# SQL Query
query = """
SELECT 
    Customers.Country,
    SUM(Transactions.Quantity * Transactions.UnitPrice) AS TotalSales
FROM 
    Transactions
JOIN 
    Customers ON Transactions.CustomerID = Customers.CustomerID
WHERE 
    Transactions.InvoiceDate LIKE '2010-12-01%'
GROUP BY 
    Customers.Country
ORDER BY 
    TotalSales DESC;
"""

# Execute the query and fetch results
results = pd.read_sql_query(query, conn)

# Display the results
print(results)

# Close the connection
conn.close()

############################################################
############################################################
# 2. Top 5 Customers by Total Spend

# Connect to your SQLite database
conn = sqlite3.connect('ECommerceDB.sqlite')

# SQL Query for Top 5 Customers by Total Spend
query_top_customers = """
SELECT 
    T.CustomerID,
    C.Country, 
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


############################################################
############################################################
# 3. Top 5 Selling Products by Quantity

# Connect to your SQLite database
conn = sqlite3.connect('ECommerceDB.sqlite')

# SQL Query for Top 5 Selling Products by Quantity
query_top_products_quantity = """
SELECT 
    T.StockCode,
    P.Description,
    SUM(T.Quantity) AS TotalQuantitySold
FROM 
    Transactions T
JOIN
    Products P ON T.StockCode = P.StockCode
GROUP BY 
    T.StockCode
ORDER BY 
    TotalQuantitySold DESC
LIMIT 5;
"""

# Execute the query and fetch results
top_products_quantity = pd.read_sql_query(query_top_products_quantity, conn)

# Display the results
print(top_products_quantity)

# Close the connection
conn.close()



############################################################
############################################################
# 4. Top 5 Selling Products by Revenue

# Connect to your SQLite database
conn = sqlite3.connect('ECommerceDB.sqlite')

# SQL Query for Top 5 Selling Products by Revenue
query_top_products_revenue = """
SELECT 
    T.StockCode,
    P.Description,
    SUM(T.Quantity * T.UnitPrice) AS TotalRevenue
FROM 
    Transactions T
JOIN
    Products P ON T.StockCode = P.StockCode
GROUP BY 
    T.StockCode
ORDER BY 
    TotalRevenue DESC
LIMIT 5;
"""

# Execute the query and fetch results
top_products_revenue = pd.read_sql_query(query_top_products_revenue, conn)

# Display the results
print(top_products_revenue)

# Close the connection
conn.close()


############################################################
############################################################
# 5. Top Selling Product by Revenue by Country

# Connect to your SQLite database
conn = sqlite3.connect('ECommerceDB.sqlite')

# SQL Query for Top 3 Selling Products by Revenue by Country
query_top_1_product_by_country = """
WITH RankedProducts AS (
    SELECT
        C.Country,
        T.StockCode,
        P.Description,
        SUM(T.Quantity * T.UnitPrice) AS TotalRevenue,
        RANK() OVER (
            PARTITION BY C.Country
            ORDER BY SUM(T.Quantity * T.UnitPrice) DESC
        ) AS RevenueRank
    FROM
        Transactions T
    JOIN Customers C ON T.CustomerID = C.CustomerID
    JOIN Products P ON T.StockCode = P.StockCode
    GROUP BY
        C.Country, T.StockCode
)
SELECT
    Country,
    StockCode,
    Description,
    TotalRevenue
FROM
    RankedProducts
WHERE
    RevenueRank <= 1
ORDER BY
    Country, TotalRevenue DESC;
"""

# Execute the query and fetch results
top_1_product_by_country = pd.read_sql_query(query_top_1_product_by_country, conn)

# Display the results
print(top_1_product_by_country)

# Close the connection
conn.close()



########################################################
########################################################
# 6. How the price changed over time for specific StockCode?

# Connect to your SQLite database
conn = sqlite3.connect('ECommerceDB.sqlite')

# SQL Query for fetching unique prices for a product and the first occurrence date
query_unique_price_first_date = """
SELECT DISTINCT
    UnitPrice,
    FIRST_VALUE(InvoiceDate) OVER (PARTITION BY UnitPrice ORDER BY InvoiceDate) AS FirstOccurrenceDate
FROM 
    Transactions
WHERE 
    StockCode = '85123A'
GROUP BY 
    UnitPrice
ORDER BY 
    FirstOccurrenceDate;
"""

# Execute the query and fetch results
unique_price_first_date = pd.read_sql_query(query_unique_price_first_date, conn)

# Display the results
print(unique_price_first_date)

# Close the connection
conn.close()