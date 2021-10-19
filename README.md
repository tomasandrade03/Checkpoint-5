--> O código foi desenvolvido e executado em um ambiente Linux.
    Tem a finalidade de escanear um IP com o intuito de verificar quais portas estão abertas naquele host.
    
--> Funcionamento

Neste primeiro trecho do código, são utilizadas as bibliotecas RE e IPADDRESS para que a validação do IP que será escaneado seja feita. Caso esse IP seja inválido, o usuário terá a oportunidade de inseri-lo novamente.
![image](https://user-images.githubusercontent.com/83794673/137901584-820df9db-43cd-4114-be9a-068591c4c1eb.png)

Já neste segundo trecho do código, a biblioteca que está sendo utilizada é a SOCKET, e tem a função de fazer uma conexão com o host solicitado para que a verificação de portas abertas possa ser feita.
![image](https://user-images.githubusercontent.com/83794673/137902683-75df1034-3fae-49ce-892b-1b10d66cfe86.png)

Print de demonstração do funcionamento do código:
![image](https://user-images.githubusercontent.com/83794673/137903596-60f19d58-60fb-4527-8786-ead6f7c8dbdd.png)
![image](https://user-images.githubusercontent.com/83794673/137904094-8beb1071-9adc-4478-b566-3037598ca406.png)


