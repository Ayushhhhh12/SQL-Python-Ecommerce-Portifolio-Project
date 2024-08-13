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

#Q1.Calculate the moving average of order values for each customer over their order history.

query = """ select customer_id, order_purchase_timestamp, payment,
avg(payment) over(partition by customer_id order by order_purchase_timestamp
rows between 2 preceding and current row) as mov_avg
from
(select orders.customer_id, orders.order_purchase_timestamp, 
payments.payment_value as payment
from payments join orders
on payments.order_id = orders.order_id) as a   
  """
cur.execute(query)
data = cur.fetchall()
df = pd.DataFrame(data)
print(df.head())