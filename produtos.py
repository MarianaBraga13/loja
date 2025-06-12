# CRUD produtos

# Buscar produtos
import tkinter as tk
from tkinter import messagebox
from db import conectar

# definindo a função de busca
def buscar_produtos(lista_exibir, nome_entry):
    conn = conectar()
    cursor = conn.cursor()
    nome_da_busca = nome_entry.get().strip()
    # banco de dados -> (SELECT) / front-end -> (nome_busca)
    cursor.execute('SELECT * FROM produtos WHERE nome LIKE ?', (f'%{nome_da_busca}%',))

    # procurando o nome ou parte dele dentro do banco de dados
    produtos_validos = cursor.fetchall()
    conn.close()

    # back-end ---> front-end: mostrando na tela as opções de produtos ao usuário
    if produtos_validos:
        # criando a lista
        for row in produtos_validos:
            lista_exibir.insert(tk.END, f'{row[0]} - {row[1]} - R${row[2]:.2f}')
    else:
        lista_exibir.insert(tk.END, "Nenhum produto encontrado.")


# criar função e método para adicionar produtos no database
def adicionar_produtos(produto_entry, preco_entry):
    conn = conectar()
    cursor = conn.cursor()
    nome = produto_entry.get()
    preco = preco_entry.get()

    cursor.execute('INSERT INTO produtos', (nome, preco))
