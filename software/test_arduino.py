import time

# Pines simulados A, B, C del MUX
mux_pins = [False, False, False]  # Inicialmente, todos los pines están en LOW

def configurar_mux(config):
    for i in range(3):
        mux_pins[i] = (config & (1 << i)) != 0

# Configuraciones de prueba
configuraciones_prueba = [0b000, 0b001, 0b010, 0b011, 0b100, 0b101, 0b110, 0b111]

# Simulación cambiando las configuraciones
for config in configuraciones_prueba:
    configurar_mux(config)
    time.sleep(0.0002)  # Espera para simular la frecuencia de muestreo de 5000 Hz
    print(f"Configuración del MUX: {config}, Salida del MUX: {mux_pins}")
