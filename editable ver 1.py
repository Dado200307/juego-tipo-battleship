    #planeacion de la idea del juego.
    #Se propone hacer un juego de buscaminas
    #se propone hacer un juego del gato (ese de x y o)
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
