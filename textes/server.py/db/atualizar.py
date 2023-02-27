import sqlite3

# Define as variáveis para atualização
id_usuario = 1
nome_usuario = 'Maria'
idade_usuario = 25

# Abre uma conexão com o banco de dados
conn = sqlite3.connect('exemplo.db')

# Atualiza o registro com o ID especificado na tabela "usuarios"
conn.execute("UPDATE usuarios SET NOME = ?, IDADE = ? WHERE ID = ?", (nome_usuario, idade_usuario, id_usuario))

# Salva as mudanças e fecha a conexão com o banco de dados
conn.commit()
conn.close()