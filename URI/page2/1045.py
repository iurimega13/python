"""
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A² = B² + C², apresente a mensagem: TRIANGULO RETANGULO
se A² > B² + C², apresente a mensagem: TRIANGULO OBTUSANGULO
se A² < B² + C², apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).
Saída
Imprima todas as classificações do triângulo especificado na entrada.
Exemplos de Entrada	Exemplos de Saída
7.0 5.0 7.0
TRIANGULO ACUTANGULO
TRIANGULO ISOSCELES
6.0 6.0 10.0
TRIANGULO OBTUSANGULO
TRIANGULO ISOSCELES
6.0 6.0 6.0
TRIANGULO ACUTANGULO
TRIANGULO EQUILATERO
5.0 7.0 2.0
NAO FORMA TRIANGULO

"""
a, b, c = map(float, input().split())
a, b, c = sorted([a, b, c], reverse=True)

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
elif a**2 == (b**2 + c**2):
    print('TRIANGULO RETANGULO')
elif a**2 > (b**2 + c**2):
    print('TRIANGULO OBTUSANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
else:
    print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
