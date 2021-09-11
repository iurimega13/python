"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in palavras:
    print('\nNa palavra {} temos '.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.lower() in vogais:
            print('{}'.format(letra), end=' ')