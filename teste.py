from db import conectar

def mostrar_users_cadastrados():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    cadastrados = cursor.fetchall()
    conn.close()

    print("Usuários com cadastro:\n")
    if cadastrados:
        for usuario in cadastrados:
            
            print(f"ID: {usuario[0]} - Nome: {usuario[1]} - Senha: {usuario[2]}")
    else:
        print("Sem usuários cadastrados no momento.\n")

mostrar_users_cadastrados()

def mostrar_prod_cadastrados():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    prod_cadastrados = cursor.fetchall()
    conn.close()

    print("\nAqui os produtos cadastrados no banco de dados:\n")
    if prod_cadastrados:
        for produto in prod_cadastrados:
            print(f"ID: {produto[0]} - Nome: {produto[1]} - Preço: R${produto[2]:.2f}")
    else:
        print("Não há produtos cadastrados no momento.")

mostrar_prod_cadastrados()

# Deletando o usuário duplicado
def deletar_user_duplicado():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id=3')
    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        print(f"O usuário duplicado foi excluído com sucesso!")
    else:
        print("Não há usuários duplicados para serem deletados, no momento.")

deletar_user_duplicado()

# deletando duplicidades automaticamente (ver)