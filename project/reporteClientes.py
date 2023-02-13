import sqlite3
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
 
conn=sqlite3.connect('tienda.db')
cursor_obj = conn.cursor()
 
 
def read_from_db():
 
  cursor_obj.execute('SELECT * FROM ORDENES')
  data = cursor_obj.fetchall()
  print(data)
  for row in data:
    print(row)
 
 

 
def graf_data():
  cursor_obj.execute('SELECT USER_CLIENT, SUM(PRICE_TOTAL) FROM ORDENES GROUP BY USER_CLIENT ORDER BY USER_CLIENT ASC')
  data = cursor_obj.fetchall()
 
  cliente = []
  ventas = []
 
  for row in data:
    cliente.append(row[0])
    ventas.append(row[1])
  print(data)
  ax=plt.subplot()
  ax.bar(cliente,ventas)
  plt.show()
 
graf_data()
cursor_obj.close
conn.close()  