"""exercicio 3
autor: vinicius
instrução: solicite o valor de um capital, o prazo de investimento, a taxa de juros, 
calcule e imprima na tela o valor capitalizado.
versão: 0.0.1"""

# Alocação de memoria

capital_investido = ""
prazo_investimento = ""
taxa_juros = ""

## Entrada de dados

capital_investido = float(input("capital investido: "))
prazo_investimento = int(input("prazo de investimento, meses: "))
taxa_juros = float(input("taxa de juros mensal (%): "))

# Processamento de dados

valor_capitalizado = capital_investido * (1 + (taxa_juros/100)) ** prazo_investimento

#Saída de dados
print(valor_capitalizado)