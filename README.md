# Inteligencia Artificial - Proyecto Connect 4

Universidad del Valle de Guatemala

Departamento de Ciencias de la Computación

Inteligencia Artificial - Sección 20

Cristian Fernando Laynez Bachez - 201281

## ¿En que consiste?

Básicamente el objetivo de este proyecto es desarrollar una IA que sea capaz de ganar una partida en el juego de Connect4

## Tecnologías y librerías

Este proyecto fue desarrollado con lo siguiente:

- Python
- SocketIO

## Ejecutar el proyecto

Necesitas ingresar los siguientes argumentos para hacer funcionar el cliente:

- USER NAME
- IP ADDRESS
- PORT
- ID TOURNAMENT

```
python3 client.py user_name ip_address port id_tournament
```

Ejemplo:

```
python3 client.py Cristian localhost 4000 142857
```

## ¿Cómo funciona este proyecto?

Este proyecto esta formado con lo siguiente:

- Algoritmo min-max : Este algoritmo se encarga de analizar la mejor jugada que puede tomar la IA.
- Valores Alpha / Beta : Es una técnica donde estos parámetros apoyan al algoritmo Min-Max donde este puede mejorar la eficiencia de busqueda. Alpha representa el mejor valor más grande mientras que Beta representa el mejor valor más pequeño.
- Función Heuristica: Para este contexto esta funcion nos ayuda nos ayuda a analizar una puntuación numérica a una determinada posición del tablero cuando el depth este a 0 o no existan posibles movimientos, se encarga de evaluar los estados del tablero que no son estados terminales, esto ayuda a tomar mejores desiciones.

## Extras:

Se programo un programa llamado "local.py" donde se puede jugar connect 4 con la IA (Player VS IA) [De todas formas se puede modificar para que se pueda jugar jugador vs jugador o IA vs IA].

