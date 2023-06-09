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

#O elif nos dá a possibilidade de fazer uma comparação composta, visto que não é uma boa prática usar if's dentro de outros if's, para isso existe o elif
#No código acima verificamos se a idade do paciente é maior ou igual a 65 anos e, se a resposta for Falsa, devemos verificar ainda se o paciente está com suspeita de doença infecto-contagiosa
#E se, ainda assim, for Falsa a condição, então, podemos considerar que o paciente deve aguardar sem prioridade na sala comum de espera