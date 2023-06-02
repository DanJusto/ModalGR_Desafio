def converteNotas(vetorNotas):
    conversor = {
        "dó":"I",
        "ré":"II",
        "mi":"III",
        "fá":"IV",
        "sol":"V",
        "lá":"VI",
        "si":"VII"
    }

    vetorAlgarismos = []

    for nota in vetorNotas:
        notaMinuscula = nota.lower()
        vetorAlgarismos.append(conversor.get(notaMinuscula, "nota inválida"))

    return vetorAlgarismos


def main():
    entrada = input("Digite as notas musicais que deseja converter separada por vírgula: ")
    stringSemEspacos = entrada.replace(" ", "")
    notas = stringSemEspacos.split(",")

    algarismos = converteNotas(notas)

    print(algarismos)

main()