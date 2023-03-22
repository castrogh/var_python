tabuada = int(input("Digite um número para exibir a tabuada: "))

if tabuada<=0:
    print("Número inválido. Digite um número positivo maior que zero.")
else:
    print("Tabuada do número ", tabuada)
#Neste momento é iniciado o laço for e declarada a variável valor, que está dentro de um range, que tem as seguintes características: a variável valor tem valor inicial igual a 1, vai ter seu final em 11 e é incrementada em +1 a cada vez que o laço for executado 
    for valor in range(1,11,1):
        print("\t" + str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))

#O laço for indica o término do laço de duas formas básicas: por um número que delimita o seu final ou por uma lista de dados que foi verificada por completo.
#Pode-se afirmar que o while trabalha mais diretamente com a interação do usuário final, diferentemente do for, com o que normalmente a situação está previamente definida pelo próprio sistema.
#O exemplo usado também foi o de uma tabuada convencional, igual ao usado no laço while