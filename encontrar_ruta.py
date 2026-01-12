#Elementos a utilizar:
#jugador= 🧍 se mueve
#vacio= ◻️ espacio libre
#Muro= 🧱 No se puede pasar
#Objetivo= 🏁 Meta si llegas
#Borde= 🔳 Marco

#Reglas del juego:
#movimientos: w=arriba, s=abajo, a=izquierda, d=derecha
#no puedes salir del mapa
#no puedes atravesar muros
#Al llegar a 🏁 ganaste
#Mostrar info en HUD: Posicio, controles, Estado del juego

#Nivel de dificultad:
#mapa chico: 8x8
#4-6 obstaculos
#1 Objetivo

import os
import random
from collections import deque

#Configuracion
FILAS = 8
COLUMNAS = 8

BORDE = "🔳"
VACIO = "⬜"
AGUA = "🌊"
BLOQUEADO = "🚧"
INICIO = "🟢"
MURO = "🧱"
OBJETIVO = "🏁" 
RUTA = "⭐"


#VAlores numericos para el mapa del juego
TERRENO_LIBRE = 0
TERRENO_MURO = 1
TERRENO_AGUA = 2
TERRENO_BLOQUEADO = 3


#Funciones

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def crear_mapa():
    mapa = [[TERRENO_LIBRE for _ in range(COLUMNAS)] for _ in range(FILAS)]
    

    #Obstaculos
    tipos_obstaculos = [
        (TERRENO_MURO, 3),
        (TERRENO_AGUA, 2),
        (TERRENO_BLOQUEADO, 1)
    ]

    for tipo, cantidad in tipos_obstaculos:
        for _ in range(cantidad):
            f, c = random.randint(0, FILAS -1), random.randint(0, COLUMNAS -1)
            if mapa[f][c] == TERRENO_LIBRE:
                mapa[f][c] = tipo

    #ya no ponemos objetivo por que el usuario elije donde empeza y su destino
    return mapa

def obtener_simbolo(mapa, pos, inicio, objetivo, ruta=None):
    """"Convertimos el valor numerico en simbolo"""
    f, c = pos

    #aca la prioridad es: inicio > objetivo > ruta > terreno
    if pos == inicio:
        return INICIO
    elif pos == objetivo:
        return OBJETIVO
    elif ruta and pos in ruta:
        return RUTA
    
    # su no es especial, muestra el terreno
    terreno = mapa[f][c]
    if terreno == TERRENO_LIBRE:
        return VACIO
    elif terreno == TERRENO_MURO:
        return MURO
    elif terreno == TERRENO_AGUA:
        return AGUA
    elif terreno == TERRENO_BLOQUEADO:
        return BLOQUEADO
    return VACIO #por defecto

def imprimir_mapa(mapa, inicio, objetivo, ruta=None, mensaje=""):
    """Imprimme el mapa con la ruta calculada si es que existe"""
    limpiar()

    print("=" * 50)
    print("🧭 THE HUDDLE - CALCULADORA DE RUTAS")
    print("=" * 50)

    #Imprimir el mapa
    print("\n" + BORDE * (COLUMNAS + 2))
    for f in range(FILAS):
        print(BORDE, end="")
        for c in range(COLUMNAS):
            simbolo = obtener_simbolo(mapa, (f, c), inicio, objetivo, ruta)
            print(simbolo, end="")
        print(BORDE)
    
    #Leyenda
    print("\n LEYENDA:")
    print(f" {INICIO} Inicio │ {OBJETIVO} Objetivo │ {RUTA} Ruta optima")
    print(f" {MURO} Muro │ {AGUA} Agua │ {BLOQUEADO} Bloqueado")

    if mensaje:
        print(f"\n {mensaje}")

    if ruta:
        print(f"\n Longitud de la ruta: {len(ruta) -1} pasos")

    #funcion para pedir coordenadas
def pedir_coordenadas(mapa, tipo="inicio"):

    while True:
        try:
            print(f"\n 📍 Ingresa coordenadas de {tipo.upper()}:")
            f = int(input(f" Fila (0-{FILAS-1}): "))
            c = int(input(f" Columna (0-{COLUMNAS-1}): "))

            #Validar que este dentro del mapa y que no sea muro
            if not (0 <= f < FILAS and 0 <= c < COLUMNAS):
                print("❌ Coordenadas fuera del mapa.")
                continue

            #Validar que no sea muro
            if mapa[f][c] == TERRENO_MURO:
                print("❌ No puedes elegir un muro.")
                continue
            return (f, c)
        except ValueError:
            print("❌ Ingresa numeros validos.")

def buscar_ruta_bfs(mapa, inicio, objetivo):
    """Encuentra el camino mas corto usando BFS
    Retorna: Lista de coordenadas del camino, o None si no existe"""
    cola = deque([(inicio, [inicio])])
    visitados = {inicio}

    #Movimientos posibles
    direcciones = [(-1, 0), (1, 0), (0, -1), (0,1)]

    while cola:
        (f, c), camino = cola.popleft()

        #llego?
        if(f, c) == objetivo:
            return camino
        
        #Explora vecinos
        for df, dc in direcciones:
            nf, nc = f + df, c + dc 
            nueva_pos = (nf, nc)

        #Verifica si es valido
            if (0 <= nf < FILAS and
                0 <= nc < COLUMNAS and
                nueva_pos not in visitados):

        # No atavesar muros ni bloqueados
                if mapa[nf][nc] not in [TERRENO_MURO, TERRENO_BLOQUEADO]:
                    visitados.add(nueva_pos)
                    cola.append((nueva_pos, camino + [nueva_pos]))
    return None




#LOOP PRINCIPAL
def main():
    """Ejecuta el programa principal"""
    limpiar()
    
    print("=" * 50)
    print("🧭 THE HUDDLE - CALCULADORA DE RUTAS")
    print("=" * 50)
    print("\nBienvenido al calculador de rutas óptimas.")
    
    input("\nPresiona ENTER para generar el mapa...")
    
    #  Crear mapa
    mapa = crear_mapa()
    
    #  Mostrar mapa vacío
    imprimir_mapa(mapa, None, None, None, "Mapa generado. Elige tus puntos.")
    
    #  Pedir inicio y objetivo
    inicio = pedir_coordenadas(mapa, "inicio")
    objetivo = pedir_coordenadas(mapa, "objetivo")
    
    #  Mostrar antes de calcular
    imprimir_mapa(mapa, inicio, objetivo, None, "🔍 Calculando ruta...")
    input("\nPresiona ENTER para calcular...")
    
    #  ¡CALCULAR LA RUTA CON BFS!
    ruta = buscar_ruta_bfs(mapa, inicio, objetivo)
    
    #  Mostrar resultado
    if ruta:
        imprimir_mapa(mapa, inicio, objetivo, ruta, "✅ ¡Ruta encontrada!")
        print(f"\n🎯 Pasos de la ruta:")
        for i, (f, c) in enumerate(ruta):
            print(f"   {i}. ({f}, {c})")
    else:
        imprimir_mapa(mapa, inicio, objetivo, None, "❌ No hay ruta posible.")
    
    # Opción de reiniciar
    opcion = input("\n¿Otra ruta? (s/n): ").lower()
    if opcion == 's':
        main()
    else:
        print("\n👋 ¡Gracias por usar THE HUDDLE!")


#Iniciar juego
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa terminado.")

