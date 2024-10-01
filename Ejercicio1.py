import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros del experimento
num_targets = 10  # Cantidad de objetivos en la pantalla
probabilities = np.random.rand(num_targets)  # Probabilidades aleatorias para cada objetivo
probabilities /= np.sum(probabilities)  # Asegurar que sumen 1 (normalización)

# Simulación del experimento
num_particles = 1000  # Número de partículas lanzadas
hits = np.random.choice(range(num_targets), size=num_particles, p=probabilities)

# Contar cuántas partículas impactaron cada objetivo
intensities = np.bincount(hits, minlength=num_targets)

# Gráfico de resultados
plt.bar(range(num_targets), intensities)
plt.xlabel('Objetivo en la pantalla')
plt.ylabel('Intensidad (Número de impactos)')
plt.title('Experimento de doble rendija probabilístico')
plt.show()
