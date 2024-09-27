import numpy as np
import random

# Crea un tablero fijo rellenado de ("_")
def crear_tablero(tamaño=10):
    tablero = np.full((tamaño, tamaño), "_")
    return tablero

# Coloca un barco en el tablero comprobando que no haya otro
def colocar_barco(barco, tablero):
    for (fila, col) in barco:
        if tablero[fila, col] == '_':  # Solo coloca el barco si es agua
            tablero[fila, col] = 'O'
    return tablero

# Dispara a una casilla, importante para luego el cambio de turno
def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
        return "Tocado"
    elif tablero[casilla] == "_":
        print("Agua")
        tablero[casilla] = "A"
        return "Agua"
    else:
        print("Ya disparaste aquí")
        return "Ya disparado"

# Crea un barco de manera aleatoria 
def crear_barco(eslora, tamaño_tablero=10):
    orientacion = random.choice(['H', 'V'])  # H para horizontal, V para vertical
    if orientacion == 'H':
        fila = random.randint(0, tamaño_tablero - 1)
        col = random.randint(0, tamaño_tablero - eslora)
        barco = [(fila, c) for c in range(col, col + eslora)]
    else:
        fila = random.randint(0, tamaño_tablero - eslora)
        col = random.randint(0, tamaño_tablero - 1)
        barco = [(f, col) for f in range(fila, fila + eslora)]
    
    return barco

# Verifica si un barco es válido para ser colocado dentro del tablero
def barco_valido(barco, tablero):
    for (fila, col) in barco:
        if fila >= len(tablero) or col >= len(tablero) or tablero[fila, col] != "_":
            return False
    return True

# Coloca varios barcos en el tablero hasta que sean validos
def colocar_barcos(tablero):
    lista_esloras = [2, 2, 2, 3, 3, 4]
    for eslora in lista_esloras:
        colocado = False
        while not colocado:
            barco = crear_barco(eslora)
            if barco_valido(barco, tablero):
                colocar_barco(barco, tablero)
                colocado = True

# El turno del jugador, que repite si acierta
def turno_jugador(tablero_enemigo):
    while True:
        try:
            fila = int(input("Introduce la fila del disparo (0-9): "))
            col = int(input("Introduce la columna del disparo (0-9): "))
            resultado = disparar((fila, col), tablero_enemigo)
            if resultado == "Agua":  # Si falla, sale del bucle y cambia el turno
                break
        except (ValueError, IndexError):
            print("Entrada inválida, por favor intenta de nuevo.")

# El turno de la máquina, si repite acierta
def turno_maquina(tablero_jugador):
    while True:
        fila, col = random.randint(0, 9), random.randint(0, 9)
        print(f"La máquina dispara a ({fila}, {col})")
        resultado = disparar((fila, col), tablero_jugador)
        if resultado == "Agua":  # Si falla, sale del bucle y cambia el turno
            break

# Comprueba si quedan barcos en el tablero
def quedan_barcos(tablero):
    return 'O' in tablero

# Función principal del juego
def jugar():
    # Tableros del jugador y la máquina
    tablero_jugador = crear_tablero()
    tablero_maquina = crear_tablero()

    # Colocar barcos en ambos tableros
    colocar_barcos(tablero_jugador)
    colocar_barcos(tablero_maquina)

    # Turnos alternos hasta que uno acierte
    turno_jugador_activo = True  # Empieza el jugador
    while quedan_barcos(tablero_jugador) and quedan_barcos(tablero_maquina):
        if turno_jugador_activo:
            print("Turno del jugador")
            turno_jugador(tablero_maquina)
            turno_jugador_activo = False  # Cambia turno a la máquina si falla
        else:
            print("Turno de la máquina")
            turno_maquina(tablero_jugador)
            turno_jugador_activo = True  # Cambia turno al jugador si falla

    # Mostrar quién ganó y si quieres volver a jugar
    if quedan_barcos(tablero_jugador):
        print("¡Has ganado!")
    else:
        print("La máquina ha ganado.")
def iniciar_juego():
    while True:
        jugar()  # Inicia una partida
        # Preguntar al usuario si quiere volver a jugar
        jugar_nuevamente = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_nuevamente != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

# Para iniciar el juego:
if __name__ == "__main__":
    jugar()