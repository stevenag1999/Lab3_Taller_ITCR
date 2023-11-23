Para calcular la tasa de muestreo efectiva (Sampling Rate) y el jitter, puedes seguir los siguientes pasos:

### Tasa de Muestreo Efectiva:

La tasa de muestreo efectiva se refiere a la cantidad real de muestras que se toman por unidad de tiempo. En este caso, el Timer1 está configurado para generar interrupciones cada 200 microsegundos (5,000 Hz). Puedes medir el tiempo entre las interrupciones para obtener la tasa de muestreo efectiva. Puedes hacer esto utilizando un contador en la interrupción del Timer1 y luego calcular:

$ \[ \text{Tasa de Muestreo Efectiva} = \frac{1}{\text{Tiempo promedio entre interrupciones}} \] $

### Jitter:

El jitter se refiere a la variabilidad en el intervalo de tiempo entre las muestras. Puedes medir el jitter observando las variaciones en el tiempo entre interrupciones consecutivas. Puedes calcular el jitter como la desviación estándar de los intervalos de tiempo. En pseudocódigo:



