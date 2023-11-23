Las siguiente imagenes muestran los circuitos utilizados para este proyecto, se subdividen en bloques para lograr una mejor visualizacion:

### 1) BLoque 1 Fase diferencial.

Esta fase hace la diferenciacion de la salida de la termocupla, el circuito es un amplificador operacional diferencial con 4 pares de resistencias de realimentación R1-R4 y dos resistencias R5-R6 para    controlar el ganancial del circuito.

En un amplificador operacional diferencial, el voltaje en el pin de entrada no inversora (V1) se compara con el voltaje en el pin de entrada inversora (V2). La diferencia de voltaje entre estos dos pines es lo que el amplificador operacional diferencial amplifica.

El circuito está configurado de tal manera que cuando el voltaje en V1 es mayor que el voltaje en V2, la salida del amplificador operacional diferencial (S1) será positiva, lo que indicará una conexión entre las terminales pos y neg del amplificador operacional diferencial.



![image](https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/79070879/a6003851-1de8-4e4b-80d7-2029be0c9855)


Para ya luego entrar a la fase de escalamiento que ahi es donde entra a trabajar un multiplexor que va a ayudar a seleccionar los valores de resistencia optimos para la ganancia del bloque.

![image](https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/79070879/fb6d9ec8-f0e1-455f-b818-3d7be9f73a67)


Ya con esto y el arduino controlando las patillas de seleccion del mux, permite escalar la ganancia de esta etapa.

En la etapa post amplificación se trabaja para preservar la integridad de la señal, permitiendo una transmisión y procesamiento más preciso y fiable de la información analógica.

![image](https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/79070879/a9959931-2b76-4a68-a820-f769623d25c0)

Siendo como final la etapa de aislamiento para lograr mantener por fuera tensiones dañinas del sistema del sensor.


![image](https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/79070879/8d2cfe97-894e-4796-8d44-d7542b787050)

Junto con el optoacoplador 4n25, nos da la facilidad de control sin requerir un circuito muy complejo.


Por ultimo, dando lugar al siguiente diagrama de bloques para todo el circuito.

![image](https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/79070879/13602311-e4c4-4a51-a628-2005e9acfd5a)










