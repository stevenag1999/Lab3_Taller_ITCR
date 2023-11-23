# Script Arduino y control de tasa de muestreo

Este código Arduino se centra en el control de canales y la configuración de escalas mediante un multiplexor (MUX) para un sistema de adquisición de datos analógicos. La variable cant_canales indica cuántos canales están activos, mientras que ch1 y ch2 representan el estado de dos canales. Se utiliza un array mux_pins para almacenar los pines A, B y C del MUX.

La configuración inicial incluye la inicialización del puerto serial y la configuración del convertidor analógico a digital (ADC). Se destaca la utilización del Timer1 para establecer una tasa de muestreo precisa. Este Timer1 opera en modo CTC (Clear Timer on Compare Match) y genera interrupciones a una frecuencia de 5000 Hz, logrando una tasa de muestreo de 0.2 ms.

En el bucle principal, se recibe comandos desde la computadora a través del puerto serial, interpretando los bits para determinar los estados de los canales y la escala seleccionada. La función configurarMUX se encarga de ajustar el MUX según la escala seleccionada.

La gestión de los canales y el ADC se realiza en el bucle principal, donde se activa o desactiva el ADC en función de la cantidad de canales y su estado. La interrupción del Timer1 se utiliza para indicar cuando el ADC está listo para realizar una nueva conversión.

### Test arduino

El script del test simula la configuración de un multiplexor (MUX) de 8 entradas mediante tres pines virtuales A, B, y C. El bucle de prueba cambia la configuración del MUX a través de combinaciones de 0 y 1 en estos pines y espera brevemente para simular la frecuencia de muestreo de 5000 Hz. En cada iteración, imprime la configuración actual y el estado del MUX, lo que permite verificar que la salida del MUX cambia según las combinaciones de las entradas A, B, y C. Este enfoque proporciona una simulación simple y efectiva para validar el comportamiento del MUX en condiciones de prueba.

![Captura desde 2023-11-23 03-20-47](https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/92649989/72be9a2c-f4f3-48e8-b486-856f3db65f71)

# GUI

Esta GUI tiene como objetivo principal la adquisición y visualización en tiempo real de datos provenientes de dos canales diferentes a través de una comunicación serial con un dispositivo Arduino. Secciones:

### Librerías ###
Se utilizan las librerías `tkinter` para la interfaz gráfica, `matplotlib` para la visualización de gráficos, `serial` para la comunicación serial con Arduino, `time` para gestionar retardos, y `csv` para la manipulación de archivos CSV.

### Comunicación Serial ###
Se establece y configura la comunicación serial con el Arduino, utilizando el puerto `seleccionado en momento` a una velocidad de 115200 baudios. También se incluye un procedimiento para resetear el Arduino antes de la adquisición de datos.

### Funciones de los Botones ###
- **adquirir_datos(canalP):** Función para la adquisición de datos de uno o ambos canales, según el parámetro canalP. Los datos adquiridos se almacenan en listas (`datos_canal1` y `datos_canal2`).

- **graficar_datos():** Función para actualizar la gráfica en tiempo real. Dependiendo de las opciones seleccionadas en la interfaz gráfica, grafica los datos del Canal 1, Canal 2 o ambos.

- **almacenar_datos():** Función para almacenar los datos de la sesión en un archivo de texto (`datos.txt`). Recopila información como el autor, fecha, magnitudes físicas y escalas, y los datos de los canales seleccionados. Sin embargo para efectos de este desarrollo también se llevó acabo la modificacion para que lo datos se generaran en un csv para post análisis requerido. 

- **cargar_datos():** Función para cargar y graficar datos previamente almacenados en el archivo `datos.txt`.

- **determinar_comando():** Función que determina el comando a enviar al Arduino según las opciones seleccionadas en la interfaz, como canales activados y escalas.

- **actualizar_informacion():** Función para actualizar la información (escalas) que se enviará al Arduino según las opciones seleccionadas en la interfaz.

### Configuración Inicial y Variables Auxiliares ###
Se establecen variables iniciales y auxiliares, como el comando de configuración, listas para almacenar datos de los canales, y variables para controlar la activación de los canales.

### Ventanas y Diseño de la GUI ###
Se configuran los elementos de la interfaz gráfica, incluyendo etiquetas, botones, entradas de texto y checkboxes. También se crea un espacio de graficación utilizando `matplotlib` y se define el diseño general de la ventana principal.

La GUI permite al usuario configurar parámetros, activar/desactivar canales, visualizar datos en tiempo real, almacenar y cargar sesiones de datos. Además, facilita la interacción con el dispositivo Arduino a través de la comunicación serial.
