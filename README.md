# 🧭 THE HUDDLE - Calculadora de Rutas

**Autor:** Ivan Leiva  
**Proyecto:** Challenge CodePro 4.0  
**Fecha:** 25 Enero 2025

---

## 📖 ¿Qué es este proyecto?

Este es mi proyecto para el primer challenge de la etapa de The Huddle de CodePro. La idea principal era crear un pequeño programa que encuentre el camino mas corto entre punto A y el punto B, debia contar con obstaculos, como si fuera un GPS de la vida cotidiana guiando por la ciudad

Al principio del challenge me costo entender un poco como funcionaba el challenge ya que solo alcance a leer un solo algoritmo (BFS), pero luego me concentre en entender los demas algoritmos (Dijkstra y A*), logre implementar todos y que el usuario decida cual usar.

---

## 🎯 ¿Qué hace el programa?


El programa hace lo siguiente:

1. Genera un mapa aleatorio de [10x10] con diferentes tipos de terrenos
2. El usuario elige dónde empieza y dónde quiere llegar
3. Calcula la mejor ruta usando uno de los tres algoritmos
4. Muestra el camino en pantalla con símbolos ASCII 

Los terrenos que uso son:
- `.` = Camino libre (fácil de pasar)
- `X` = Muros (no se puede pasar)
- `~` = Agua (se puede pasar pero cuesta más)
- `#` = Zonas bloqueadas (tampoco se puede pasar)

---

## 🧠 ¿Qué algoritmos implementé?

El Algoritmo que implemente son los tres que podiamos usar a eleccion, pero me parecio mas efectivo el BFS.

### 1. BFS (Breadth-First Search)

El BFS o Breadth-First Search (Busqueda en Anchura). Es un algoritmo que explora un grafo o matriz por niveles. Primero revisa todos los caminos vecinos, y luego los vecinos de esos, y asi sucesivamente hasta llegar a la meta. Garantiza encontrar el camino mas corto mas no el mas efectivo.


**¿Por qué lo elegí?**
-Elegi el BFS por que me garantiza el camino mas corto en cantidad de pasos
-Es relativamente simple de entender e implementar
-Funciona perfecto cuando todos los movimientos tienen el mismo "costo"
-Es el algoritmo que mas se ajustaba a los requisitos del challenge

### 2. Dijkstra
El Dijkstra es un metodo para enconrar una ruta corta desde un origen a todos los demas usando un grafo (red) con pesos no negativos. Funcionando de forma iterativa al explorar gradualmente rutas, priorizando las mas cortas y actualizando distancias hasta encontrar la solucion mas optima


**Diferencia con BFS:**
Ambos algoritmos buscan la ruta mas corta de un punto A al punto B, pero BFS no funciona para grafos no ponderados (minimos numeros de aristas) usando una cola. Es util por que el dijkstra calcula costos variabes, es deir, permita modelar situaciones dond ecada paso tiene un costo diferente.  

### 3. A* (A-Star)

La heurisicas son atajos que ayudan a personas a tomar decisiones rapidas. Son regkas o metodos que ayudan a las a persona a utilizar la razon y la experiencia ya adquirida para resolver problemas de manera eficiente.

**¿Qué lo hace especial?**
Lo que lo hace especial es la estimacion inteligente dek costo desde un nodo de inicio hasta el objetivo, que guia la busqueda de forma eficiente sin garantizar que la solucion optima sea la mas corta.

---

## 🛠️ ¿Cómo lo construí?
Cuando recibi el challenge, lo primero que hice fue leer los requisitos varias veces por que al principio no entendia bien que era un "algoritmo pathfinding". Busque videos en Youtube sobre BFS y encontre varios que explicaban el concepto con ejemplos visuales de laberintos.


### Pasos que seguí:

1. **Primero armé el mapa:**
   - [¿Cómo lo hiciste? ¿Qué fue lo más difícil?]
      Empece creando una funcion para generar un mapa vacio. Mi primera version usaba un bucle simple:
      mapa = []
      for _ in range(10):
      fila = [0] * 10
      mapa.append(fila)
      Funcionaba bien. Lo que me costo al principio fue entender como acceder a una casilla especifica con (mapa[fila][columna]), pero despues de hacer algunas pruebas y ver errores entendi.
2. **Luego la visualización:**
   - [¿Por qué elegiste ASCII? ¿Probaste emojis?]
      Al principio mi mapa mostraba emojis y se veia bien. Pero decidi usar ASCII por que el challenge pedia explicitamente esos simbolos.
      
      Lo mas complicado fue hacer que se viera ordenado con los bordes + y los espacios entre cada simbolo. tuve que usar (end=" ")  en los prints para que no saltaa de linea.

      Tambien cree una funcion (obtener_simbolo()) que decide que mostrar segun prioridades: inicio>objeto>ruta>terreno. Esto mantuvo el codigo organizado.

3. **Después el BFS:**
   - [¿Qué parte te costó más? ¿Cómo lo resolviste?]
      Implementar el BFS fue lo que me costo mas del proyecto. Al principio no entendia bien como funcionaban las estructuras de datos que necesitaba:
      *Cola(deque): Para procesar las posiciones en orden
      *Visitados(set): Para no revisar la misma casilla dos veces
      *Padres(diccionario): Para recinstruir el camino al final



### Problemas que tuve:

El problema que tuve intentar guardar el camino completo en cada elemento de la cola. Esto no funcionaba bien y el codigo tenia errores. 
---

## 📚 ¿Qué aprendí?

Aprendi que para que el BFS funcione debia usar "padres" donde cada posicion "recuerda" de donde vino. AL final, con ese diccionario reconstruyo el camino completo de atras hacia adelante. Tambien aprendi un poco de estructuras de datos y matrices bidimencionales. 



### Lecciones personales:

- [Algo que aprendiste sobre programación]
- [Algo que aprendiste sobre resolver problemas]
- [Algo que mejorarías si lo hicieras de nuevo]

---

##  ¿Cómo usar el programa?

### Requisitos:
- Python 3.x
- Terminal/Consola

### Ejecutar:

```bash
# Clonar el repositorio
git clone https://github.com/Ivan-leiva-dev/encontrar-ruta-python.git

# Entrar a la carpeta
cd encontrar-ruta-python

# Ejecutar
python encontrar_ruta.py
```

### Uso:

1. El programa genera un mapa aleatorio
2. Te pide coordenadas de inicio (ejemplo: fila 0, columna 0)
3. Te pide coordenadas de destino (ejemplo: fila 9, columna 9)
4. Eliges el algoritmo (1=BFS, 2=Dijkstra, 3=A*)
5. Te muestra la ruta con `*`

---

## 🎨 Ejemplo de salida

```
+ - - - - - - - - - +
+ S . . . X . . . . +
+ . . ~ . . . . . . +
+ . X * * * . . . . +
+ . . * . . # . . . +
+ . . * . . . . . . +
+ . . X * ~ * * * . +
+ . . . . . . . * . +
+ . . . . . . X * . +
+ . . . . . . . * . +
+ . . . . . . . . E +
+ - - - - - - - - - +

✅ ¡Ruta encontrada con BFS!
📏 Longitud: 18 pasos
```

---

## 📧 Contacto

**Ivan Leiva**  
GitHub: [@Ivan-leiva-dev](https://github.com/Ivan-leiva-dev)

---

*"En una ciudad bloqueada, el código encuentra el camino."*