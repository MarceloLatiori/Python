
def servico():
    print('Seja Bem-Vindo á CopyaLL do Marcelo Latiori')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')
# função com valores de serviço
def valor_servico():
    return {'DIG': 1.10, 'ICO': 1.00, 'IPB': 0.40, 'FOT': 0.20}
# função para escolha do servico
def escolha_servico():
    valores = valor_servico()
    while True:
        escolha = input('Entre com o tipo de Serviço Desejado: ').upper()    
        if escolha in valores:
            print(f'Valor do serviço é de: R$ {valores[escolha]:.2f}')
            return escolha
        else:
            print('Serviço inválido. Escolha entre DIG, ICO, IPB ou FOT.')
# função para definir a quantidade de páginas, um loop try ...except para que a entrada seja um numero inteiro;
def num_pagina():
    while True:
        try:
            num_paginas = int(input('Qual o número de páginas: '))
            if num_paginas < 10:
                print('Número de páginas sem desconto')
                return num_paginas
            elif 10 <= num_paginas < 100:
                print('O número de páginas com desconto é de 10%')
                return num_paginas - (num_paginas * 0.10)
            elif 100 <= num_paginas < 1000:
                print('O número de páginas com desconto é de 15%')
                return num_paginas - (num_paginas * 0.15)
            elif 1000 <= num_paginas < 10000:
                print('O número de páginas com desconto é de 20%')
                return num_paginas - (num_paginas * 0.20)
            else:
                print('Não é aceito pedidos nessa quantidade de páginas')
        except ValueError:
            print('Insira um valor válido: digite um valor numérico')
# oferece serviços adicionais, usa um loop para garantir que a escolha seja valida e imprime o valor do serviço escolhido.
# usa um try...except para garantir que o usuario para garantir que a entrada seja valida.
def servico_extras():
    print("Serviços Extra: ")
    print("1 - Encadernação simples (R$ 10.00)")
    print("2 - Encadernação de capa dura (R$ 25.00)")
    print("0 - Não desejo mais nada (R$ 0.00)")

    while True:
        try:
            adicional = int(input("Escolha um Serviço ADICIONAL: "))
            if adicional == 1:
                print('O valor do adicional é de: R$ 10.00')
                return 10.00
            elif adicional == 2:
                print('O valor do adicional é de: R$ 25.00')
                return 25.00
            elif adicional == 0:
                print('Sem adicional. R$ 0.00')
                return 0.00
            else:
                print("Escolha de extra inválida. Não será adicionado nenhum valor extra.")
        except ValueError:
            print('Digite um Adicinal valido')
# função para calcular os valores
def calcular_valor_total(valor_servico, num_paginas, valor_extra):
    return (valor_servico * num_paginas) + valor_extra
# inicio do main chamando as funções anteriores
servico()
servico_escolhido = escolha_servico()
valor_servicos = valor_servico()
valor_paginas_com_desconto = num_pagina()

valor_extra = servico_extras()
valor_total = calcular_valor_total(valor_servicos[servico_escolhido], valor_paginas_com_desconto, valor_extra)

print(f'Valor com desconto: R$ {valor_total:.2f}')
print('Obrigado por escolher os serviços da CopyaLL' )

