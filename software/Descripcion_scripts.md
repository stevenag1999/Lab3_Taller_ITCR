### Script Arduino y control de tasa de muestreo

Este código Arduino se centra en el control de canales y la configuración de escalas mediante un multiplexor (MUX) para un sistema de adquisición de datos analógicos. La variable cant_canales indica cuántos canales están activos, mientras que ch1 y ch2 representan el estado de dos canales. Se utiliza un array mux_pins para almacenar los pines A, B y C del MUX.

La configuración inicial incluye la inicialización del puerto serial y la configuración del convertidor analógico a digital (ADC). Se destaca la utilización del Timer1 para establecer una tasa de muestreo precisa. Este Timer1 opera en modo CTC (Clear Timer on Compare Match) y genera interrupciones a una frecuencia de 5000 Hz, logrando una tasa de muestreo de 0.2 ms.

En el bucle principal, se recibe comandos desde la computadora a través del puerto serial, interpretando los bits para determinar los estados de los canales y la escala seleccionada. La función configurarMUX se encarga de ajustar el MUX según la escala seleccionada.

La gestión de los canales y el ADC se realiza en el bucle principal, donde se activa o desactiva el ADC en función de la cantidad de canales y su estado. La interrupción del Timer1 se utiliza para indicar cuando el ADC está listo para realizar una nueva conversión.

### Test arduino

El script del test simula la configuración de un multiplexor (MUX) de 8 entradas mediante tres pines virtuales A, B, y C. El bucle de prueba cambia la configuración del MUX a través de combinaciones de 0 y 1 en estos pines y espera brevemente para simular la frecuencia de muestreo de 5000 Hz. En cada iteración, imprime la configuración actual y el estado del MUX, lo que permite verificar que la salida del MUX cambia según las combinaciones de las entradas A, B, y C. Este enfoque proporciona una simulación simple y efectiva para validar el comportamiento del MUX en condiciones de prueba.

![Captura desde 2023-11-23 03-20-47](https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/92649989/72be9a2c-f4f3-48e8-b486-856f3db65f71)

