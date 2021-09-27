import pandas as pd


# Simples separador
def separador():
    print("\n" + "-" * 100 + "\n")


# Definindo dados com coluna e linhas em uma variável chamada d
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

# Criando um quadro de dados usando a função pd.DataFrame ()
df = pd.DataFrame(data = d)

# Imprimindo o quadro de dados
print(df)

separador()

# Imprimindo o número de colunas
print('Número de colunas --> {}'.format(df.shape[1]))

separador()

# Imprimindo o número de linhas
print('Número de linhas --> {}'.format(df.shape[0]))

separador()