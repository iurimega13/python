frase = input("Digite uma frase: ").strip().upper()

print("""
A letra A aparece {} vezes na frase.
A primeira letra A aparece na posição {}.
A ultima letra A aparece na posição {}.
      """.format(frase.count('A'), frase.find('A')+1, frase.rfind('A')+1))