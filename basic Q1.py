import pandas as pd
import mysql.connector
import os
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ayush#12345',
    database='ecommerce'
)
cur = db.cursor()

# Q1. List all unique cities where customers are located

# query = """ select distinct customer_city from customers """
# cur.execute(query)
# data = cur.fetchall()
# print(data)

# Q2 Count the number of orders placed in 2017.

query = """ select count(order_id) FROM orders where year(order_purchase_timestamp) = 2017 """
cur.execute(query)
data = cur.fetchall()
print(data[0][0])
