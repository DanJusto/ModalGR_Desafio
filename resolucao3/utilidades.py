from datetime import datetime

def validarData(dataEmString):
    try:
        datetime.strptime(dataEmString, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def recebeEValidaInformacoes():

    print("Bem-vindo ao programa de empréstimo para colaboradores.")
    print("Informe seus dados para simulação do empréstimo.")

    nome = input("Digite seu nome completo: ")

    dataDeAdmissao = input("Digite a data de sua admissão no formato dd/mm/aaaa: ")
    while validarData(dataDeAdmissao) == False:
        dataDeAdmissao = input("Data inválida. Digite a data de sua admissão no formato dd/mm/aaaa: ")
    data = datetime.strptime(dataDeAdmissao, '%d/%m/%Y').date()

    salarioFuncionario = int(input("Digite seu salário atual excluindo os centavos: R$ "))
    while salarioFuncionario < 1:
        salarioFuncionario = int(input("O valor precisa ser positivo. Digite seu salário atual excluindo os centavos: R$ "))

    valorEmprestimo = int(input("Digite o valor do empréstimo pretendido excluindo os centavos: R$ "))
    while valorEmprestimo % 2 != 0:
        print("Insira um valor válido!")
        valorEmprestimo = int(input("Digite o valor do empréstimo pretendido excluindo os centavos: R$ "))

    informacoes = dict(nome = nome, data = data, salario = salarioFuncionario, emprestimo = valorEmprestimo)

    print("**********************************************************************")

    return informacoes