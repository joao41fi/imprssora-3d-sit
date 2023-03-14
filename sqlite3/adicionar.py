import sqlite3
con = sqlite3.connect("sqlite3/tutorial.db")
cur = con.cursor()


data = ['treceiro', 2005, 'stl']
cur.execute("INSERT INTO lista_impre VALUES(?,?,?)",data)
con.commit()

# pode se tranformar em um fucão para ir a dicionado a lista 