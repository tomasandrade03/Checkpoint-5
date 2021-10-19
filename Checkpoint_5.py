'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Fábio Henrique Cabrini
Atividade: Checkpoint 5 - 2º Semestre
Alunos:
Gabriel Anselmo Pires Dos Santos - RM87010
Tomás Esteves Andrade - RM89081
'''
import socket
import ipaddress
import re

IP = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

while True:
    IP = input("Digite o IP que deseja escanear: ")
    try:
        validIP = ipaddress.ip_address(IP)
        print("Endereço válido!")
        break
    except:
        print("Esse endereço não é válido!")

for i in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.00001)
        con = s.connect_ex((IP,i))
        if con == 0:
            print ("Portas abertas: ", i)
print("\nScan finalizado!")
