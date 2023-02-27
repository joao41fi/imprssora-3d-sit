import sqlite3

# Abre uma conexão com o banco de dados
conn = sqlite3.connect('exemplo.db')

# Cria uma tabela chamada "usuarios"
conn.execute('''CREATE TABLE usuarios
(ID INT PRIMARY KEY NOT NULL, 
NOME TEXT NOT NULL,
IDADE INT NOT NULL,
VIDA INT NOT NULL);''')

# Insere um registro na tabela "usuarios"
conn.execute("INSERT INTO usuarios (ID,NOME,IDADE,VIDA) VALUES (1, 'João', 30,'kill')")

# Salva as mudanças e fecha a conexão com o banco de dados
conn.commit()
conn.close()
