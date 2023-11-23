
### Tasa de Muestreo Efectiva:

La tasa de muestreo efectiva se refiere a la cantidad real de muestras que se toman por unidad de tiempo. En este caso, el Timer1 está configurado para generar interrupciones cada 0.2 ms (5,000 Hz). Puedes medir el tiempo entre las interrupciones para obtener la tasa de muestreo efectiva. Puedes hacer esto utilizando un contador en la interrupción del Timer1 y luego calcular:

![WhatsApp Image 2023-11-23 at 16 57 48](https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/92649989/a583420d-97cb-405e-a60b-c9883237117a)


El resultado al medir los valores de Ts fue de alrededor de 20ms.

### Jitter:

El jitter se refiere a la variabilidad en el intervalo de tiempo entre las muestras. Puedes medir el jitter observando las variaciones en el tiempo entre interrupciones consecutivas. Puedes calcular el jitter como la desviación estándar de los intervalos de tiempo. En pseudocódigo:



