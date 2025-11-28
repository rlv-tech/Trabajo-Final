# Ta-Te-Ti (Usuario Vs Maquina)
from random import randrange
import time

# Formato tablero con números y fichas
def mostrar_tablero(tablero):
    print("\n+---+---+---+")
    print(f"| {tablero[0]} | {tablero[1]} | {tablero[2]} |")
    print("+---+---+---+")
    print(f"| {tablero[3]} | {tablero[4]} | {tablero[5]} |")
    print("+---+---+---+")
    print(f"| {tablero[6]} | {tablero[7]} | {tablero[8]} |")
    print("+---+---+---+\n")

# Verificar ganador
def hay_ganador(tablero, jugador):
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8],   # filas
        [0,3,6], [1,4,7], [2,5,8],   # columnas
        [0,4,8], [2,4,6]             # diagonales
    ]
    return any(tablero[a] == tablero[b] == tablero[c] == jugador for a,b,c in combinaciones)

# Movimiento de la máquina
def movimiento_maquina(tablero):
    libres = [i for i in range(9) if tablero[i] not in ["X","O"]]
    return libres[randrange(len(libres))]

# Juego principal
def tateti():
    tablero = ["1","2","3","4","5","6","7","8","9"]
   
    jugador = "X"
    maquina = "O"
    
    print("\n¡Bienvenido al Ta-Te-Ti contra la máquina!")
    mostrar_tablero(tablero)
    
    turno = "jugador"

    while True:

        # Turno del jugador
        if turno == "jugador":
            casilla = input("Elegí un casillero (1-9): ")

            if not casilla.isdigit():
                print("Tenés que ingresar un número del 1 al 9.")
                continue
            casilla = int(casilla) - 1
            
            if casilla < 0 or casilla > 8:
                print("Posición inválida.")
                continue
            
            if tablero[casilla] in ["X", "O"]:
                print("Ese lugar ya está ocupado.")
                continue
            tablero[casilla] = jugador
            mostrar_tablero(tablero)
            
            if hay_ganador(tablero, jugador):
                print("¡Felicidades, ganaste!\n")
                break

            turno = "maquina"

        # Turno de la máquina    
        else:
            time.sleep(0.3)
            print("\n---------------------------")
            print("La máquina está pensando...\n")
            time.sleep(1)
            pos = movimiento_maquina(tablero)
            tablero[pos] = maquina
            mostrar_tablero(tablero)

            if hay_ganador(tablero, maquina):
                print("¡Perdiste! La máquina hizo Ta-Te-Ti\n")
                break

            turno = "jugador"

        # Empate
        if all(x in ["X","O"] for x in tablero):
            print("¡Hay un empate!\n")
            break

while True:
    tateti()

    while True:
        opcion = input("¿Querés jugar de nuevo? (s/n): ").strip().lower()

        if opcion == "s":
            break
        elif opcion == "n":
            print("\n¡Gracias por jugar! Hasta la próxima.\n")
            exit()
        else:
            print("\nOpción inválida. Escribí solo 's' o 'n'.\n")
