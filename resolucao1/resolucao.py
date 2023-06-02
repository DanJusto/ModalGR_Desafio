import utilidades

def criaVetorDeRepetidos(vetor1, vetor2):
    vetorFinal = []

    for i in vetor1:
        for j in vetor2:
            if i == j and i not in vetorFinal:
                vetorFinal.append(i)
                continue

    return vetorFinal
    

def main():
    entrada1 = input("Vetor 1 - Digite 20 números inteiros separados por vírgula: ")
    while utilidades.validaRecebimentoDeVetor(entrada1) == False:
        entrada1 = input("Vetor 1 - Valores digitados não correspondem a regra. Digite 20 números inteiros separados por vírgula: ")

    entrada2 = input("Vetor 2 - Digite 20 números inteiros separados por vírgula: ")
    while utilidades.validaRecebimentoDeVetor(entrada2) == False:
        entrada2 = input("Vetor 2 - Valores digitados não correspondem a regra. Digite 20 números inteiros separados por vírgula: ")

    vetor1 = utilidades.converteStringEmVetorDeInteiros(entrada1)
    vetor2 = utilidades.converteStringEmVetorDeInteiros(entrada2)

    vetorFinal = criaVetorDeRepetidos(vetor1, vetor2)

    print(vetorFinal)

main()