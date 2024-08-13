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

#Q3. Find the total sales per category.

query = """ select p.product_category ,
 round(sum(pay.payment_value),2) sales
from products p
         join order_items o
         on p.product_id = o.product_id
         join payments pay
         on pay.order_id = o.order_id
         group by p.product_category
         """
cur.execute(query)
data = cur.fetchall()
df = pd.DataFrame(data,columns=[ 'p.product_category',"pay.payment_value " ])
print(df)