from db import criar_tabs
from login import tela_login
from produtos import tela_principal

# estou passando tela_principal como parâmetro
# para a tela_login
# isso permite que se o acesso for liberado
# a tela_principal seja acessada só depois do login

if __name__ == "__main__":
    criar_tabs()
    tela_login(tela_principal)


