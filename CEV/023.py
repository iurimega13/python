n = int(input('Informe um número: '))

print("""
Analizando o número {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
      """.format(n, n%10, (n%100)//10, (n%1000)//100, n//1000))