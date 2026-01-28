""" The Huddle - Calculadora de rutas 
Enuentra el camino mas corto en una ciudad con obstaculos
Algoritmos: BFS (Breadth-First Search), Dijkstra, A*"""

import os
import random
from collections import deque

#TAMAÑO DEL MAPA
FILAS = 10
COLUMNAS = 10

#VALORES NUMERICOS DEL TERRENO
TERRENO_LIBRE = 0   #Camino libre
TERRENO_MURO = 1   #Edificio(obstaculo)
TERRENO_AGUA = 2    #Agua(osbtaculo con ruta alternativa)
TERRENO_BLOQUEADO = 3  #Zona bloqueada temporalmente

#SIMBOLOS MODO ASCII
BORDE = "+"
LIBRE = "."
MURO = "X"
AGUA = "~"
BLOQUEADO = "#"
INICIO = "S"
OBJETIVO = "E"
RUTA = "*"

def limpiar_pantalla():
    """ Limpia la consola segun el sistema operativo"""
    os.system("cls" if os.name == "nt" else "clear")

def generar_mapa():
    """crea un mapa vacio (todos los espacios libres)"""

    mapa = []
    for _ in range(FILAS):
        fila = [TERRENO_LIBRE] * COLUMNAS
        mapa.append(fila)
    return mapa
                    
def agregar_obstaculos(mapa, tipo_terreno, cantidad):
    """Agrega obstaculos de un tipo especifico al mapa""" 
    colocados = 0
    intentos = 0
    max_intentos = cantidad * 10

    while colocados < cantidad and intentos < max_intentos:
        #genera una fila aleatoria entre 0 y FILAS-1
        f = random.randint(0, FILAS -1)

        #genera una columna aleatoria entre 0 y columnas -1
        c = random.randint(0, COLUMNAS -1)

        #verifica si la posicion esta libre
        if mapa[f][c] == TERRENO_LIBRE:
            #coloca el obstaculo
            mapa[f][c] = tipo_terreno
            colocados += 1
        intentos += 1


def obtener_simbolo(valor_terreno, es_inicio= False, es_objetivo= False, es_ruta=False):
    """Convirte un valor numerico en simbolo visual"""

    if es_inicio:
        return INICIO #"S"
    elif es_objetivo:
        return OBJETIVO #"E"
    elif es_ruta:
        return RUTA #"*"
    else:
        if valor_terreno == TERRENO_LIBRE:
            return LIBRE  #"."
        elif valor_terreno == TERRENO_MURO:
            return MURO  #"X"
        elif valor_terreno == TERRENO_AGUA:
            return AGUA  #"~"
        elif valor_terreno == TERRENO_BLOQUEADO:
            return BLOQUEADO  #"#"
        else:
            return LIBRE
        

def mostrar_mapa(mapa, inicio=None, objetivo=None, ruta=None, mensaje=" "):
    """Muestra el mapa en pantalla con formato visual"""
    limpiar_pantalla()

    print("=" * 50)
    print("🧭 CALCULADORA DE RUTAS")
    print("=" * 50)
    print()

    print(BORDE + " " + "- " * COLUMNAS + BORDE)

    for f in range(FILAS):
        print(BORDE, end= " ")

        for c in range(COLUMNAS):
            es_inicio = (inicio is not None and inicio == (f, c))
            es_objetivo = (objetivo is not None and objetivo == (f, c))
            es_ruta = (ruta is not None and (f, c) in ruta)

            simbolo = obtener_simbolo(mapa[f][c], es_inicio, es_objetivo, es_ruta)
            print(simbolo, end=" ")
        print(BORDE)

    print(BORDE + " " + "- " * COLUMNAS + BORDE)

    print("\n📖 LEYENDA:")
    print(f" {INICIO} = Inicio │ {OBJETIVO} = Objetivo │ {RUTA} = Ruta")
    print(f" {MURO} = Muro │ {AGUA} = Agua │ {BLOQUEADO} = Bloqueado │ {LIBRE} = Libre")

    if mensaje:
        print(f"\n📨  {mensaje}")

        if ruta:
            print(f"\n  Longitud: {len(ruta) -1} pasos")

def pedir_coordenadas(mapa, tipo="inicio"):
    while True:
        try:
            print(f"\n📍Ingresa coordenadas de {tipo.upper()}:")
            f = int(input(f" Fila (0-{FILAS-1}): "))
            c = int(input(f" Columna (0-{COLUMNAS-1}): "))

            if not (0 <= f < FILAS and 0 <= c < COLUMNAS):
                print("❌ Fuera del mapa. Intenta de nuevo.")
                continue
            return (f, c)
        except ValueError:
            print("❌ Debes ingresar numeros. Intenta de nuevo.")

def buscar_ruta_bfs(mapa, inicio, objetivo):
    """Encuentra la ruta mas corta usando BFS (Breadth-First search)"""
    cola = deque([inicio])
    visitados = {inicio}
    padres = {inicio: None}

    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while cola:
        f, c = cola.popleft()

        if (f, c) == objetivo:
            return reconstruir_camino(padres, objetivo)
        
        for df, dc in direcciones:
            nf = f + df
            nc = c + dc
            nueva_pos = (nf, nc)


            if (0 <= nf < FILAS and
                0 <= nc < COLUMNAS and
                nueva_pos not in visitados):

                if mapa[nf][nc] not in [TERRENO_MURO, TERRENO_BLOQUEADO]:
                    visitados.add(nueva_pos)
                    padres[nueva_pos] = (f, c)
                    cola.append(nueva_pos)
    return None

def reconstruir_camino(padres, objetivo):
    """Reconstruye el camino desde el inicio hasta el objetivo"""
    camino = []
    actual = objetivo

    while actual is not None:
        camino.append(actual)
        actual = padres[actual]

    camino.reverse()
    return camino

# ========== PROGRAMA PRINCIPAL (CORREGIDO) ==========

def main():
    """Función principal del programa"""
    
    while True:  # ✅ Loop infinito controlado
        limpiar_pantalla()
        
        # Bienvenida
        print("=" * 50)
        print("🧭 THE HUDDLE - CALCULADORA DE RUTAS")
        print("=" * 50)
        print("\n🌆 Estás en una ciudad desconocida...")
        print("El cielo está nublado, los caminos bloqueados.")
        print("Tu GPS dice: 'Buena suerte, estás por tu cuenta.'")
        print("\n🎯 Tu misión: Encontrar la mejor ruta posible.")
        
        input("\nPresiona ENTER para generar el mapa...")
        
        # Crear mapa con obstáculos
        mapa = generar_mapa()
        agregar_obstaculos(mapa, TERRENO_MURO, 5)
        agregar_obstaculos(mapa, TERRENO_AGUA, 3)
        agregar_obstaculos(mapa, TERRENO_BLOQUEADO, 2)
        
        # Mostrar mapa inicial
        mostrar_mapa(mapa, None, None, None, "Mapa generado. Elige tus puntos.")
        
        # Pedir coordenadas al usuario
        inicio = pedir_coordenadas(mapa, "inicio")
        objetivo = pedir_coordenadas(mapa, "objetivo")
        
        # Mostrar antes de calcular
        mostrar_mapa(mapa, inicio, objetivo, None, "🔍 Calculando ruta...")
        input("\nPresiona ENTER para calcular...")
        
        # ¡CALCULAR LA RUTA CON BFS!
        ruta = buscar_ruta_bfs(mapa, inicio, objetivo)
        
        # Mostrar resultado
        if ruta:
            mostrar_mapa(mapa, inicio, objetivo, ruta, "✅ ¡Ruta encontrada!")
            
            # Mostrar pasos de la ruta
            print(f"\n🎯 PASOS DE LA RUTA:")
            for i, (f, c) in enumerate(ruta):
                terreno = mapa[f][c]
                tipo = ""
                if terreno == TERRENO_AGUA:
                    tipo = " (Agua - ruta alternativa)"
                print(f"   {i}. ({f}, {c}){tipo}")
            
            # Estadísticas
            print(f"\n📊 ESTADÍSTICAS:")
            print(f"   • Pasos totales: {len(ruta) - 1}")
            agua_cruzada = sum(1 for (f, c) in ruta if mapa[f][c] == TERRENO_AGUA)
            if agua_cruzada > 0:
                print(f"   • Zonas de agua atravesadas: {agua_cruzada}")
        else:
            mostrar_mapa(mapa, inicio, objetivo, None, "❌ No hay ruta posible.")
            print("\n💡 Sugerencia: Los obstáculos bloquean completamente el camino.")
        
        # Opción de reiniciar
        print()
        opcion = input("¿Calcular otra ruta? (s/n): ").lower()
        
        if opcion != 's':  # Si NO es 's', sale del loop
            break
    
    # Mensaje de despedida 
    print("\n" + "=" * 50)
    print("👋 ¡Gracias por usar THE HUDDLE!")
    print("El destino... se calcula en código. 🧭✨")
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Programa terminado por el usuario.")
    except Exception as e:
        print(f"\n Error inesperado: {e}")
