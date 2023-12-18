import os

host = input("Digite o Ip ou Host a ser verificado!")

os.system("ping -n 6 {}".format(host))

