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

#Q2  2. Find the average number of products per order, grouped by customer city.

query = """ 
        with count_per_order as 
(select orders.order_id, orders.customer_id, count(order_items.order_id) as oc
from orders join order_items
on orders.order_id = order_items.order_id
group by orders.order_id, orders.customer_id)

select customers.customer_city, round(avg(count_per_order.oc),2) average_orders
from customers join count_per_order
on customers.customer_id = count_per_order.customer_id
group by customers.customer_city order by average_orders desc
  """
cur.execute(query)
data = cur.fetchall()
df = pd.DataFrame(data,columns=["customer_city","average_orders"])
df.head(10)
print(df)
# o = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October"]
# ax = sns.barplot(x = df["months"], y = df["order_count"],data=df,order=o)
# plt.xticks(rotation = 45)
# ax.bar_label(ax.containers[0])
# plt.show()