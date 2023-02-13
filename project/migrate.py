import sqlite3


conn=sqlite3.connect('tienda.db')
cursor_obj = conn.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS ORDENES")
table = """ CREATE TABLE ORDENES (
            ORDER_ID    INT,
            PRICE_TOTAL INT,
        	PRODUCT_ID  INT,
            NAME        VARCHAR(50),
            NROSERIE	VARCHAR(50),
            CANTIDAD	INT,
            PRODUCT	    VARCHAR(50),
            PRICE_UNIT	INT,
            CATEGORIA	VARCHAR(50),
            STOCK_ACUTAL INT,
            DATE	    DATETIME,
            USER_ADMIN	VARCHAR(50),
            USER_CLIENT VARCHAR(50)
        ); """
cursor_obj.execute(table)


conn.commit()
conn.close()
print('CREACION CULMINADA')

