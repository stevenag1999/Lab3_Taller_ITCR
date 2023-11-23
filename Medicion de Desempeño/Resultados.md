
### Tasa de Muestreo Efectiva:

La tasa de muestreo efectiva se refiere a la cantidad real de muestras que se toman por unidad de tiempo. En este caso, el Timer1 está configurado para generar interrupciones cada 0.2 ms (5,000 Hz). Puedes medir el tiempo entre las interrupciones para obtener la tasa de muestreo efectiva. Puedes hacer esto utilizando un contador en la interrupción del Timer1 y luego calcular:


![ggggg](https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/92649989/7bf5956c-cd9b-4c25-90c7-43d6bc859633)


El resultado al medir los valores de Ts fue de alrededor de 5.5ms.

### Jitter:

El jitter se refiere a la variabilidad en el intervalo de tiempo entre las muestras. Puedes medir el jitter observando las variaciones en el tiempo entre interrupciones consecutivas. Puedes calcular el jitter como la desviación estándar de los intervalos de tiempo. En pseudocódigo:



