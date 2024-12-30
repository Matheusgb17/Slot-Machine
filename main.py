import random

MAX_LINHAS = 3
MAX_APOSTA = 100
MIN_APOSTA = 1

LIN = 3
COL = 3

dic_simbolos = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def rodar_slot(lin, col, simbolos):
    print("Rodando slots...\n\n")
    todos_simbolos = []
    for simbolo, dic_simbolos in simbolos.items():
        
        for _ in range(dic_simbolos):
            todos_simbolos.append(simbolo)

    colunas = []    
    for _ in range(col):
        coluna = []
        simbolos_atuais = todos_simbolos[:]
        
        for _ in range(lin):
            valor = random.choice(simbolos_atuais)  
            simbolos_atuais.remove(valor)
            coluna.append(valor)
        
        colunas.append(coluna) 
     
    return colunas

def printar_maquina(colunas):
    for lin in range(len(colunas[0])):
        
        for i, coluna in enumerate(colunas):
            
            if i != len(colunas)-1:
                print(coluna[lin], end = " | ")
            else:
                print(coluna[lin], end = "")
        print()

def depositar():
    while True:
        montante = input("Quanto gostaria de depositar? R$")
        if montante.isdigit():
            montante = int(montante)
            if montante > 0:
                break
            else:
                print("O montante deve ser maior que zero!")
        else:
            print("Por favor, insira um numero!")

    return montante

def escolher_numero_de_linhas():
    while True:
        linhas = input("Insira o numero de linhas de aposta (1-" + str(MAX_LINHAS) + ") : ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAX_LINHAS:
                break
            else:
                print("Insira um numero valido!")
    return linhas

def escolher_aposta():
    while True:
        montante = input("Quanto gostaria de apostar? R$")
        if montante.isdigit():
            montante = int(montante)
            if MIN_APOSTA <= montante <= MAX_APOSTA:
                break
            else:
                print(f"O montante deve ser entre R${MIN_APOSTA} e R${MAX_APOSTA}!")
        else:
            print("Por favor, insira um numero!")

    return montante

def verifica_saldo(aposta, saldo):
    return aposta <= saldo

def main():
    saldo = depositar()
    linhas = escolher_numero_de_linhas()
    aposta = escolher_aposta()

    total = aposta * linhas

    if verifica_saldo(total, saldo):
        print(f"Voce esta apostando R${aposta} em {linhas} linhas. A aposta total é: R${total}")
    else:
        print("Voce não tem saldo suficiente para essa aposta!")

    slots = rodar_slot(LIN, COL, dic_simbolos)
    printar_maquina(slots)


main()
