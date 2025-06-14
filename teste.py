from db import conectar

#criar função para ver todos os usuários no banco
def ver_cadastrados():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    cadastrados = cursor.fetchall()
    conn.close()

    if cadastrados:
        for usuario in cadastrados:
            print("Usuários cadastrados no banco de dados:")
            print(f"{usuario[0]} - {usuario[1]}")
    else:
        print("Sem usuários cadastrados.")

ver_cadastrados()        
