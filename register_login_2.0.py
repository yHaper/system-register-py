# Teste da junção dos dois scripts (de registro e de login)

import os
import time

os.system ("clear")
print ("\033[1;32mREGISTRO\033[m\n")
register = input("\033[0;32mCrie um novo usuario: \033[m")
time.sleep(0.2)
os.system ("clear")
print ("\033[1;32mREGISTRO\033[m\n")
senha = input("\033[0;32mOlá {}, agora crie uma senha: \033[m".format(register.title()))
dados = register, senha

time.sleep(0.5)
os.system ("clear")
print ("\033[0;32mRegistro finalizado!\033[m")
time.sleep(0.5)
os.system ("clear")

print ("\033[1;32mLOGIN\033[m\n")
if dados:
    login = input("\033[0;32mDigite seu usuario: \033[m")
    if login == register:
        time.sleep(0.5)
        os.system("clear")
        reset = 0

        while reset < 1:
            login = input("\033[0;32mDigite sua senha: \033[m")
            if login == senha:
                os.system("clear")
                print("\033[1;32mLogado com sucesso!\033[m")
                reset += 1
            else:
                print ("\033[0;31mSenha ou usuario fornecido, não existe!\033[m")
                rset = input("\033[0;32mDeseja tentar novamente? [Y/n]: \033[m")
                if rset == "n" or rset == "N":
                    os.system("clear")
                    reset += 1
                else:
                    os.system("clear")
    else:
        os.system("clear")
        print ("\033[0;31mSenha ou usuario fornecido, não existe!\033[m")


# POR INCRIVEL QUE PARECE, A MINHA IDEIA DEU CERTO.
# CONSEGUI CRIAR UM SISTEMA DE REGISTRO E LOGIN SOZINHO
# Proximo passo: fazer uma copia desse script e fazer comentarios linha por linha
# explicanro para que cada linha serve.
