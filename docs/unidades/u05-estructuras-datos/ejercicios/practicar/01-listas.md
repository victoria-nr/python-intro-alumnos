# Ejercicios para practicar listas


**Ejercicio 1**

Realiza un programa que defina una lista llamada `lista_numeros` y la inicialice con 10 ceros. A continuación, recorre la lista y asigna a cada elemento un valor aleatorio (del 1 al 10). Posteriormente muestra en pantalla cada elemento de la lista junto con su cuadrado y su cubo. 
*Pista:* recuerda que puedes generar números aleatorios con la función `randint` del módulo `random`

**Ejercicio 2** 

Crea una lista de 5 elementos donde cada elemento sea una cadena que se pide por el teclado. Copia los elementos de la lista en otra lista, pero en orden inverso, y muestra los elementos invertidos por la pantalla. 

**Ejercicio 3** 

Realiza un programa que lea por teclado las 5 notas obtenidas por un alumno. Debes controlar que las notas estén comprendidas entre 0 y 10 y pueden contener decimales. A continuación, debe mostrar todas las notas indicando su orden, es decir, “Nota 1: 5.5, Nota 2: 6, ...”, debe mostrar también la nota media, la nota más alta que ha sacado y la menor.

**Ejercicio 4** 

Realiza un programa que pida números enteros y los añada a una lista hasta que llegue a 10 elementos o se introduzca un número negativo. A continuación, se debe imprimir la lista. 

**Ejercicio 5** 

Hacer un programa que inicialice una lista de 10 números con valores aleatorios, y posteriormente ordene los elementos de menor a mayor en la misma lista utilizando una función concreta. Deberá mostrarse la lista original y la ordenada. 

**Ejercicio 6** 

Crea un programa que pida un número de mes al usuario entre 1 y 12 (por ejemplo, el 4, que sería abril) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas para guardar los días de los meses y los nombres. Para simplificarlo vamos a suponer que febrero tiene 28 días. Controla con un bucle while que el número de mes esté entre 1 y 12. 

**Ejercicio 7** 

Realiza un programa que cree 2 listas de cinco enteros cada una, y pida sus valores por teclado. A continuación, debe unir las 2 listas en una lista resultado e imprimir sus valores. 

**Ejercicio 8** 

Queremos guardar los nombres y las edades de los alumnos de un curso. Para ello utilizarás dos listas, una para nombres y otra para edades. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos: 

- Todos los alumnos mayores de edad (su nombre y edad). 
- Los alumnos mayores, es decir, los que tienen más edad (su nombre y edad). 

**Ejercicio 9** 

Queremos guardar la temperatura mínima y máxima de los 7 días de la semana pasada en dos listas. Para ello pide las temperaturas por teclado. Realiza un programa que dé la siguiente información: 

- Calcule la temperatura media de cada día. 

- Calcule los días con menos temperatura. 

- Lea una temperatura por teclado y se muestre los días cuya temperatura máxima coincide con ella. Si no existe ningún día se mostrará un mensaje informativo. 

*Nota: Como implementación básica, nos podemos referir a los días por su número (por ejemplo, el día 1 el lunes, el 2 es martes, etc). Si queréis mejorar el programa, nos referiremos por su nombre (lunes, martes, etc.)*

**Ejercicio 10** 

Elabora un pequeño programa que gestionará una lista de la compra. El programa mostrará un menú con las opciones disponibles. Las opciones son las siguientes: 

```python
#Mostrar menu 
print("\nGestión de Lista de la Compra") 
print("1. Mostrar la lista") 
print("2. Añadir elementos a la lista") 
print("3. Borrar elementos de la lista") 
print("4. Contar elementos de la lista") 
print("5. Añadir una lista de elementos a la ya existente") 
print("6. Borrar toda la lista") 
print("7. Salir") 
```

Se trata de implementar cada una de las acciones. La opción 2 añade un solo elemento a la lista, por ejemplo, *leche*, mientras que la opción 5 es capaz de añadir varios elementos a la lista de una vez, escritos separados por coma, por ejemplo, *cereales,jamón,agua* 


**Ejercicio 11** 

Amplía el ejercicio anterior para que incluya los precios y las cantidades de cada elemento. En lugar de gestionar solo una lista con los nombres de los productos, añade dos listas adicionales: 

- **Una lista de precios**, donde cada precio corresponde al producto en la misma posición de la lista de productos. 

- **Una lista de cantidades**, que indica cuántas unidades de cada producto se quiere comprar. 

El programa debe incluir las siguientes funcionalidades: 

1. Crear una nueva lista de la compra (vaciando los datos anteriores). 
2. Añadir un producto** con su precio y cantidad. 
3. Eliminar un producto de la lista. 
4. Contar los productos en la lista. 
5. Añadir una lista de productos con sus precios y cantidades. 
6. Borrar toda la lista. 
7. Ordenar la lista de la compra por precio o cantidad. 
8. Calcular el importe total de la compra, multiplicando la cantidad de cada producto por su 9. precio y sumando los resultados. 
9. Mostrar los productos de la lista, es decir, cada producto con sus unidades y precio 
10. Salir 

**Ejercicio 12** 

Reescribe el ejercicio 10 para que utilice funciones. 


**Ejercicio 13** 

Reescribe el ejercicio 11 para que utilice funciones.
