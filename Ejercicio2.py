import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros del experimento cuántico
num_targets = 10  # Cantidad de objetivos en la pantalla
amplitudes = np.random.rand(num_targets) + 1j * np.random.rand(num_targets)  # Amplitudes aleatorias complejas
probabilities = np.abs(amplitudes) ** 2  # Probabilidad es el cuadrado del módulo de la amplitud
probabilities /= np.sum(probabilities)  # Normalizar

# Simulación del experimento
num_particles = 1000
hits = np.random.choice(range(num_targets), size=num_particles, p=probabilities)

# Contar cuántas partículas impactaron cada objetivo
intensities = np.bincount(hits, minlength=num_targets)

# Gráfico de resultados
plt.bar(range(num_targets), intensities)
plt.xlabel('Objetivo en la pantalla')
plt.ylabel('Intensidad (Número de impactos)')
plt.title('Experimento de doble rendija cuántico')
plt.show()
