# 🧩 Juego de Caminos en Consola (Python)

Este proyecto es un mini juego desarrollado en **Python** que se ejecuta en consola.  
El jugador debe desplazarse por un mapa evitando muros y encontrando el objetivo final.

El proyecto fue creado como práctica de lógica, control de movimientos, validación de caminos y representación de estados, sentando las bases para la implementación de algoritmos de búsqueda como **BFS (Breadth-First Search)**.

---

## 🎯 Objetivo del juego

- Mover al jugador por el mapa usando controles de teclado
- Evitar muros y salir de los límites del mapa
- Llegar al objetivo 🏁 para ganar la partida

---

## 🧠 Conceptos aplicados

- Manejo de matrices (mapa 2D)
- Control de estados y posiciones
- Validación de movimientos
- Bucles y condicionales
- Entrada de datos por consola
- Diseño de HUD en consola
- Pensamiento lógico aplicado a caminos y restricciones

---

## 🗺️ Elementos del mapa

| Elemento | Símbolo | Descripción |
|--------|--------|------------|
| Jugador | 🧍 | Personaje controlado por el usuario |
| Espacio vacío | ⬜ | Camino libre |
| Muro | 🧱 | Obstáculo, no se puede atravesar |
| Objetivo | 🏁 | Meta del juego |
| Borde | 🔳 | Marco del mapa |

---

## 🎮 Controles

- **W** → Arriba  
- **S** → Abajo  
- **A** → Izquierda  
- **D** → Derecha  
- **Q** → Salir del juego  

---

## 📏 Reglas del juego

- No se puede salir del mapa
- No se pueden atravesar muros
- El mapa es de **8x8**
- Se generan entre **4 y 6 muros aleatorios**
- Existe **un único objetivo**
- Al llegar a 🏁, el jugador gana

---

## 🖥️ HUD (Interfaz en consola)

Durante el juego se muestra:
- El mapa con bordes
- La posición actual del jugador
- Los controles disponibles
- Mensajes de estado (movimiento inválido, victoria, salida)

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- Librerías estándar:
  - `os`
  - `random`
- Consola / Terminal

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/tu-repo.git
