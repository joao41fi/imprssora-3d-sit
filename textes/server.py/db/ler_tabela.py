import sqlite3

# Abre uma conexão com o banco de dados
conn = sqlite3.connect('exemplo.db')

# Executa uma consulta na tabela "usuarios" e obtém todos os registros
cursor = conn.execute("SELECT * from usuarios")
registros = cursor.fetchall()

# Imprime os registros na tela
for registro in registros:
    print(registro)

# Fecha a conexão com o banco de dados
conn.close()
