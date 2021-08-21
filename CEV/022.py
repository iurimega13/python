nome = input('Digite seu nome: ')

print("""
Analizando seu nome...
Seu nome em maiúsculas é {}
seu nome em minúsculas é {}
Seu nome ao todo tem {} letras
Seu primeiro nome é {} e tem {} letras     
      """.format(nome.upper(), nome.lower(), len(nome), nome.split()[0], len(nome.split()[0])))