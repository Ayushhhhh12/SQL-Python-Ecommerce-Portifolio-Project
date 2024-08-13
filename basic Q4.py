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

#Q4. Calculate the percentage of orders that were paid in installments.

query = """select 
            (sum(case when payment_installments >= 1 then 1 else 0 end))/count(*)*100 
            from payments
  """
cur.execute(query)
data = cur.fetchall()
print(data[0][0])
