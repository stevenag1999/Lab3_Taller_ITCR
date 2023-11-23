import numpy as np
import matplotlib.pyplot as plt
import csv

# Leer datos desde el archivo CSV
with open('datos_termocupla.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = {'Tiempo (ms)': [], 'Canal 1 (mV)': []}
    for row in reader:
        data['Tiempo (ms)'].append(float(row['Tiempo (ms)']))
        data['Canal 1 (mV)'].append(float(row['Canal 1 (mV)']))

# Obtener arrays de tiempo y voltaje desde los datos leídos
tiempo_ms = np.array(data['Tiempo (ms)'])
voltaje_mV = np.array(data['Canal 1 (mV)'])

# Relación lineal entre voltaje y temperatura (hipotética)
# Ajusta esta función según la relación lineal entre voltaje y temperatura
def voltaje_a_temperatura(voltaje_mV):
    return (voltaje_mV - 500) / 10.0

# Calcula la variación de temperatura (ΔT) en grados Celsius
delta_T = voltaje_a_temperatura(voltaje_mV) - voltaje_a_temperatura(voltaje_mV[-1])

# Calcula la derivada dV/dt numéricamente
delta_tiempo = np.diff(tiempo_ms)
derivada_voltaje = np.diff(voltaje_mV) / delta_tiempo

# Calcula k = dV/dt / ΔT
k_values = derivada_voltaje / delta_T[:-1]

# Gráfica para visualizar los resultados
plt.plot(tiempo_ms[1:], k_values, label='Valores de k')
plt.xlabel('Tiempo (ms)')
plt.ylabel('k')
plt.title('Variación de k con el tiempo')
plt.legend()
plt.show()

# Calcula el promedio de los valores de k
k_promedio = np.mean(k_values)
print(f'Valor promedio de k: {k_promedio}')
