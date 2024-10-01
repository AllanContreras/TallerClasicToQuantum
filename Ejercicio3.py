import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros
slit_distance = 0.1  # distancia entre las rendijas
wavelength = 0.5  # longitud de onda
screen_distance = 2.0  # distancia a la pantalla
screen_width = 1.0  # ancho de la pantalla
num_points = 500  # puntos en la pantalla donde se calculará la intensidad

# Posiciones en la pantalla
screen_points = np.linspace(-screen_width/2, screen_width/2, num_points)

# Función para calcular la fase de la onda desde cada rendija
def wave_amplitude(distance, wavelength):
    return np.cos(2 * np.pi * distance / wavelength)

# Distancias desde cada rendija a cada punto en la pantalla
d1 = np.sqrt((screen_points + slit_distance / 2) ** 2 + screen_distance ** 2)
d2 = np.sqrt((screen_points - slit_distance / 2) ** 2 + screen_distance ** 2)

# Amplitudes de las ondas en cada punto en la pantalla
amplitude1 = wave_amplitude(d1, wavelength)
amplitude2 = wave_amplitude(d2, wavelength)

# Superposición de las ondas
total_amplitude = amplitude1 + amplitude2
intensity = total_amplitude ** 2  # La intensidad es proporcional al cuadrado de la amplitud

# Graficar los resultados
plt.plot(screen_points, intensity)
plt.xlabel('Posición en la pantalla')
plt.ylabel('Intensidad')
plt.title('Patrón de interferencia en el experimento de doble rendija')
plt.show()
