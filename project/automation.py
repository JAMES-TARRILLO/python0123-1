import sqlite3
conn=sqlite3.connect('tienda.db')
cursor_obj = conn.cursor()

with open('project\dataTienda.csv','r') as file:
    grabar=0
    for fila in file:
        cursor_obj.execute('INSERT INTO ORDENES VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', fila.split(";"))
        conn.commit()
        grabar+=1
conn.close()

print("INSERCION FINALIZADA")

