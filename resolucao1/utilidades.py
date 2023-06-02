def validaRecebimentoDeVetor(entrada):
    vetor = converteStringEmVetorDeInteiros(entrada)
    if len(vetor) != 20:
        return False

    for i in vetor:
        if type(i) is not int:
            return False

    return True


def converteStringEmVetorDeInteiros(entrada):
    stringSemEspacos = entrada.replace(" ", "")
    valores = stringSemEspacos.split(",")

    vetor = []
    for valor in valores:
        try:
            vetor.append(int(valor))
        except:
            vetor = [1]
            return vetor
        
    return vetor