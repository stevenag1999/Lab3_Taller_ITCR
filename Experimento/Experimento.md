## Pruebas de temperatura en el laboratorio

Se hizo una recolección de datos sobre los registros de la medición de temperatura cuando se introdujo la termocupla en una botella con agua caliente, se mantuvo registrando datos hasta que el agua disminuyera considerablemente la temperatura, los datos se guardaron en archivo csv. Se adaptó el script para unicamente 
para esta prueba con el fin de que el rango de registro de datos fuera mas largo.

Se utilizó el nuevo modelo DAS el cual se implementó un MUX de 8bits controlado por la señal del arduino para controlar la escala de los equipos 

![WhatsApp Image 2023-11-18 at 17 15 03](https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/92649989/781771db-ace9-4ca8-9f45-7d0f769cd0d4)

## Constante k

Para determinar la constante k de la ecuación diferencial dv/dt = k(T - T) , puedes seguir estos pasos:

1. Obtén las lecturas de la termocupla en milivoltios y sus tiempos correspondientes.
2. Calcula la variación de temperatura Delta T en grados Celsius en función de las lecturas de milivoltios. Puedes usar la relación conocida entre la temperatura y el voltaje de la termocupla. Supongamos que hay una relación lineal entre el voltaje y la temperatura.
3. Calcula la derivada dV/dt en función del tiempo. Puedes usar las lecturas de milivoltios y sus tiempos para estimar esta derivada numéricamente utilizando diferencias finitas.
4. Estima la constante k al dividir dV/dt por Delta T.
5. Calcula el promedio de los valores de k obtenidos a lo largo del registro de la termocupla.

### Pruebas en canal 1

![image](https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/92649989/9f355a96-8f4c-4ddf-bfe3-1629f53faf11)
