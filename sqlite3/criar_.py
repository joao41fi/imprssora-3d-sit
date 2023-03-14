import sqlite3
con = sqlite3.connect("sqlite3/tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE lista_impre(Name, data, furmato)") # a criar tapbela lista_impre