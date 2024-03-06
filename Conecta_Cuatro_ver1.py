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


class JuegoConectaCuatro:
    def __init__(self):
        # Inicializa el juego creando un objeto Tablero y configurando el primer jugador como 'X'.
        self.tablero = Tablero()
        self.jugador_actual = 'X'

    def cambiar_turno(self):
        # Cambia el turno entre jugadores 'X' y 'O'.
        self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'

    def obtener_columna_valida(self):
        # Solicita al jugador actual que elija una columna válida.
        while True:
            try:
                columna = int(input(f"Jugador {self.jugador_actual}, elige una columna (0-{self.tablero.columnas - 1}): "))
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
                print("Respuesta inválida. Por favor, ingresa 'Sí' o 'No'.")

    def jugar(self):
        # Bucle principal del juego.
        while True:
            self.tablero.imprimir_tablero()
            columna = self.obtener_columna_valida()
            if self.tablero.realizar_movimiento(columna, self.jugador_actual):
                if self.tablero.verificar_ganador(self.jugador_actual):
                    self.tablero.imprimir_tablero()
                    print(f"¡Jugador {self.jugador_actual} ha ganado!")
                    if self.reiniciar_juego():
                        self.tablero = Tablero()
                        self.jugador_actual = 'X'
                    else:
                        break
                elif all(cell != ' ' for row in self.tablero.tablero for cell in row):
                    self.tablero.imprimir_tablero()
                    print("¡Empate!")
                    if self.reiniciar_juego():
                        self.tablero = Tablero()
                        self.jugador_actual = 'X'
                    else:
                        break
                self.cambiar_turno()

if __name__ == "__main__":
    juego = JuegoConectaCuatro()
    juego.jugar()
