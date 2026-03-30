# Lógica E (and)
from win32file import TF_REUSE_SOCKET

verifica_email = True
verifica_senha = True

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print('Entra no programa.. executa')

#Lóica OU (or)
logica = (False or False or False)
print(logica)
#Operador de negação
negacao = not False
print(negacao)

if not verifica_login:
    print('Loga ai...')