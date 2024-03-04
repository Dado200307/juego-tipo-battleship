class Tablero:
    def __init__(self, filas=6, columnas=7):
        # Inicializa el tablero con el tamaño especificado.
        self.filas = filas
        self.columnas = columnas
        self.tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

    def imprimir_tablero(self):
        # Imprime el estado actual del tablero en la consola.
        for fila in self.tablero:
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
                if all(self.tablero[fila][columna + i] == jugador for i in range(4)):
                    return True

        for columna in range(self.columnas):
            for fila in range(self.filas - 3):
                if all(self.tablero[fila + i][columna] == jugador for i in range(4)):
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

