# Requisitos:
#
#  1 [O] comprensión de listas con condicionales
#  2 [ ] comprensión de diccionarios
#  3 [O] comprensión de conjuntos
#  4 [O] empaquetamiento de variables
#  5 [O] asignación múltiple
#  6 [O] desempaquetamiento de funciones
#  7 [O] desempaquetamiento extendido
#  8 [ ] enumerado con compresión de listas
#  9 [O] método constructor
# 10 [O] representación de cadenas
# 11 [O] métodos estáticos
# 12 [ ] herencia múltiple
# 13 [ ] normas para métodos y atributos

import random

class Tablero:
    # [9] Metodo constructor
    def __init__(self, filas, columnas):
        # Inicializa el tablero con el tamaño especificado.
        self.filas = filas
        self.columnas = columnas
        # [3] comprensión de conjuntos
        self.tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

    # [11] Metodo estatico para imprimir el tamaño del tablero
    @staticmethod
    def imprimir_tamaño_tablero(tablero):
        print(f"El tablero tiene {len(tablero)} filas y {len(tablero[0])} columnas.")

    def imprimir_tablero(self):
        # Imprime el estado actual del tablero en la consola.
        for fila in self.tablero:
            # [10] representación de cadenas
            print('|'.join(fila))
            print('-' * (self.columnas * 2 - 1))

    def realizar_movimiento(self, columna, jugador):
        # Realiza un movimiento en el tablero para el jugador especificado.
        fila = self.obtener_fila_disponible(columna)
        if fila is not None:
            self.tablero[fila][columna] = jugador
            return True
        return False

    def obtener_fila_disponible(self, columna):
        # Obtiene la fila disponible en una columna específica.
        for fila in range(self.filas - 1, -1, -1):
            if self.tablero[fila][columna] == ' ':
                return fila
        return None

    def verificar_ganador(self, jugador):
        # Verifica si el jugador actual ha ganado el juego.
        # Comprueba todas las posibles combinaciones en filas, columnas y diagonales.
        for fila in range(self.filas):
            for columna in range(self.columnas - 3):
                #  [3] comprensión de conjuntos
                resultado = {self.tablero[fila][columna + i] for i in range(4)}
                if resultado == {jugador}:
                    return True

        for columna in range(self.columnas):
            for fila in range(self.filas - 3):
                #  [3] comprensión de conjuntos
                resultado = {self.tablero[fila + i][columna] for i in range(4)}
                if resultado == {jugador}:
                    return True

        for fila in range(3, self.filas):
            for columna in range(self.columnas - 3):
                if all(self.tablero[fila - i][columna + i] == jugador for i in range(4)):
                    return True

        for fila in range(self.filas - 3):
            for columna in range(self.columnas - 3):
                if all(self.tablero[fila + i][columna + i] == jugador for i in range(4)):
                    return True

        return False

class JuegoConectaCuatro:
    # [9] Metodo constructor
    def __init__(self, *argumentos):
        # [7] desempaquetamiento extendido
        tamaño, jugadores, *simbolos = argumentos

        # [5] Asignacion multiple
        self.jugador_1, self.jugador_2 = jugadores
        
        # [6] desempaquetamiento de funciones
        self.tablero = Tablero(*tamaño)
        
        tamaño_simbolos = len(simbolos)
        
        simbolo_1 = random.randint(0, tamaño_simbolos - 1)
        simbolo_2 = random.randint(0, tamaño_simbolos - 1)
        
        while simbolo_1 == simbolo_2:
            simbolo_2 = random.randint(0, tamaño_simbolos - 1)

        self.jugador_1_simbolo = simbolos[simbolo_1]
        self.jugador_2_simbolo = simbolos[simbolo_2]

        self.jugador_actual = self.jugador_2_simbolo

    def cambiar_turno(self):
        # Cambia el turno entre jugadores self.jugador_2_simbolo y self.jugador_1_simbolo.
        self.jugador_actual = self.jugador_1_simbolo if self.jugador_actual == self.jugador_2_simbolo else self.jugador_2_simbolo

    def obtener_columna_valida(self):
        # Solicita al jugador actual que elija una columna válida.
        while True:
            try:
                nombre_jugador = self.jugador_1 if self.jugador_actual == self.jugador_2_simbolo else self.jugador_2
                columna = int(input(f"{nombre_jugador}, elige una columna {nombre_jugador} (0-{self.tablero.columnas - 1}): "))
                if 0 <= columna < self.tablero.columnas:
                    return columna
                else:
                    print("Columna inválida. Elige una columna dentro del rango.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

    def reiniciar_juego(self):
        # Pregunta al jugador si quiere reiniciar el juego y devuelve True o False en consecuencia.
        while True:
            respuesta = input("¿Quieres jugar de nuevo? (Sí/No): ").lower()
            if respuesta == 'sí':
                return True
            elif respuesta == 'no':
                return False
            else:
                print("Respuesta inválida. Por favor, ingresa 'Si' o 'No'.")

    def jugar(self):
        # Bucle principal del juego.
        while True:
            self.tablero.imprimir_tablero()
            columna = self.obtener_columna_valida()
            if self.tablero.realizar_movimiento(columna, self.jugador_actual):
                #  [1] comprensión de listas con condicionales
                casillas_libres = [fila for fila in self.tablero.tablero for celda in fila if celda != ' ']

                if self.tablero.verificar_ganador(self.jugador_actual):
                    self.tablero.imprimir_tablero()

                    if self.jugador_actual == self.jugador_2_simbolo:
                        print(f"¡{self.jugador_1} ha ganado!")
                    else:
                        print(f"¡{self.jugador_2} ha ganado!")
                    
                    if self.reiniciar_juego():
                        self.tablero = Tablero(self.tablero.filas, self.tablero.columnas)
                        self.jugador_actual = self.jugador_2_simbolo
                    else:
                        break
                elif len(casillas_libres) == 0:
                    self.tablero.imprimir_tablero()
                    print("¡Empate!")
                    if self.reiniciar_juego():
                        self.tablero = Tablero(self.tablero.filas, self.tablero.columnas)
                        self.jugador_actual = self.jugador_2_simbolo
                    else:
                        break
                self.cambiar_turno()

if __name__ == "__main__":

    entrada = -1

    filas = -1
    columnas = -1

    nombre_jugador_1 = ""
    nombre_jugador_2 = ""

    # Solicitar al usuario el tamaño de columnas del tablero
    while True:
        try:
            columnas = int(input("Ingrese el numero de columnas que tendra el juego: "))
            if columnas > 4:
                break
            else:
                print("El numero ingresado debe ser mayor a 4")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Solicitar al usuario el tamaño de filas del tablero
    while True:
        try:
            filas = int(input("Ingrese el numero de filas que tendra el juego: "))
            if filas > 4:
                break
            else:
                print("El numero ingresado debe ser mayor a 4")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    # Preguntar por el nombre del jugador 1
    nombre_jugador_1 = input("Ingrese el nombre del jugador 1: ")

    # Preguntar por el nombre del jugador 2
    nombre_jugador_2 = input("Ingrese el nombre del jugador 2: ")

    # [4] Empaquetar las variables
    jugadores = (nombre_jugador_1, nombre_jugador_2)
    tamaño = (filas, columnas)

    juego = JuegoConectaCuatro(tamaño, jugadores, "🦔", "🤙", "🔥", "😎", "😋", "🥲", "🦆", "🌟", "🪐", "🌱", "🐈")

    Tablero.imprimir_tamaño_tablero(juego.tablero.tablero)

    juego.jugar()
