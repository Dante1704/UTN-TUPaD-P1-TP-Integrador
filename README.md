<p align="center">
  <img src="assets/logo-utn.png" alt="Logo UTN" width="100%"/>
</p>
<p align="center">
  <strong>Universidad Tecnológica Nacional</strong>
</p>

# Trabajo Práctico Integrador - Programación I

## Marco teórico

Cuando uno empieza a programar, enseguida aparecen dos cosas: buscar datos y ordenarlos. A veces no se nota, pero están en casi todo. Desde encontrar un nombre en una lista, hasta mostrar resultados ordenados de menor a mayor. La verdad que entender estos procesos ayuda un montón a pensar cómo se trabaja con datos en general.
Un algoritmo es un conjunto de pasos que sirven para resolver un problema. En el caso de los algoritmos de búsqueda, la idea es encontrar un dato específico dentro de una estructura como una lista. El más simple de todos es la búsqueda lineal, que va comparando uno por uno. Sirve siempre, pero si hay muchos datos puede volverse lenta. Se dice que su complejidad es O(n), lo que significa que el tiempo que tarda depende de cuántos elementos haya. Donde O(n) es el tiempo de ejecución que crece proporcionalmente al tamaño de los datos, por ejemplo, si tenemos una lista con 100 elementos, el algoritmo puede hacer hasta 100 pasos, si tuviera 1.000 haría 1.000 etc.

Después hay otra forma que es más rápida, pero tiene una condición: que los datos ya estén ordenados. Se llama búsqueda binaria, y lo que hace es dividir la lista a la mitad cada vez, descartando la parte que no sirve. Así encuentra el valor mucho más rápido, con complejidad es O (log n), aunque no se puede aplicar, en cualquier caso. Es necesario aclarar que O (log n) es el tiempo logarítmico que crece muy lentamente, aunque aumente la cantidad de datos. Es logarítmico porque el número de pasos crece como el logaritmo de n en base 2, como en el caso de la búsqueda binaria.

Justamente por eso ordenar se vuelve tan importante. Hay muchos algoritmos que hacen esto, y uno de los más usados es el quicksort. Fue inventado por Tony Hoare, tomando tomando un problema de ordenamiento y lo descompone en subproblemas, que a su vez se descomponen en más subproblemas, trabajando eligiendo un valor pivote. Esto se logra mediante programación recursiva, donde la programación recursiva es una técnica que consiste en que una función se llame a si misma para resolver un problema hasta lograr el caso base. Luego separa los datos menores a un lado y los mayores al otro. Después repite el mismo proceso con esos dos grupos. Es como dividir el problema en partes más chicas.

Cabe destacar que quicksort como fue introducido por Tony inicialmente no fue perfecto, pero a medida que pasaron los años muchas personas colaboraron para ajustar y resolver las debilidades.

Algunas personas, ingenieros y programadores, han argumentado que cuando las particiones son lo suficientemente pequeñas, este tipo de ordenamiento resulta ser menos eficiente que usar otros metodos de ordenamiento. 

Quicksort suele ser eficiente y rápido en la mayoría de los casos, aunque hay situaciones donde no rinde tanto. Igual, en general se comporta muy bien y es bastante usado en la práctica, porque además no necesita mucha memoria extra.

El peor escenario posible en el algoritmo de ordenamiento quicksort se da cuando el tiempo de ejecución crece significativamente debido a una mala elección del pivote. Este tiempo está directamente relacionado con la cantidad de elementos de entrada.

Existen distintos métodos para seleccionar el pivote y tratar de evitar ese caso desfavorable. Una opción es usar siempre el mismo elemento del conjunto (como el primero, el del medio o el último), pero esto implica el riesgo de que ese elemento sea el valor más bajo o más alto, lo que lleva a una mala partición.

Otra alternativa es calcular la mediana de todos los elementos, lo cual mejora la eficiencia pero también agrega complejidad al algoritmo.

Una solución intermedia consiste en seleccionar tres elementos del conjunto (por ejemplo, el primero, el del medio y el último) y usar como pivote el valor intermedio entre ellos. Esta técnica mejora la elección del pivote sin complicar demasiado el proceso.

En este trabajo vamos a implementar una búsqueda simple, utilizando busqueda binaria y quicksort en Python, para ver en la práctica cómo funcionan estos conceptos.


---

## Integrantes (ordenados alfabéticamente)

- **Pablo Basualdo Arcati**
- **Dante Kaddarian**

---

## Consigna

Llevar adelante una investigación práctica y aplicada sobre conceptos fundamentales y avanzados del lenguaje Python, integrando teoría, casos de uso reales, desarrollo de software y difusión de los resultados obtenidos.

---

### Estructura del proyecto
<pre>
📦 
├─ main.py                               # Script principal que ejecuta el programa
├─ README.md                             # Instrucciones y documentación del proyecto
└─ utils/                                # Módulo con funciones auxiliares
   | busqueda_binaria_iterativa.py       # Función de iteración que recorre una lista 
   |                                       dividiendola en dos partes en cada recorrido hasta 
   |                                       llegar al objetivo de busqueda
   | obtener_palabras_limpias.p          # Funciones para convertir un string en una lista
   |                                      utilizando  una expresión regular para eliminar puntos
   |                                      y comas 
   └── quicksort.py                     # Funciones de ordenamiento que recibe una lista
                                            desordenada y devuelve una lista ordenada mediante un 
                                            pivote
</pre>

---
### Presentación en video
- Docente:  **Cinthia Rigoni
- Tutor: **Martin Alejandro Garcia

### Presentación en video
Link: [Presentación](https://www.youtube.com/watch?v=EX7toJ18-Cg)

### Como Clonar y ejecutar el algoritmo
<pre>
Para clonar copiamos el siguiente link:
https://github.com/Dante1704/UTN-TUPaD-P1-TP-Integrador.git
Y abrimos una consola shell o git bash e introducimos el siguiente comando:

git clone https://github.com/Dante1704/UTN-TUPaD-P1-TP-Integrador.git

De esta forma podemos tener el repo en local, una vez realizamos este clone nos dirigimos a la función 
main.py y presionamos la "bandera" en el marco derecho superior del editor de código Visual Studio Code:
</pre>
![Bandera](assets/image.png)
<pre>
Otra forma de ejecutar el algoritmo es ejecutando en una consola shell o git bash dentro de la raiz del 
proyecto clonado:
python main.py
</pre>
