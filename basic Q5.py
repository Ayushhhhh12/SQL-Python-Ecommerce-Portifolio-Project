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

#Q5. Count the number of customers from each state. 

query = """ select customer_state customers,count(customer_id) customer_count
 from customers group by  customer_state    
  """
cur.execute(query)
data = cur.fetchall()
df = pd.DataFrame(data,columns=["customer" ,"customer_count"])
df = df.sort_values(by= "customer_count",ascending=False)
print(df)
plt.bar(df["customer"],df["customer_count"])
plt.xticks(rotation = 90)
plt.xlabel("customer")
plt.ylabel("customer_count")
plt.title("count of customer")
plt.show()
