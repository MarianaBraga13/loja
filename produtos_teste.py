import tkinter as tk
from tkinter import messagebox
from db import conectar

# definindo função para carregar lista de produtos
def carregar_produtos(lista):
    lista.delete(0, tk.END)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    prod_encontrados = cursor.fetchall()
    

    if prod_encontrados:
        
        for p in prod_encontrados:
            lista.insert(tk.END, f"{p[0]} - {p[1]} - R${p[2]:.2f}")
    else:
        lista.insert(tk.END, "Não existe nenhum produto cadastrado.")
        conn.close()        

# adicionar produtos
def adicionar_produtos(nome_entry, preco_entry, lista):
    nome = nome_entry.get()
    preco = float(preco_entry.get())
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos WHERE nome=?', (nome,))
    prod_encontrado = cursor.fetchone()

    if prod_encontrado:
        messagebox.showerror("Erro", "Produto já existe!")

    else:
        cursor.execute('INSERT INTO produtos (nome, preco) VALUES (?, ?)', (nome,preco))
        conn.commit()
        conn.close()    
        messagebox.showinfo("Info", "Produto cadastrado com sucesso!")
        carregar_produtos(lista)

# deletando produtos
def deletar_produtos(lista):
    item = lista.get(tk.ACTIVE)
    if item:
        produto_id = int(item.split(" - ")[0]) #aqui informo para ele qual é o id
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM produtos WHERE id=?', (produto_id,))
        conn.commit()
        conn.close()
        carregar_produtos(lista)

# update do valor do produto

def atualizar_preco(janela, lista, preco_entry, produto_id):
    novo_preco = float(preco_entry.get())
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('UPDATE produtos SET preco=? WHERE id=?', (novo_preco, produto_id))
        conn.commit()
        conn.close()

        if cursor.rowcount > 0:
            messagebox.showinfo("Sucesso", "Preço atualizado com sucesso!")
            janela.destroy()
            carregar_produtos(lista)
        else:
            messagebox.showwarning("Aviso", "Produto não encontrado.")
    except ValueError:
        messagebox.showinfo("Erro", "Insira um valor numérico válido.")         

def tela_principal():
    root = tk.Tk()
    root.title("Painel de Produtos")
    root.geometry("400x500")

    tk.Label(root, text="Nome do Produto").pack()
    nome_entry = tk.Entry(root)
    nome_entry.pack()

    tk.Label(root, text="Preço do Produto").pack(pady=5)
    preco_entry = tk.Entry(root)
    preco_entry.pack()

    lista = tk.Listbox(root, width=50)
    lista.pack(pady=10)

    tk.Button(root, text="Adicionar Produto", command=lambda:adicionar_produtos(nome_entry, preco_entry, lista)).pack(pady=5)
    tk.Button(root, text="Deletar Produto", command=lambda:deletar_produtos(lista)).pack(pady=5)
    tk.Button(root, text="Atualizar Preço", command=lambda:abrir_painel_atualização(lista)).pack(pady=5)
    carregar_produtos(lista)
    root.mainloop()

def abrir_painel_atualização(lista):
    item_selecionado = lista.get(tk.ACTIVE)
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione um produto para atualizar.")
        return
    partes = item_selecionado.split(" - ")
    produto_id = partes[0]
    nome_produto = partes[1]

    janela = tk.Toplevel()
    janela.title("Atualizar Produto")
    janela.geometry("300x400")

    tk.Label(janela, text=f"Produto: {nome_produto}").pack()
    tk.Label(janela, text="Novo preço").pack()
    preco_entry = tk.Entry(janela)
    preco_entry.pack()

    tk.Button(janela, text="Atualizar", command=lambda:atualizar_preco(janela, lista, preco_entry, produto_id)).pack()

    