numero = int(input("Digite a tabuada desejada: "))
cont = 1

if numero<=0:
    print("Número inválido. Digite um número positivo maior que zero.")
else:
    while cont<11:
        print("\t" + str(numero) + " x " + str(cont) + " = " + str(numero*cont)) #O \t dá um espaço à direita no texto
        cont = cont+1
    print("Esta é a tabuada do número " + str(numero))