l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))

print('Para pintar essa parede de {}m² será necessario {}L de tinta!.'.format(
    (a * l),
    ((a * l) / 2)
    ))