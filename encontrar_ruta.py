""" The Huddle - Calculadora de rutas 
Enuentra el camino mas corto en una ciudad con obstaculos
Algoritmos: BFS (Breadth-First Search), Dijkstra, A*"""

import random
from collections import deque

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


def generar_mapa(filas, columnas):
    """crea un mapa vacio (todos los espacios libres)"""
    return [[TERRENO_LIBRE for _ in range(columnas)] for _ in range(filas)]
                    
def agregar_obstaculos(mapa, filas, columnas, tipo_terreno, cantidad):
    """Agrega obstaculos de un tipo especifico al mapa""" 
    colocados = 0
    while colocados < cantidad :
        #genera una fila aleatoria entre 0 y FILAS-1
        fil, col =random.randint(0, filas-1), random.randint(0, columnas-1)
        #verifica si la posicion esta libre
        if mapa[fil][col] == TERRENO_LIBRE:
            #coloca el obstaculo
            mapa[fil][col] = tipo_terreno
            colocados += 1


def obtener_simbolo(mapa, pos, inicio, objetivo, ruta):
    """Convirte un valor numerico en simbolo visual"""

    fil, col = pos
    if pos == inicio:
        return INICIO
    if pos == objetivo:
        return OBJETIVO
    if ruta and pos in ruta:
        return RUTA

    simbolo = {0: LIBRE, 1: MURO, 2: AGUA, 3: BLOQUEADO}
    return simbolo.get(mapa[fil][col], LIBRE) 

def mostrar_mapa(mapa, FILAS, COLUMNAS, inicio, objetivo, ruta, mensaje):
    """Muestra el mapa en pantalla con formato visual"""
    print("🧭 CALCULADORA DE RUTAS")
    print()

    print(BORDE + " " + "- " * COLUMNAS + BORDE)

    for f in range(FILAS):
        print(BORDE, end= " ")
        for c in range(COLUMNAS):
            print(obtener_simbolo(mapa, (f, c), inicio, objetivo, ruta), end=" ")
        print(BORDE)
    print(BORDE + " " + "- " * COLUMNAS + BORDE)
    print(f"\n {INICIO}=Inicio │ {OBJETIVO}=Objetivo │ {RUTA}=Ruta │ {MURO}=Muro │ {AGUA}=Agua │ {BLOQUEADO}=Bloqueado")
    if mensaje:
        print(f"\n{mensaje}")
    if ruta:
        print(f"📏 Pasos: {len(ruta) -1}")
    
def pedir_coordenadas(mapa, filas, columnas, tipo):
    #Pide y valida coordenadas
    while True:
        try:
            print(f"\n📍 {tipo.upper()}:")
            fil = int(input(f" Fila (0-{filas-1}): "))
            col = int(input(f" Columns (0-{columnas-1}): "))

            if not (0 <= fil < filas and 0 <= col < columnas):
                print("❌ Fuera del mapa")
                continue
            if mapa[fil][col] in [TERRENO_MURO, TERRENO_BLOQUEADO]:
                print("❌ No puedes elegir un obstaculo")
                continue
            return (fil, col)
        except ValueError:
            print("❌ Ingresa numeros validos")


def buscar_ruta_bfs(mapa, filas, columnas, inicio, objetivo):
    """Encuentra la ruta mas corta usando BFS (Breadth-First search)"""
    cola = deque([inicio])
    visitados = {inicio}
    padres = {inicio: None}
    
    while cola:
        fil, col = cola.popleft()
        
        if (fil, col) == objetivo:
            # Reconstruir camino
            camino = []
            actual = objetivo
            while actual:
                camino.append(actual)
                actual = padres[actual]
            camino.reverse()
            return camino
        
        # Explorar vecinos (arriba, abajo, izquierda, derecha)
        for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nuevo_fil, nueva_col = fil + df, col + dc
            nueva_pos = (nuevo_fil, nueva_col)
            
            if (0 <= nuevo_fil < filas and 0 <= nueva_col < columnas and
                nueva_pos not in visitados and
                mapa[nuevo_fil][nueva_col] not in [TERRENO_MURO, TERRENO_BLOQUEADO]):
                
                visitados.add(nueva_pos)
                padres[nueva_pos] = (fil, col)
                cola.append(nueva_pos)
    return None
# ========== PROGRAMA PRINCIPAL (CORREGIDO) ==========

def configurar_obstaculos():
    """Permite al usuario configurar cantidad de obstáculos sin modificar código"""
    print("\n🚧 CONFIGURACIÓN DE OBSTÁCULOS")
    print("=" * 50)
    
    try:
        muros = int(input(f"¿Cuántos {MURO} Muros? (0-15): "))
        agua = int(input(f"¿Cuántos {AGUA} Agua? (0-15): "))
        bloqueados = int(input(f"¿Cuántos {BLOQUEADO} Bloqueados? (0-15): "))
        
        # Validar
        if not all(0 <= x <= 15 for x in [muros, agua, bloqueados]):
            print("⚠️ Usando valores por defecto")
            return 5, 3, 2
        
        print(f"\n✅ Total: {muros + agua + bloqueados} obstáculos")
        return muros, agua, bloqueados
        
    except ValueError:
        print("⚠️ Entrada inválida. Usando valores por defecto")
        return 5, 3, 2
    
def modificar_mapa_interactivo(mapa, filas, columnas):
    """Permite agregar o quitar obstáculos después de crear el mapa"""
    while True:
        print("\n🛠️  MODIFICAR MAPA")
        print("=" * 50)
        print("1. Agregar obstáculo")
        print("2. Quitar obstáculo")
        print("3. Continuar sin cambios")
        
        try:
            opcion = int(input("\nOpción (1-3): "))
            
            if opcion == 3:
                break
            
            if opcion in [1, 2]:
                # Mostrar mapa actual
                mostrar_mapa(mapa, filas, columnas, None, None, None, "Mapa actual")
                
                
                if opcion == 1:  # Agregar
                    print(f"\nTipo: 1={MURO} | 2={AGUA} | 3={BLOQUEADO}")
                    tipo = int(input("Tipo de obstáculo (1-3): "))
                    fila = int(input(f"Fila (0-{filas-1}): "))
                    columna = int(input(f"Columna (0-{columnas-1}): "))

                    if tipo in [1, 2, 3]:
                        mapa[fila][columna] = tipo
                        print("✅ Obstáculo agregado")
                    else:
                        print("❌ Tipo inválido")
                
                elif opcion == 2:  # Quitar
                    mapa[fila][columna] = TERRENO_LIBRE
                    print("✅ Obstáculo eliminado")
            else:
                print("❌ Opción inválida")
                
        except ValueError:
            print("❌ Entrada inválida")

def main():
    print("🧭 THE HUDDLE - CALCULADORA DE RUTAS")

    # === CREAR MAPA UNA SOLA VEZ ===
    while True:
        try:
            filas = int(input("\nFilas del mapa: "))
            columnas = int(input("Columnas del mapa: "))
            if filas <= 0 or columnas <= 0:
                print("❌ Valores inválidos")
                continue
            break
        except ValueError:
            print("❌ Ingresa números válidos")

    mapa = generar_mapa(filas, columnas)

    muros, agua, bloqueados = configurar_obstaculos()
    agregar_obstaculos(mapa, filas, columnas, TERRENO_MURO, muros)
    agregar_obstaculos(mapa, filas, columnas, TERRENO_AGUA, agua)
    agregar_obstaculos(mapa, filas, columnas, TERRENO_BLOQUEADO, bloqueados)

    if input("\n¿Modificar mapa inicialmente? (s/n): ").lower() == 's':
        modificar_mapa_interactivo(mapa, filas, columnas)

    # === LOOP PRINCIPAL ===
    while True:
        inicio = pedir_coordenadas(mapa, filas, columnas, "inicio")
        objetivo = pedir_coordenadas(mapa, filas, columnas, "objetivo")

        mostrar_mapa(mapa, filas, columnas, inicio, objetivo, None, "🔍 Calculando...")
        input("\nPresiona ENTER para calcular...")

        ruta = buscar_ruta_bfs(mapa, filas, columnas, inicio, objetivo)

        if ruta:
            mostrar_mapa(mapa, filas, columnas, inicio, objetivo, ruta, "✅ Ruta encontrada")
        else:
            mostrar_mapa(mapa, filas, columnas, inicio, objetivo, None, "❌ Sin ruta")

        # 👉 ACÁ está la clave
        if input("\n¿Modificar obstáculos y recalcular? (s/n): ").lower() == 's':
            modificar_mapa_interactivo(mapa, filas, columnas)
            continue  # vuelve a calcular usando el MISMO mapa

        if input("\n¿Calcular otra ruta sin cambiar mapa? (s/n): ").lower() == 's':
            continue

        break


            
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Programa terminado por el usuario.")
    