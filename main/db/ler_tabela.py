import sqlite3

# Abre uma conexão com o banco de dados
def abrir(caminho,tabela):
 conn = sqlite3.connect(caminho)

 # Executa uma consulta na tabela "usuarios" e obtém todos os registros
 cursor = conn.execute("SELECT * from "+tabela)
 registros = cursor.fetchall()


    
 #print(registros)

 # Fecha a conexão com o banco de dados
 conn.close()
 return registros

if __name__ == '__main__':
  ok = abrir('main/ficheiro.db','fichieros')
  print(ok[0][0])