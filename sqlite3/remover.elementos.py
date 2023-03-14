import sqlite3

con = sqlite3.connect("sqlite3/tutorial.db")
cur = con.cursor()

# Definir o ID da linha que será excluída
id_para_apagar = 4

# Definir o comando SQL para excluir a linha
comando_sql = f"DELETE FROM lista_impre WHERE rowid = {id_para_apagar};"

# Executar o comando SQL
cur.execute(comando_sql)

# Salvar as mudanças no banco de dados
con.commit()

# Fechar a conexão com o banco de dados
con.close()