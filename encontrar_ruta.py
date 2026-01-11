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

#Configuracion
FILAS = 8
COLUMNAS = 8

BORDE = "🔳"
VACIO = "⬜"
JUGADOR = "🧍"
MURO = "🧱"
OBJETIVO = "🏁" 

#Funciones

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def crear_mapa():
    mapa = [[VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]
    

    #muros
    for _ in range(6):
        f, c = random.randint(0, FILAS-1), random.randint(0, COLUMNAS-1)
        mapa[f][c] = MURO

    #Objetivo
    while True:
        of, oc = random.randint(0, FILAS-1), random.randint(0, COLUMNAS-1)
        if mapa[of][oc] == VACIO:
            mapa[of][oc] = OBJETIVO
            break
    return mapa

def imprimir_hud(mapa, posicion):
    limpiar()

    print(BORDE * (COLUMNAS + 2))
    for f in range(FILAS):
        print(BORDE, end="")
        for c in range(COLUMNAS):
            if (f, c) == posicion:
                print(JUGADOR, end="")
            else:
                print(mapa[f][c], end="")
        print(BORDE)
    print(BORDE * (COLUMNAS + 2))

    print("\n Controles: W A S D │ Q salir")
    print(f"📍 Posicion: {posicion}")

def mover(jugador, tecla):
    f, c = jugador
    if tecla == "w": f -= 1
    elif tecla == "s": f += 1
    elif tecla == "a": c -= 1
    elif tecla == "d": c += 1
    return f, c

def movimiento_valido(mapa, pos):
    f, c = pos
    if 0 <= f < FILAS and 0 <= c < COLUMNAS:
        return mapa[f][c] != MURO
    return False

#LOOP PRINCIPAL

def jugar():
    mapa = crear_mapa()
    

    jugador = None
    for f in range(FILAS):
        for c in range(COLUMNAS):
            if mapa[f][c] == VACIO:
                jugador = (f, c)
                break
        if jugador:
            break
    if not jugador:
        jugador = (0, 0)

    while True:
        imprimir_hud(mapa, jugador)

        #verificar victora
        if mapa[jugador[0]][jugador[1]] == OBJETIVO:
            print("\n 🏆 ¡GANASTE! Llegaste al objetivo.")
            break

        #pedir movimiento
        tecla = input("🧑‍💻 Movimiento: ").lower()

        #salir
        if tecla == "q":
            print("👋 ¡Gracias por jugar!")
            break

        #Mover jugador
        if tecla in ["w", "a", "s", "d"]:
            nueva_pos = mover(jugador, tecla)
            if movimiento_valido(mapa, nueva_pos):
                jugador = nueva_pos
            else:
                print("❌ Movimiento inválido. Intenta de nuevo.")
                input("Presiona Enter para continuar...")

#Iniciar juego
jugar()

