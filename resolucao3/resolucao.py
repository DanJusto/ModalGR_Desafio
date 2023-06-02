from datetime import date
from dateutil.relativedelta import relativedelta
import utilidades
import cash


def verificaTempoDeCasa(data):
    hoje = date.today()

    diferenca = relativedelta(hoje, data)

    if diferenca.years < 5:
        return False
    
    return True


def verificaTetoEmprestimo(salario, emprestimo):
    teto = salario * 2
    if emprestimo > teto:
        return False
    
    return True


def calcularNotasMaiorValor(emprestimo):

    notasDeCem = cash.pegarNotasCem(emprestimo)
    valorRemanescente = emprestimo - (notasDeCem * 100)
    
    notasDeCinquenta = cash.pegarNotasCinquenta(valorRemanescente)
    valorRemanescente -= (notasDeCinquenta * 50)

    notasDeVinte = cash.pegarNotasVinte(valorRemanescente)
    valorRemanescente -= (notasDeVinte * 20)

    notasDeDez = cash.pegarNotasDez(valorRemanescente)
    valorRemanescente -= (notasDeDez * 10)

    notasDeCinco = 0
    if valorRemanescente % 2 != 0:
        notasDeCinco = cash.pegarNotasCinco(valorRemanescente)
        valorRemanescente -= (notasDeCinco * 5)

    notasDeDois = cash.pegarNotasDois(valorRemanescente)
    valorRemanescente -= (notasDeDois * 2)

    return {
        "cem": notasDeCem,
        "cinquenta": notasDeCinquenta, 
        "vinte": notasDeVinte,
        "dez": notasDeDez,
        "cinco": notasDeCinco,
        "dois": notasDeDois
        }


def calcularNotasMenorValor(emprestimo):

    notasDeVinte = cash.pegarNotasVinte(emprestimo)
    valorRemanescente = emprestimo - (notasDeVinte * 20)

    notasDeDez = cash.pegarNotasDez(valorRemanescente)
    valorRemanescente -= (notasDeDez * 10)

    notasDeCinco = 0
    if valorRemanescente % 2 != 0:
        notasDeCinco = cash.pegarNotasCinco(valorRemanescente)
        valorRemanescente -= (notasDeCinco * 5)

    notasDeDois = cash.pegarNotasDois(valorRemanescente)
    valorRemanescente -= (notasDeDois * 2)

    return {
        "vinte": notasDeVinte,
        "dez": notasDeDez,
        "cinco": notasDeCinco,
        "dois": notasDeDois
        }


def calcularNotasMeioMeio(emprestimo):

    metade = emprestimo / 2
    ultimoDigito = metade % 10

    if ultimoDigito == 1 or ultimoDigito == 3:
        notasDeCinco = 1
        notasMaiores = calcularNotasMaiorValor(metade - 5)
        notasMaiores["cinco"] = notasDeCinco
        notasMenores = calcularNotasMenorValor(metade - 5)
        notasMenores["cinco"] = notasDeCinco
    else:
        notasMaiores = calcularNotasMaiorValor(metade)
        notasMenores = calcularNotasMenorValor(metade)

    return [notasMaiores, notasMenores]


def pegarNotasUtilizadas(notas):

    if type(notas) == dict:
        notasUtilizadas = {}
        for chave in notas.keys():
            if notas[chave] != 0:
                notasUtilizadas[chave] = notas[chave]

        return notasUtilizadas

    vetor = []
    notasUtilizadas0 = {}
    for chave in notas[0].keys():
        if notas[0][chave] != 0:
            notasUtilizadas0[chave] = notas[0][chave]
    vetor.append(notasUtilizadas0)

    notasUtilizadas1 = {}
    for chave in notas[1].keys():
        if notas[1][chave] != 0:
            notasUtilizadas1[chave] = notas[1][chave]
    vetor.append(notasUtilizadas1)

    return vetor
    

def mensagem(notas, titulo):

    if type(notas) == dict:
        print(titulo)
        for chave in notas.keys():
            print(f"\t- {notas[chave]} de {chave} reais")

        return 0
    else:
        print("Notas meio a meio:")
        print(f"{titulo} reais em notas de maior valor:")
        for chave in notas[0].keys():
            print(f"\t- {notas[0][chave]} de {chave} reais") 

        print(f"{titulo} reais em notas de menor valor:")
        for chave in notas[1].keys():
            print(f"\t- {notas[1][chave]} de {chave} reais") 

        return 0

def main():
    dadosEmprestimo = utilidades.recebeEValidaInformacoes()

    if verificaTempoDeCasa(dadosEmprestimo.get("data")) == False or verificaTetoEmprestimo(dadosEmprestimo.get("salario"), dadosEmprestimo.get("emprestimo")) == False:
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
        return 1

    notasMaiorValor = calcularNotasMaiorValor(dadosEmprestimo.get("emprestimo"))
    notasMenorValor = calcularNotasMenorValor(dadosEmprestimo.get("emprestimo"))
    NotasMeioMeio = calcularNotasMeioMeio(dadosEmprestimo.get("emprestimo"))

    notasMaiorValorUtilizadas = pegarNotasUtilizadas(notasMaiorValor)
    notasMenorValorUtilizadas = pegarNotasUtilizadas(notasMenorValor)
    notasMeioMeioUtilizadas = pegarNotasUtilizadas(NotasMeioMeio)

    mensagem(notasMaiorValorUtilizadas, "Notas de maior valor:")
    mensagem(notasMenorValorUtilizadas, "Notas de menor valor:")
    mensagem(notasMeioMeioUtilizadas, (dadosEmprestimo.get("emprestimo") // 2))

    return 0

main()