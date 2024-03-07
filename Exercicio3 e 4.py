'''
EXERCICIO 3
a) 1, 3, 5, 7, 9

A lógica é adicionar 2 ao elemento anterior

b) 2, 4, 8, 16, 32, 64, 128

A lógica é multiplicar o elemento anterior por 2

c) 0, 1, 4, 9, 16, 25, 36, 49

A lógica é que o correspondente do elemento é elevado ao quadrado. A sequência vai até
6 ao quadrado, o próximo deve ser 7 ao quadrado

d) 4, 16, 36, 64, 100

A lógica é similar à anterior, mas apenas para números pares.

e) 1, 1, 2, 3, 5, 8, 13

A lógica é a formação da sequência de Fibonacci

f) 2,10, 12, 16, 17, 18, 19, 20

Imagino que seja 20, mas não tenho certeza de como é a lógica para este item.

'''
# --------------------------------------------------------------------------------
'''
EXERCICIO 4

Eu ligo um dos interruptores (i1) e vou a uma das salas (s1). 
Se a lampada estiver acesa, faço i1 - s1
Se i1 - s1, eu volto para a sala dos interruptores e ligo o segundo interruptor.  
Vou para s2. Se a lampada estiver acesa, i2 - s2, e por consequencia i3 - s3

senão, sei que i1 - s2 ou i1 - s3.
Desligo i1 e ligo i2. Vou a s2. Se a lampada estiver acesa, sei que i2 - s2, i1 - s3 e
i3 - s1.
Se a lampada não estiver acesa, sei que i2 - s1 ou i2 - s3. Eu usaria como tentativa
i2 - s3, i1 - s2 e i3 - s1

'''