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

#Q1  Calculate the number of orders per month in 2018.

query = """ select  monthname(order_purchase_timestamp) months,count(order_id) order_count
from orders where year(order_purchase_timestamp) = 2018
group by months

  """
cur.execute(query)
data = cur.fetchall()
df = pd.DataFrame(data,columns=["months" ,"order_count"])
o = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October"]
ax = sns.barplot(x = df["months"], y = df["order_count"],data=df,order=o)
plt.xticks(rotation = 45)
ax.bar_label(ax.containers[0])
plt.show()


# df = df.sort_values(by= "acc",ascending    =False)
