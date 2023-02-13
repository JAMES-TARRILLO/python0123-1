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
  cursor_obj.execute('SELECT USER_ADMIN, SUM(PRICE_TOTAL) FROM ORDENES GROUP BY USER_ADMIN ORDER BY USER_ADMIN ASC')
  data = cursor_obj.fetchall()
 
  vendedor = []
  ventas = []
 
  for row in data:
    vendedor.append(row[0])
    ventas.append(row[1])
  print(data)

  ax=plt.subplot()
  ax.bar(vendedor,ventas,facecolor='r')
  plt.show()
 
graf_data()
cursor_obj.close
conn.close()    