import matplotlib.pyplot as plt
import numpy as np

# Dados
tempo = np.array([4, 8, 12, 16, 20, 24])
densidade_optica = np.array([0.011, 0.046, 0.162, 0.459, 0.961, 1.366])
#densidade_optica = [0.011, 0.046, 0.162, 0.459, 0.961, 1.366, 1.498, 1.515, 1.519, 1.537, 1.508, 1.426]

# Função
def crescimento(x):
  return 0.000000 * x**3 + 0.000100 * x**2 - 0.003000 * x + 0.002000

# Gráfico
plt.plot(tempo, densidade_optica, label="Dados")
plt.plot(tempo, crescimento(tempo), label="Função")
plt.xlabel("Tempo (h)")
plt.ylabel("Densidade Óptica")
plt.legend()
plt.show()