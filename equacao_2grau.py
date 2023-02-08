#cálculo das raízes da equação do segundo grau!
print("A forma da equação do 2º grau é : ax²+bx+c =0 . Entre com os valores de a,b e c")

import math #define uma função matemática que possibilita calcular a raiz quadrada.
a = float(input("Entre com um número a:\n")) #define a entrada de uma variável float
b = float(input("Entre com um número b:\n")) #define a entrada de uma variável float
c = float(input("Entre com um número c:\n"))#define a entrada de uma variável float

delta = b*b-(4*a*c) #Calcula o valor da variável delta

if(delta==0): #condição inicial se delta for igual a zero o programa resolve a solução e a imprime
    solucao=(b*-1)/(2*a)
    print("Há apenas uma raíz real e o valor dela é ", solucao)
else: #caso contrário se delta não for igual a zero temos as seguintes condições:
    if(delta>0): #se delta>0 teremos duas soluções e elas serão impressas
        raiz_delta = math.pow(delta, 1 / 2)
        solucao_1=((b*-1)+(raiz_delta))/(2*a)
        solucao_2=((b*-1)-(raiz_delta))/(2*a)
        print("Há duas raízes reais e o valor delas é ", solucao_1," e ", solucao_2)

    elif(delta<0):#caso contrário, se delta<0 não há solução real e o programa imprime o testo abaixo.
        print("Não exixte raízes reais e o valor de delta é ", delta)
