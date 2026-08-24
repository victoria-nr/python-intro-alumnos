# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

La clave aquí es identificar qué dato debe ir en la clave, cuál en el valor y cómo se actualizan contadores o agrupaciones.

### Ejercicio 01

Idea clave: Usa diccionario['clave'] acceso; estructura datos relacionados como atributos.

??? example "Ver solución"
    ```python
    # Ejercicio 1
    '''Crea un diccionario que almacene los datos de una persona: 
    nombre, edad y ciudad. Dales los valores que quieras. 
    Luego, imprime cada uno de los valores por separado.'''
    
    persona = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
    print(persona['nombre'])
    print(persona['edad'])
    print(persona['ciudad'])
    ```

### Ejercicio 02

Idea clave: Asignación directa diccionario['clave']=valor crea claves nuevas.

??? example "Ver solución"
    ```python
    # Ejercicio 2
    '''Dado el siguiente diccionario:
    productos = {'manzana': 1.5, 'pan': 0.8, 'leche': 1.2}
    Agrega un nuevo producto llamado `'huevos'` con un valor de `2.0`. Luego imprime el diccionario actualizado.'''
    
    productos = {'manzana': 1.5, 'pan': 0.8, 'leche': 1.2}
    productos['huevos'] = 2.0
    print(productos)
    ```

### Ejercicio 03

Idea clave: 'clave' in diccionario devuelve booleano; evita KeyError.

??? example "Ver solución"
    ```python
    # Ejercicio 3
    '''Dado el diccionario anterior, muestra por pantalla si el producto
     `'pan'` está en el diccionario. Haz lo mismo con `'queso'`.'''
    
    productos = {'manzana': 1.5, 'pan': 0.8, 'leche': 1.2}
    print("Está pan en el diccionario?: ", 'pan' in productos)
    print("Está queso en el diccionario?: ",'queso' in productos)
    ```

### Ejercicio 04

Idea clave: .get(clave, defecto) evita KeyError cuando clave podría faltar.

??? example "Ver solución"
    ```python
    # Ejercicio 4
    '''Escribe un programa que solicite al usuario una palabra y devuelva su significado usando el siguiente diccionario:
    
    diccionario = {
        'python': 'Lenguaje de programación',
        'algoritmo': 'Conjunto de instrucciones',
        'variable': 'Espacio de memoria para almacenar datos'
    }
    
    *Nota: Debes controlar correctamente si el usuario introduce una palabra que no existe.*'''
    
    diccionario = {
        'python': 'Lenguaje de programación',
        'algoritmo': 'Conjunto de instrucciones',
        'variable': 'Espacio de memoria para almacenar datos'
    }
    palabra = input("Introduce una palabra: ")
    print(diccionario.get(palabra, "Palabra no encontrada"))
    ```

### Ejercicio 05

Idea clave: Bucle pide clave/valor; asignación es patrón de construcción común.

??? example "Ver solución"
    ```python
    # Ejercicio 5
    '''Crea un diccionario vacío. Luego, pide al usuario que introduzca 
    por teclado 3 pares clave-valor para rellenarlo. 
    Finalmente, imprime el diccionario.'''
    mi_dic = {}
    for _ in range(3):
        clave = input("Introduce una clave: ")
        valor = input("Introduce un valor: ")
        mi_dic[clave] = valor
    print(mi_dic)
    ```

### Ejercicio 06

Idea clave: del diccionario[clave] elimina; no confundir con pop() que devuelve.

??? example "Ver solución"
    ```python
    # Ejercicio 6
    '''Dado el siguiente diccionario:
    
    puntuaciones = {'Juan': 85, 'Ana': 92, 'Luis': 78}
    
    Actualiza la puntuación de `'Luis'` a 88. Luego elimina a `'Juan'` del diccionario y muestra el resultado final.'''
    
    puntuaciones = {'Juan': 85, 'Ana': 92, 'Luis': 78}
    puntuaciones['Luis'] = 88
    del puntuaciones['Juan']
    print(puntuaciones)
    ```

### Ejercicio 07

Idea clave: if clave not in dic es patrón básico; alternativa .get(clave, 0)+1.

??? example "Ver solución"
    ```python
    # Ejercicio 7
    '''Escribe un programa que cuente cuántas veces aparece cada letra 
    en una palabra introducida por el usuario. Usa un diccionario para
     almacenar el resultado. Ejemplo: en la palabra 'amiga' la 'a' 
     aparece 2 veces, la 'm' 1 vez, la 'i' 1 vez y la 'g' 1 vez.'''
    
    palabra = input("Introduce una palabra: ")
    conteo = {}
    
    for letra in palabra:
        if letra not in conteo:
            conteo[letra]=1
        else:
            conteo[letra]+=1
    print(conteo)
    
    #forma más compacta
    #for letra in palabra:
    #    conteo[letra] = conteo.get(letra, 0) + 1
    #print(conteo)
    ```

### Ejercicio 08

Idea clave: min(diccionario, key=diccionario.get) avanzado; bucle manual es claro.

??? example "Ver solución"
    ```python
    # Ejercicio 8
    '''Dado un diccionario con nombres de personas como claves y su edad
     como valores, muestra el nombre de la persona más joven. Crea tú mismo
       el diccionario con al menos 3 pares clave-valor.'''
    
    personas = {'Juan': 30, 'Ana': 25, 'Luis': 28}
    
    
    min_persona = None
    min_edad = None
    
    # Recorremos el diccionario
    for nombre in personas:
        edad = personas[nombre]
        if min_edad is None or edad < min_edad:
            min_edad = edad
            min_persona = nombre
    
    # Mostramos el resultado
    print("La persona más joven es", min_persona, "con", min_edad, "años.")
    
    #solución avanzada
    #joven = min(personas, key=personas.get)
    #print(f"La persona más joven es {joven} con {personas[joven]} años.")
    ```

### Ejercicio 09

Idea clave: .split() divide; diccionario acumula conteos; .lower() normaliza.

??? example "Ver solución"
    ```python
    # Ejercicio 9
    '''Escribe un programa que lea 5 frases introducidas por el usuario
     y almacene en un diccionario cuántas veces aparece cada palabra. 
     Ignora mayúsculas/minúsculas.'''
    
    conteo = {}
    for _ in range(5):
        frase = input("Introduce una frase: ")
        for palabra in frase.lower().split():
            if palabra not in conteo:
                conteo[palabra]=1
            else:
                conteo[palabra]+=1
    
            #forma más avanzada de hacer lo anterior
            #conteo[palabra] = conteo.get(palabra, 0) + 1
    print(conteo)
    ```

### Ejercicio 10

Idea clave: in diccionario verifica; multiplicación calcula subtotal y total.

??? example "Ver solución"
    ```python
    # Ejercicio 10
    '''Dado un diccionario con productos y su precio, escribe un programa 
    que calcule el precio total de una compra solicitando al usuario qué 
    productos desea y en qué cantidad mediante un bucle. El bucle terminará
    cuando el usuario introduzca la palabra 'FIN'. Cuando el usuario escoja
    un producto, imprime el desglose del producto, la cantidad, el precio
    por unidad y precio total. Al finalizar, imprime el total de la compra.
    Crea tú mismo el diccionario con al menos 4 pares producto-precio.'''
    
    productos = {'pan': 0.8, 'leche': 1.2, 'huevos': 2.0, 'galletas': 2.5}
    total = 0
    while True:
        print(productos)
        prod = input("Escoge un producto (FIN para terminar): ")
        if prod == "FIN":
            break
        if prod in productos:
            cantidad = int(input(f"Cantidad de {prod}: "))
            subtotal = cantidad * productos[prod]
            total += subtotal
            print(f"{prod}: {cantidad} x {productos[prod]} = {subtotal:.2f}€")
        else:
            print("Producto no encontrado")
    print(f"Total: {total:.2f}€")
    ```

### Ejercicio 11

Idea clave: Comprensión {v:0 for v in vocales} inicializa; .lower() normaliza.

??? example "Ver solución"
    ```python
    # Ejercicio 11
    '''Dado un texto introducido por teclado, muestra cuántas veces aparece
     cada vocal usando un diccionario. Usa una sola pasada sobre el texto.'''
    
    texto = input("Introduce un texto: ")
    vocales = 'aeiou'
    conteo = {v: 0 for v in vocales}
    for letra in texto.lower():
        if letra in conteo:
            conteo[letra] += 1
    print(conteo)
    ```

### Ejercicio 12

Idea clave: Estructura anidada [clave1][clave2] organiza complejos; .items() itera.

??? example "Ver solución"
    ```python
    # Ejercicio 12
    '''Usa un diccionario para almacenar los datos de varios estudiantes. 
    Para cada uno guarda su nombre como clave y como valor otro diccionario
     con `'nota1'`, `'nota2'`, `'nota3'`. Crea al menos 3 estudiantes. 
     Luego, calcula la nota media de cada alumno.'''
    
    estudiantes = {
        'Ana': {'nota1': 7, 'nota2': 8, 'nota3': 9},
        'Luis': {'nota1': 6, 'nota2': 7, 'nota3': 8},
        'Marta': {'nota1': 9, 'nota2': 8, 'nota3': 10}
    }
    for nombre, notas in estudiantes.items():
        media = sum(notas.values()) / len(notas)
        print(f"{nombre}: Nota media = {media:.2f}")
    ```
