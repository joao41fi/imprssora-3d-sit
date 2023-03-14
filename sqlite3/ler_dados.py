import sqlite3
con = sqlite3.connect("sqlite3/tutorial.db")
cur = con.cursor()
res = cur.execute("SELECT Name FROM lista_impre")

for row in cur.execute("SELECT Name, data,furmato FROM lista_impre"):
    print(row)

    

    # esta a obeter a lista toda vai ser divertido 