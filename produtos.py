# CRUD produtos

# Buscar produtos
import tkinter as tk
from tkinter import messagebox
from db import conectar

# definindo a função de busca
def carregar_produtos(lista, nome_entry):
    conn = conectar()
    cursor = conn.cursor()
    nome_da_busca = nome_entry.get().strip()
    # banco de dados -> (SELECT) / front-end -> (nome_busca)
    cursor.execute('SELECT * FROM produtos WHERE nome LIKE ?', (f'%{nome_da_busca}%',))

    # procurando o nome ou parte dele dentro do banco de dados
    # produtos_validos = "retorno de algo na busca", se sim, o cursor seleciona todos
    produtos_validos = cursor.fetchall()
    conn.close()

    # back-end ---> front-end: mostrando na tela as opções de produtos ao usuário
    if produtos_validos:
        # criando a lista
        for row in produtos_validos:
            lista.insert(tk.END, f'{row[0]} - {row[1]} - R${row[2]:.2f}')
    else:
        lista.insert(tk.END, "Nenhum produto encontrado.")

#adicionar produtos

def adicionar_produtos(nome_entry, preco_entry, lista):
    #captar o valor digitado
    nome = nome_entry.get()
    preco = preco_entry.get()

    #resolvendo exceções
    preco = float(preco)
    if not nome or not preco:
        messagebox.showwarning("Atenção", "Preencha ambos os campos.")
        return
    
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO produtos (nome, preco) VALUES (?, ?)', (nome, preco))
        conn.close()
        messagebox.showinfo("Produto cadastrado com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "Produto inválido.")

    #limpar o produto digitado
    carregar_produtos(lista)
    nome_entry.delete(0, tk.END)
    preco_entry.delete(0, tk.END)

# Importante! Faltou verificar se o produto existe ou não

# deletar o produto (ele já foi carregado)
# Imortante! Testar se o usuário consegue selecionar o que ele quer
# Estudo: ver como ficaria o código se ele tivesse que digitar o nome inteiro do produto
def deletar_produto(lista):
    item = lista.get(tk.ACTIVE) # Importante! Aqui o ACTIVE deve estar deletando todos os produtos!Revisar.
    if item:
        # aqui preciso dizer para ele como ele acha o id do produto
        # back-end
        produto_id = int(item.split(" - ")[0])
        # banco de dados
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM produtos WHERE id = ?', (produto_id))
        conn.commit()
        conn.close()
        # Importante!Para quê preciso carregar a lista novamente no back-end? Revisar
        carregar_produtos(lista)







