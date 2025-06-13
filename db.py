import sqlite3

#forma mais comum de criar um banco de dados
#criar uma função para conectar e criar ao mesmo tempo o banco
def conectar():
    return sqlite3.connect("loja.db")

#criar uma função para inserir tabelas
def criar_tabs():
    #criar um executor, no caso o cursor
    #antes é necessário armazenar a função conectar() em uma variável
    #porque vamos reutiliza-la para fechar a conexão
    #não teria como saber qual a conexão está aberta
    conn = conectar()
    #agora crio o cursor que vai manipular os dados
    #e já o armazeno conectado
    cursor = conn.cursor()
    #criando as tabelas
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   senha TEXT NOT NULL
                    );
    """)
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   preco REAL NOT NULL
                   );
    """)

    #salvando e fechando a conexão
    conn.commit()
    conn.close()
