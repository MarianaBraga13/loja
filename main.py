from db import criar_tabs
from login import tela_login
from produtos_teste import tela_principal

if __name__ == "__main__":
    criar_tabs()
    tela_login(tela_principal)

# observações importantes:

# estou passando tela_principal como parâmetro
# para a tela_login
# isso permite que se o acesso for liberado
# a tela_principal seja acessada só depois do login

# se algum script importar o main, não executará nada que esteja após
# a if __name__ == "__main__:" para não corrermos o risco de que
# outros projetos comecem a executar funções desnecessárias

