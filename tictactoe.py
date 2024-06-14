import pygame

# Función para graficar el tablero en la pantalla
def graficar_board():
    screen.blit(fondo, (0, 0))  # Dibuja el fondo del tablero
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == 'x':
                dibujar_x(fila, col)  # Dibuja 'x' si el tablero en esa posición es 'x'
            elif tablero[fila][col] == 'o':
                dibujar_o(fila, col)  # Dibuja 'o' si el tablero en esa posición es 'o'
    pygame.display.update()  # Actualiza la pantalla

# Función para dibujar 'x' en la posición indicada
def dibujar_x(fila, col):
    screen.blit(equis, coor[fila][col])

# Función para dibujar 'o' en la posición indicada
def dibujar_o(fila, col):
    screen.blit(circulo, coor[fila][col])

# Función para verificar si hay un ganador
def verificar_ganador():
    for i in range(3):
        # Verifica filas
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return True
        # Verifica columnas
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
            return True
    # Verifica diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
        return True
    return False

# Función principal para correr el juego
def pptictactoe():
    global screen, fondo, circulo, equis, coor, tablero

    turno = 'x'  # Comienza el turno de 'x'
    game_over = False
    clock = pygame.time.Clock()

    pygame.init()  # Inicializa Pygame
    screen = pygame.display.set_mode((450, 450))  # Configura el tamaño de la pantalla
    pygame.display.set_caption("Tres En Raya")  # Establece el título de la ventana

    # Carga y escala las imágenes
    fondo = pygame.image.load('Tictactoe/static/tictactoe_background.png')
    circulo = pygame.image.load('Tictactoe/static/circle.png')
    equis = pygame.image.load('Tictactoe/static/x.png')

    fondo = pygame.transform.scale(fondo, (450, 450))
    circulo = pygame.transform.scale(circulo, (125, 125))
    equis = pygame.transform.scale(equis, (125, 125))

    # Coordenadas para colocar las imágenes en la cuadrícula
    coor = [[(40, 50), (165, 50), (290, 50)],
            [(40, 175), (165, 175), (290, 175)],
            [(40, 300), (165, 300), (290, 300)]]

    # Inicializa el tablero vacío
    tablero = [['', '', ''],
               ['', '', ''],
               ['', '', '']]

    while not game_over:
        clock.tick(30)  # Controla la velocidad del bucle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Verifica si se cierra la ventana
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Verifica si se hace clic con el mouse
                mouseX, mouseY = event.pos  # Obtiene las coordenadas del clic
                if (mouseX >= 40 and mouseX < 415) and (mouseY >= 50 and mouseY < 425):  # Verifica si el clic está dentro del tablero
                    fila = (mouseY - 50) // 125  # Calcula la fila del clic
                    col = (mouseX - 40) // 125  # Calcula la columna del clic
                    if tablero[fila][col] == '':  # Verifica si la celda está vacía
                        tablero[fila][col] = turno  # Marca la celda con el turno actual
                        if verificar_ganador():  # Verifica si hay un ganador
                            print("El jugador {} es el ganador".format(turno))
                            game_over = True
                        else:
                            turno = 'o' if turno == 'x' else 'x'  # Cambia el turno
        graficar_board()  # Actualiza el tablero en la pantalla

    pygame.quit()  # Cierra Pygame al finalizar el juego
