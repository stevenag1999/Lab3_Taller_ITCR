# Lab3_Taller_ITCR
Proyecto Final: Diseño de un sistema de adquisición y análisis de datos. Parte III

## Enunciado
En este último trabajo, se integrará ambos sistemas elaborados en los proyectos pasados: métodos de
análisis de señales y el sistema de adquisición de datos (hardware y software).

### 3.1. Medición de desempeño
1. Se requiere medir la tasa de muestreo efectiva y así como el jitter, si es posible, tanto en la configuración del sistema con uno y dos canales activos. Recomendación: levantar un pulso en un pin del
microcontrolador previo al hacer una lectura por el ADC y bajarlo cuando entra en modo de reposo.
La frecuencia del pulso indica la tasa de muestreo, y el tiempo en alto el tiempo que toma la tarea de
conversión del ADC y comunicación del UART.
2. Cuantificación de error estático y dinámico de las mediciones tomadas por el sistema. Recomendación:
Tomar muestras de señales DC y AC cuyas magnitudes y anchos de banda sean conocidos y medidos
con instrumentos de mayor precisión por ejemplo: osciloscopio y multímetro.

### 3.2. Análisis de datos
1. Con base a la ley de Newton de temperatura dT
dt = k(T −T∞). Proponga un experimento de tal manera
encuentre de manera experimental la constante k al momento de enfría un vaso de agua caliente de
200ml a temperatura ambiente. Puede ajustar la tasa de muestreo del sistema a una apropiada que le
convenga. El experimento debe repetir al menos 3 veces y cada medición debe ser almacenada en la
base de datos. Por medio de un script externo elabore los cálculos necesarios para estimar k.

### 3.3. Documentación
1. Elabore una nota divulgativa que hable del proceso de diseño y del experimento propuesto acompañado
de fotografía y gráficos. Posibles medios: medium, hackster.io, youtube, etc.

### 3.4. Presentación de los resultados
1. Se deberá almacenar el código fuente del software que elaboré (microcontrolador y software del ordenador) en el repositorio del proyecto.
2. Deberá documentar el diseño final del circuito del hardware con las mejoras. Se debe tener el esquemático segmentado por bloques.
3. La nota divulgativa debe enlazar el repositorio de Github
