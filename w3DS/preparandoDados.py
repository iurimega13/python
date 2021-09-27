# Importar a biblioteca Pandas
import pandas as pd

"""
- Nomeie o quadro de dados como health_data
- header=0 significa que os cabeçalhos dos nomes das variáveis ​​devem ser encontrados na primeira linha (observe que 0significa a primeira linha em Python)
- sep=","significa que "," é usado como separador entre os valores. Isso ocorre porque estamos usando o tipo de arquivo .csv (valores separados por vírgula)
"""
# Importar o arquivo de dados
health_data = pd.read_csv('w3DS/data.csv', header=0, sep=",")
print(health_data)

print('\n\n','-=-'*40)

# Limpando os dados
health_data.dropna(axis=0,inplace=True)
# Resultado é um conjunto de dados sem linhas NaN
print(health_data)
print('\n\n','-=-'*40)


# Podemos usar a info()função para listar os tipos de dados em nosso conjunto de dados: 
print(health_data.info())
print('\n\n','-=-'*40)

# Podemos usar a astype()função para converter os dados object em float64.
health_data["Average_Pulse"] = health_data["Average_Pulse"].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)
# Resultado é um conjunto de dados com os dados float64
print (health_data.info())
print('\n\n','-=-'*40)


# Podemos usar a describe()função em Python para resumir os dados:
print(health_data.describe())
print('\n\n','-=-'*40)