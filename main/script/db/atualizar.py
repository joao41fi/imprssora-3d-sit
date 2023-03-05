import sqlite3


def atualizar_tabela(nome_banco, nome_tabela, coluna_atualizar, valor_atualizar):
    # Conectar ao banco de dados
    conn = sqlite3.connect(nome_banco)
    c = conn.cursor()

    # Montar a query SQL
    query = f"UPDATE {nome_tabela} SET {coluna_atualizar} = ?"
    valores = (valor_atualizar, )

    # Executar a query e salvar as mudanças
    c.execute(query, valores)
    conn.commit()

    # Fechar a conexão com o banco de dados
    conn.close()

    # Mostrar mensagem de sucesso
    print(f"Registros atualizados na tabela {nome_tabela} com sucesso!")


if __name__ == '__main__':
 atualizar_tabela("main/ficheiro.db", "fichieros", "FICH ","gcodees")