# Ejercicios de funciones

Vamos a integrar todo lo que hemos aprendido sobre funciones y módulos y vamos a crear nuestro propio módulo de funciones en Python. 

Para ello, vamos a tomar como base algunos de los ejercicios realizados durante la unidad UT3 y vamos a convertirlos en funciones. Estas funciones las agruparemos en un módulo llamado `modulo_nombre.py`, donde `nombre` será tu nombre de pila sin acentos ni caracteres extraños.

Para probar todas las funciones del módulo, crearemos un nuevo fichero llamado `test.py` que contendrá distintas llamadas a todas las funciones del módulo. Conviene que incluyas comentarios explicando las distintas llamadas.

A continuación, se enumeran los ejercicios que se van a transformar en funciones con las indicaciones oportunas. Se recomienda que se copien los ejercicios y se modifiquen para transformarlos en funciones.

*Nota: cabe distinguir cuando en las funciones se dice que "devuelven" algo o que "imprimen".*

## Ejercicios para practicar condicionales

**Ejercicio 1**

Función `mayor(n1, n2)` que recibe dos números *n1* y *n2* y devuelve el mayor. 

**Ejercicio 3** 

Función `es_par(n)` que recibe un número *n* y devuelve un booleano indicando si el número es par o no.

**Ejercicio 6** 

Función `es_mayusculas(cad)` que recibe la cadena *cad* y devuelve un booleano indicando si la cadena está toda en mayúsculas o no.

**Ejercicio 7** 

Función `potencia(base, exp)` que recibe dos números, la *base* y un exponente *exp* y devuelve la potencia calculada tal y como indica el ejercicio.

**Ejercicio 9** 

Función `ordena_mayor_menor(n1, n2, n3)` que recibe tres números *n1*, *n2* y *n3* y devuelve una tupla con los tres números ordenados de mayor a menor.

**Ejercicio 10** 

Función `clasifica_circunferencias(x1, y1, r1, x2, y2, r2)` que recibe como argumentos los centros *(x,y)* y radios *r* de dos circunferencias y las clasifica en uno de estos estados: exteriores, tangentes exteriores, secantes, tangentes interiores, interiores o concéntricas. *Nota: esta función no devuelve nada, simplemente imprime el tipo de circunferencias*

**Ejercicio 11** 

Función `clasifica_triangulo(a,b,c)` que recibe la longitud de los tres lados *a*, *b* y *c* de un triángulo e imprime el tipo de triángulo.

**Ejercicio 12** 

Función `es_bisiesto(anyo)` que recibe un año *anyo* y devuelve un booleano indicando si dicho año es bisiesto o no.

**Ejercicio 13** 

Función `es_fecha_correcta(dia, mes, anyo)` que recibe el *dia*, el *mes* y el *anyo* y devuelve un booleano indicando si la fecha es o no correcta.

**Ejercicio 14** 

Función `calcula_ganancias_uva(precio_kilo, kilos, tipo, tamanyo)` que recibe el precio por kilo en euros *precio_kilo*, la cantidad de kilos *kilos*, el tipo de uva *tipo* y el tamaño de la uva *tamanyo* y devuelve las ganancias del vinicultor en euros.

**Ejercicio 15** 

Función `costes_viaje(n)` que recibe el número de alumnos *n* y devuelve una tupla con el coste para el alumno y el coste total del autobús.

**Ejercicio 16** 

Función `coste_llamada(tiempo, es_domingo, turno)` que recibe el tiempo que dura una llamada en minutos *tiempo*, una cadena 'S' o 'N' indicando si la llamada se ha hecho en domingo o no *es_domingo* y una cadena *turno* que indica si es de mañana o de tarde. La función debe devolver el coste de la llamada.


**Ejercicio 18** 

Función `dia_escrito(n)` que recibe un número de día *n* (del 1 al 7) y devuelve el día correspondiente escrito con letras, por ejemplo, *lunes*.

**Ejercicio 19** 

Función `num_dias_mes(mes)` que recibe un número de *mes* (entre 1 y 12) y devuelve el número de días que tiene dicho mes.

**Ejercicio 20**

Función `calcula_coste_transporte(peso, zona)` que recibe el *peso* en gramos y la *zona* (del 1 al 5) y devuelve el coste de transportar el paquete.

## Ejercicios para practicar bucles

**Ejercicio 1**

Función `factorial(num)` que recibe un número entero *num* y devuelve su factorial.

**Ejercicio 5**

Función `pares_entre(num1, num2)` que recibe dos números, siendo *num1* menor que *num2*, e imprime todos los pares entre ambos números incluidos.

**Ejercicio 6**

Función `tabla_multiplicar(n)` que recibe un número entero *n* e imprime la tabla de multiplicar de ese número.

**Ejercicio 10**

Función `adivina_numero(intentos)` que recibe el número de *intentos* que tienes para tratar de adivinar un número del 1 al 100.

**Ejercicio 11**

Función `es_primo(n)` que recibe un número entero *n* y devuelve un booleano indicando si el número es o no primo.

**Ejercicio 20**

Función `primeros_primos(N)` que recibe la cantidad de números primos a mostrar *N* e imprime los N primeros números primos.
