def pegarNotasCem(valor):
    contador = 0
    valorAtual = 0
    while valor - valorAtual >= 100:
        valorAtual += 100
        contador += 1
    
    return contador

def pegarNotasCinquenta(valor):
    contador = 0
    valorAtual = 0
    while valor - valorAtual >= 50:
        valorAtual += 50
        contador += 1
    
    return contador

def pegarNotasVinte(valor):
    contador = 0
    valorAtual = 0
    while valor - valorAtual >= 20:
        valorAtual += 20
        contador += 1
    
    return contador

def pegarNotasDez(valor):
    contador = 0
    valorAtual = 0
    while valor - valorAtual >= 10:
        valorAtual += 10
        contador += 1
    
    return contador

def pegarNotasCinco(valor):
    contador = 0
    valorAtual = 0
    while valor - valorAtual >= 5:
        valorAtual += 5
        contador += 1
    
    return contador

def pegarNotasDois(valor):
    contador = 0
    valorAtual = 0
    while valor - valorAtual >= 2:
        valorAtual += 2
        contador += 1
    
    return contador