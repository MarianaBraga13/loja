import tkinter as tk
from tkinter import messagebox
from db import conectar

#definindo a função carregar/buscar

def buscar_produtos(nome_entry, lista):
    nome_busca = nome_entry.get().strip()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos WHERE (nome) LIKE ? VALUE (?)', (f'%{nome_busca}%',))
    # valor encontrado? ---> encontrou produtos?
    # armazene em uma variável !
    produtos_encontrados = cursor.fetchall()
    conn.close()

    # quando os valores encontrados são armazenados em uma variável no back-end
    # podemos então manipulá-los no back-end
    # para podermos exibir uma lista no front-end, por exemplo

    if produtos_encontrados: # ou seja, se o cursor nos traz algo do banco, então...
        # agora precisamos exibir esses dados capturados pelo cursor.fetchall()
        # eles estão armazenados na variável ---> produtos_encontrados
        # exiba-os em uma lista
        # como? percorra os resultados e crie uma nova tabela para o usuário
        for coluna in produtos_encontrados:
            lista.insert(f'{coluna[0]} - {coluna[1]} - R${coluna[2]}:.2f')
    else:
        lista.insert(tk.END, "Nenhum produto encontrado")
        # verificar se aqui ficaria melhor utiliar o messagebox

# adicionando produtos
def incluir_produtos(nome_entry, preco_entry):
    nome = nome_entry.get()
    preco = preco_entry.get()

    # tratando exceção 1
    if not nome or not preco:
        messagebox.showerror("Erro", "Ambos os campos devem ser preenchidos corretamente.")
    # caso esteja correto ---> try it:

    try:
        conn = conectar()
        cursor = conn.cursor()
        # checando se já existe ou não no banco de dados
        cursor.execute('SELECT * FROM produtos WHERE nome =?' (nome,))
        existe = cursor.fetchone()

        if not existe:
            cursor.execute ('INSERT INTO produtos (nome, preco) VALUES (?, ?)', (nome, preco))
            conn.close()
            messagebox.showinfo("Info", f"Produto {nome} cadastrado com sucesso!")
        else:
            messagebox.showinfo("Info", "Produto já cadastrado.")

    except ValueError:
        messagebox.showerror("Erro", "Produto inválido. Não foi possível cadastrá-lo")

# deletando o produto
def deletar_produto(nome_entry):
    nome = nome_entry.get()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos WHERE nome=?'(nome,))
    
    existe = cursor.fetchone()
    conn.close()

    if not existe:
        messagebox.showinfo("Info", "Produto não existe no banco de dados.")
    else:
        cursor.execute('DELETE FROM produtos WHERE nome=?',(nome,))    
    conn.commit()
    conn.close()

    # interface gráfica ---> front-end

    def tela_principal():
        root = tk.Tk()
        root.title("Painel de Produtos")
        root.geometry("400x500")

        tk.Label(root, text="Nome do Produto").pack()
        nome_entry = tk.Entry(root)
        nome_entry.pack()

        tk.Label(root, text="Preço").pack()
        preco_entry = tk.Entry(root)
        preco_entry.pack()

        # Campo de busca
        tk.Label(root, text="Buscar Produto por Nome").pack()
        nome_entry = tk.Entry(root)
        nome_entry.pack()
        tk.Button(root, text="Buscar", command=lambda: buscar_produtos(nome_entry, lista))
        lista = tk.Listbox(root, width=50)
        lista.pack(pady=10)

        tk.Button(root, text="Adicionar Produto", command=lambda:incluir_produtos(nome_entry, preco_entry))
        tk.Button(root, text="Deletar Produto", command=lambda:deletar_produto(nome_entry))

        buscar_produtos(lista)
        root.mainloop()
        

        







