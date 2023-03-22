nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infecto = input("Suspeita de doença infectocontagiosa? ").upper()

if idade >= 65:
    print ("O paciente " + nome + " POSSUI atendimento prioritário.")
    print ("Idade superior ou igual a 65 anos.")
elif doenca_infecto=="SIM":
    print ("O paciente " + nome + " deve ser redirecionado para a sala de espera reservada!")
else:
    print ("O paciente " + nome + " NÃO POSSUI atendimento prioritário.")
    print ("Idade inferior a 65 anos.")

print("Análise de Atendimento Priortário Conclúida!")