from db import conectar

def mostrar_cadastrados():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    cadastrados = cursor.fetchall()
    conn.close()

    print("Usuários com cadastro:")
    if cadastrados:
        for usuario in cadastrados:
            
            print(f"ID: {usuario[0]} - Nome: {usuario[1]} - Senha: {usuario[2]}")
    else:
        print("Sem usuários cadastrados no momento.")

mostrar_cadastrados()