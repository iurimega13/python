nome = input('Digite seu nome completo: ').strip()

print("""
Muito prazer em te conhecer!
Seu primeiro nome é {}
Seu ultimo nome é {}
      """.format(nome.split()[0], nome.split()[-1]))