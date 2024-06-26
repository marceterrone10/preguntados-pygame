import pygame
import random

ahorcado = {"Palabras":
[
{"id":1, "ES": "elefante", "EN": "elephant"},
{"id":2, "ES": "departamento", "EN": "department"},
{"id":3, "ES": "medicina", "EN": "medicine"},
{"id":4, "ES": "ingenieria", "EN": "engineering"},
{"id":5, "ES": "computadora", "EN": "computer"},
{"id":6, "ES": "dispositivo", "EN": "device"},
{"id":7, "ES": "software", "EN": "software"},
{"id":8, "ES": "hardware", "EN": "hardware"},
{"id":9, "ES": "idioma", "EN": "language"},
{"id":10, "ES": "ciudadano", "EN": "citizen"}
]
}

# Ahorcado:
# Lista de diccionarios
# Se elegirá el idioma a jugar, palabras en español o en inglés.

# Se tendrán tantos intentos como letras tenga la palabra

# cada palabra adivinada suma un punto por letra de la misma

# La figura del ahorcado será: 
#  - círculo para la cabeza.
#  - rectángulo para el tórax.
#  - líneas para brazos y piernas.

# La app debe tener un botón de inicio de juego
# una vez iniciado el mismo se debe colocar el nick del jugador en una caja de texto
# Debe tener también otro botón para cerrar el juego (No hacerlo desde la X)
# Debe tener un botón para mutear / desmutear el audio
# Debe tener a la vista los puntos acumulados
# Luego de cada partida, debe guardar en un archivo los siguientes datos:
# Nick y puntaje
# Debe mostrarse el top 3 de los mejores puntajes en la pantalla inicial.


pygame.init() #Se inicializa pygame

screen = pygame.display.set_mode([1280, 720]) #Se crea una ventana
rect_boton_jugar = pygame.Rect(490, 150, 290, 70)
rect_boton_puntaje = pygame.Rect(490, 260, 290, 70)
rect_boton_salir = pygame.Rect(490, 370, 290, 70)

rect_boton_lenguaje = pygame.Rect(990, 30, 290, 70)

font = pygame.font.SysFont("Arial Narrow", 50)
text_start = font.render("Start", True, (0, 255, 0))
text_puntaje = font.render("Puntaje", True, (0, 255, 0))
text_salir = font.render("Salir", True, (0, 255, 0))
text_lenguaje = font.render("Español", True, (247, 252, 247))

esta_jugando = False

espaniol = True
idioma = ""

running = True
while running:
    
    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse down: {event.pos}")
            if rect_boton_jugar.collidepoint(event.pos):
                esta_jugando = True
                #print("Apreto start")
            
            if rect_boton_puntaje.collidepoint(event.pos):
                print("Apreto puntaje")
            
            if rect_boton_salir.collidepoint(event.pos):
                running = False
            
            if rect_boton_lenguaje.collidepoint(event.pos):
                if espaniol == True:
                    idioma = "Español"
                    espaniol = False
                else:
                    idioma = "English"
                    espaniol = True
    
    
    if esta_jugando == False:
        screen.fill((140, 229, 245))# Se pinta el fondo de la ventana
        pygame.draw.rect(screen, (245, 51, 44), rect_boton_jugar, border_radius=15)
        pygame.draw.rect(screen, (245, 51, 44), rect_boton_puntaje, border_radius=15)
        pygame.draw.rect(screen, (245, 51, 44), rect_boton_salir, border_radius=15)
        screen.blit(text_start, (600, 170))
        screen.blit(text_puntaje, (580, 280))    
        screen.blit(text_salir, (600, 390))
    
    else:
        screen.fill((134, 235, 134))
        pygame.draw.rect(screen, (245, 51, 44), rect_boton_lenguaje, border_radius=15)
        text_lenguaje = font.render(idioma, True, (247, 252, 247))
        screen.blit(text_lenguaje, (560, 170))
    
    
    pygame.display.flip()# Muestra los cambios en  la pantalla

pygame.quit() # Fin