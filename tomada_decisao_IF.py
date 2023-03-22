nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

if idade >= 65:
    print ("O paciente " + nome + " POSSUI atendimento prioritário.")
    print ("Idade superior ou igual a 65 anos.")
else:
    print ("O paciente " + nome + " NÃO POSSUI atendimento prioritário.")
    print ("Idade inferior a 65 anos.")

print("Análise de Atendimento Priortário Conclúida!")

#O Python executa os comandos de acordo com o nível que possuem dentro das estruturas, o que define o nível de cada comando é a identação
#Dentro das estruturas if e else temos um segundo print em cada uma, que assim como o primeiro comando, só será mostrado no output, caso sua respectiva condição seja satisfeita
#Por outro lado, também temos um print que está fora das estruturas if e else, sendo assim, este print será mostrado no output, independente da condição que foi satisfeita