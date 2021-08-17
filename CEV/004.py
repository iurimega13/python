x= input('Digite algo: ')

print('{0} é do alfabeto: {1}'.format(x, x.isalpha()))
print('{0} é númerico: {1}'.format(x, x.isnumeric()))
print('{0} é alfanumérico: {1}'.format(x, x.isalnum()))