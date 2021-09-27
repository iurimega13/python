import numpy as np

# Simples separador
def separador():
    print("\n" + "-" * 100 + "\n")


print("""
Duração	Average_Pulse	Max_Pulse	Calorie_Burnage	Horas_Trabalho	Hours_Sleep
  30	    80	            120	            240	            10	        7
  30	    85	            120	            250	            10      	7
  45	    90	            130	            260	            8	        7
  45	    95	            130	            270	            8	        7
  45	    100         	140         	280         	0       	7
  60	    105         	140         	290         	7       	8
  60	    110         	145         	300         	7       	8
  60	    115         	145         	310         	8       	8
  75	    120         	150         	320         	0       	8
  75	    125         	150         	330         	8       	8

""")
separador()

# Encontrando o maior valor do Average_pulse
Average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print("O maior valor do Average_pulse é: {}".format(Average_pulse_max))
separador()

# Encontrando o menor valor do Average_pulse
Average_pulse_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print("O menor valor do Average_pulse é: {}".format(Average_pulse_min))
separador()


# A mean() função NumPy é usada para encontrar o valor médio de uma matriz.
Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
Average_Calorie_burnage = np.mean(Calorie_burnage)
print("O valor médio do Calorie_burnage é: {}".format(Average_Calorie_burnage))
separador()