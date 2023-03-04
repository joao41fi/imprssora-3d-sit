import sqlite3

# Abre uma conexão com o banco de dados
conn = sqlite3.connect('main/ficheiro.db')

# Cria uma tabela chamada "usuarios"
conn.execute('''CREATE TABLE fichieros
(FICH TEXT PRIMARY KEY NOT NULL);''')

# Insere um registro na tabela "usuarios"
conn.execute("INSERT INTO fichieros (FICH) VALUES ('texte.gcode')")

# Salva as mudanças e fecha a conexão com o banco de dados
conn.commit()
conn.close()
