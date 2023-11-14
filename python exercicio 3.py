def servico():
    print('Seja Bem-Vindo á CopyaLL do Marcelo Latiori')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia' )

def escolha_servico():
    valor_DIG = 1.10
    valor_ICO = 1.00
    valor_IPB = 0,40

    while True:
        escolha_servico = input ('Entre com o tipo de Serviço Desejadosssss :')
        if (escolha_servico.upper() == 'DIG'.upper()):
            print('valor do serviço é de : {:.2f}'.format(valor_DIG))
            valor_do_servico = valor_DIG
            return 1.10
        elif (escolha_servico.upper() == 'ICO'.upper()):
            print('valor do serviço é de {:.2f}:'.format(valor_ICO))
            valor_do_servico = valor_ICO
            return 1.00
        elif (escolha_servico.upper() == 'IPB'.upper()):
            print('valor do serviço é de {:.2f} :'.format(valor_IPB))
            valor_do_servico = valor_IPB
            return 0.40
        elif (escolha_servico.upper() == 'FOT'.upper()):
            print('valor do servico é de : {:.2f}'.format(valor_FOT))
            valor_do_servico = valor_FOT
            return 0.20
        else:
            print('serviço invalido')
# inicio da função para escolher o numero de páginas
def num_pagina():
    while True:
        try:
            num_paginas = int(input('Qual o número de páginas: '))

            if (num_paginas < 10):
                print('numero de paginas sem desconto')
                desconto = 0.00 * num_paginas
            elif ((num_paginas >= 10) and (num_paginas < 100)):
                desconto= 0.10
                print('o numero de paginas com desconto é de 10%')
            elif ((num_paginas >= 100) and (num_paginas < 1000)):
                desconto = 0.15
                print('o numero de pagina com desconto é de 15%')
            elif ((num_paginas >= 1000) and (num_paginas < 10000)):
                desconto = 0.20
                print('o numero de  paginas com desconto é de 20%' )
                return num_paginas, desconto
            else:
                (num_paginas >= 10000)
                print('Não é aceito pedidos nessa quantidades de paginas')

        except ValueError:
                print('Insira um valor valido: digite um valor numérico:  ')
# inicio da função extras
def extras():
    print("Serviços Extra: ")
    print("1 - Encadernação simples (R$10.00)")
    print("2 - Encadernação de capa dura (R$25.00)")
    print("0 - Não desejo mais nada (R$0.00)")
# escolha da função extras
    escolha_extra = int(input("Escolha um Serviço  Extra Desejado: "))
    while True:
        if escolha_extra == 1:
            return 10.00
        elif escolha_extra == 2:
            return 25.00
        elif escolha_extra == 0:
            return 0.00
        else:
            print("Escolha de extra inválida. Não será adicionado nenhum valor extra.")

# Início do main

servico = servico()

valor_servico = escolha_servico()
num_paginas = num_pagina()
escolha_extra = extras()

# Calcula o valor sem desconto
valor_sem_desconto = valor_servico * num_paginas

# Calcula o valor com desconto e  extras
valor_com_desconto = valor_sem_desconto - valor_sem_desconto * desconto + escolha_extra

# Imprime os valores com desconto e sem desconto
print(f"Valor sem desconto: R${valor_sem_desconto:.2f}")
print(f"Valor com desconto e extras: R${valor_com_desconto:.2f}")
