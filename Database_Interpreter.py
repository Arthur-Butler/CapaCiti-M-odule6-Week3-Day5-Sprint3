#Importing bar graph utils from pandas
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
#Importing pandas for dataframe
import pandas as pd
#Importing DataFrame from pandas import
from pandas import DataFrame
#Importing mysql.connector to connect to database
import mysql.connector
#Establishin database connection
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1738art",
    database="sprintdb"
)
#Creatin cursor to navigate database
mycursor=mydb.cursor()
#Fetchin columns from database using SQL
mycursor.execute("SELECT `stock`.`ItemAmount` FROM stock")
ItemAmount=mycursor.fetchall()
#Placing data in lists
y=[]
for row in ItemAmount:
    y.extend(row)
print(y)
mycursor.execute("SELECT `stock`.`Items` FROM stock")
Items=mycursor.fetchall()
x=[]
for row in Items:
    x.extend(row)
print(x)    
y_pos=np.arange(7)
#Diplaying data viually using a bar graph
plt.bar(y_pos, y, align='center', alpha=1)
plt.xticks(y_pos, x)
plt.ylabel('Stock Amount')
plt.xlabel('Item Category')
plt.title('Amount of stock for each item in a category')
plt.show()

mycursor.execute("SELECT `chips`.`Stock Amount` FROM chips")
ItemAmount=mycursor.fetchall()
#Placing data in lists
sizes1=[]
for row in ItemAmount:
    sizes1.extend(row)
print(sizes1)
mycursor.execute("SELECT `chips`.`Brand_Name` FROM chips")
Items=mycursor.fetchall()
labels1=[]
for row in Items:
    labels1.extend(row)
print(labels1)    
y_pos=np.arange(len(x1))
#Diplaying data viually using a piechart
colors=['red','blue','green','yellow','purple','pink','orange']
explode=(0,0,0,0,0,0,0)
plt.pie(sizes1, explode=explode, labels=labels1, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

mycursor.execute("SELECT cooldrinks.Stock_Amount FROM cooldrinks")
ItemAmount=mycursor.fetchall()
#Placing data in lists
sizes2=[]
for row in ItemAmount:
    sizes2.extend(row)
print(sizes2)
mycursor.execute("SELECT Brand_Name FROM cooldrinks")
Items=mycursor.fetchall()
labels2=[]
for row in Items:
    labels2.extend(row)
print(labels2)    
y_pos=np.arange(len(x2))
#Diplaying data viually using a piechart
colors=['red','blue','green','yellow','purple','pink','orange']
explode=(0,0,0,0,0,0,0)
plt.pie(sizes2, explode=explode, labels=labels2, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()

mycursor.execute("SELECT chocolates.Stock_Amount FROM chocolates")
ItemAmount=mycursor.fetchall()
#Placing data in lists
sizes3=[]
for row in ItemAmount:
    sizes3.extend(row)
print(sizes3)
mycursor.execute("SELECT Brand_Name FROM chocolates")
Items=mycursor.fetchall()
labels3=[]
for row in Items:
    labels3.extend(row)
print(labels3)    
#Diplaying data viually using a piechart
colors=['red','blue','green','yellow','purple','pink','orange','white']
explode=(0,0,0,0,0,0,0,0)
plt.pie(sizes3, explode=explode, labels=labels3, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()


mycursor.execute("SELECT cupcakes.Stock_Amount FROM cupcakes")
ItemAmount=mycursor.fetchall()
#Placing data in lists
sizes4=[]
for row in ItemAmount:
    sizes4.extend(row)
print(sizes4)
mycursor.execute("SELECT Brand_Name FROM cupcakes")
Items=mycursor.fetchall()
labels4=[]
for row in Items:
    labels4.extend(row)
print(labels4)    
#Diplaying data viually using a piechart
pcolors=['red','blue','green','yellow']
explode=(0,0,0,0)
plt.pie(sizes4, explode=explode, labels=labels4, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

mycursor.execute("SELECT fruit.Stock_Amount FROM fruit")
ItemAmount=mycursor.fetchall()
#Placing data in lists
sizes5=[]
for row in ItemAmount:
    sizes5.extend(row)
print(sizes5)
mycursor.execute("SELECT Brand_Name FROM fruit")
Items=mycursor.fetchall()
labels5=[]
for row in Items:
    labels5.extend(row)
print(labels5)    
#Diplaying data viually using a piechart
colors=['red','blue','green','yellow','purple','pink','orange','white']
explode=(0,0,0,0,0,0,0,0)
plt.pie(sizes5, explode=explode, labels=labels5, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

mycursor.execute("SELECT pies.Stock_Amount FROM pies")
ItemAmount=mycursor.fetchall()
#Placing data in lists
sizes6=[]
for row in ItemAmount:
    sizes6.extend(row)
print(sizes6)
mycursor.execute("SELECT Brand_Name FROM pies")
Items=mycursor.fetchall()
labels6=[]
for row in Items:
    labels6.extend(row)
print(labels6)    
#Diplaying data viually using a piechart
colors=['red','blue','green','yellow','purple','pink','orange']
explode=(0,0,0,0,0,0,0)
plt.pie(sizes6, explode=explode, labels=labels6, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

mycursor.execute("SELECT veggies.Stock_Amount FROM veggies")
ItemAmount=mycursor.fetchall()
#Placing data in lists
sizes7=[]
for row in ItemAmount:
    sizes7.extend(row)
print(sizes7)
mycursor.execute("SELECT Brand_Name FROM veggies")
Items=mycursor.fetchall()
labels7=[]
for row in Items:
    labels7.extend(row)
print(labels7)    
#Diplaying data viually using a piechart
colors=['red','blue','green','yellow','purple']
explode=(0,0,0,0,0)
plt.pie(sizes7, explode=explode, labels=labels7, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
