### Configurando los BITS DE REGISTRO

<img width="728" alt="Captura de pantalla 2023-11-22 a la(s) 20 07 00" src="https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/81390103/c6050cf7-86b5-468e-9645-3c244d7bee21">

El registro que nos interesa de primera manera entra es el ADCSRA(ADC Setting Register A) , como se muestra en la imagen el ARDUINO consta de 8 bits y cada bit tiene un significado tiene un nombre. De esos bits el que nos interesa seria el  ADEN(ADC Enable Bit).

```
 // Configuración General del ADC
    //->Registro ADMUX
    ADMUX |= (1 << REFS0); //Voltaje de referencia 5V (REFS1 ya está en 0)
    ADMUX |= (1 << ADLAR); //Ajuste Izquierdo
    //->Registro ADCSRA
    ADCSRA |= (1 << ADATE); // Free-running
    ADCSRA |= (1 << ADIE); // habilitar interrupciones del ADC
  
    ADCSRA &= ~(1 << ADPS2) & ~(1 << ADPS1) & ~(1 << ADPS0);    //Prescaler en 128
}
```

### Interrupciones

Para el desarrollo del proyecto es importante tener el control de las Interrupciones del ARDUINO. Ya que necesitamos que detenga el funcionamiento del Loop Principal y pase a la función que necesitamos. En el caso del proyecto se ocupa para el conteo de pulsos y en el caso del ARDUINO contamos con Comparador Analogo que tiene un interrupción que se activa cuando detecta que su señal sobrepasa el voltaje de referencia.

```
ISR(ANALOG_COMP_vect)
{
counter++
}

```

<img width="775" alt="Captura de pantalla 2023-11-22 a la(s) 20 17 35" src="https://github.com/stevenag1999/Lab3_Taller_ITCR/assets/81390103/383d6c79-96a8-427a-b3e6-a49ab34c74db">
