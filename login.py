import tkinter as tk
from tkinter import messagebox
from db import conectar

#criando a função para consultar os dados do login/validação do login
def login(nome_entry, senha_entry, root, abrir_painel):
    #preciso receber e guardar os dados inseridos no front-end de usuário e senha
    nome = nome_entry.get()
    senha = senha_entry.get()
    #agora preciso buscar no banco de dados
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE nome=? AND senha=?',(nome, senha))
    usuario_valido = cursor.fetchone()
    conn.close()


    #condições para usuário ingressar:
    if usuario_valido:
        messagebox.showinfo("Login", "Login efetuado com sucesso!")
        root.destroy()
        abrir_painel() #Definida como parâmetro na tela de login
                        #é o painel da def tela_login

    else:
        messagebox.showerror("Erro", "Usuário(a) ou senha inválida.")

#cadastrando o usuário
def cadastrar(nome_entry, senha_entry):
    #preciso do nome e senha
    nome = nome_entry.get()
    senha = senha_entry.get()
    #conectando o cursor novamente
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, senha) VALUES (?, ?)', (nome, senha))
    conn.commit()
    conn.close()
    messagebox.showinfo("Cadastro","Usuário(a) cadastrado(a) com sucesso!")

#definindo a tela de login ------>Front-End

def tela_login(abrir_painel):
    #ativar tela padrão do Tkinter
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x200")

    #criando o espaço para input usuário
    tk.Label(root, text="Usuário").pack() #aqui é o texto sobre o retângulo
    nome_entry = tk.Entry(root) #aqui é aquele retângulo para entrar com dados
    nome_entry.pack()

    #criando o espaço para input da senha
    tk.Label(root, text="Senha").pack
    senha_entry = tk.Entry(root, show="*")
    senha_entry.pack()

    #agora os botões e os comandos do back-end
    tk.Button(root, text="Login",command=lambda:login(nome_entry, senha_entry, root, abrir_painel)).pack(pady=5)
    tk.Button(root, text="Cadastrar", command=lambda:cadastrar(nome_entry, senha_entry)).pack()

    #cria um loop de tela
    root.mainloop()

    
