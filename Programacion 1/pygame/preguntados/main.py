import pygame
from datos import lista

pygame.init() #inicializar pygame

screen = pygame.display.set_mode((1280, 720)) #creo ventana con dimensiones 500x500px
pygame.display.set_caption("Preguntados")
#botones y colores
rect_boton_jugar = pygame.Rect(490, 250, 290, 70)
rect_boton_puntajes = pygame.Rect(490, 360, 290, 70)
rect_boton_salir = pygame.Rect(490, 470, 290, 70)
rect_boton_sonido = pygame.Rect(1150, 20, 100, 50)
rect_boton_pregunta = pygame.Rect(450, 20, 390, 100)
rect_boton_reiniciar = pygame.Rect(450, 200, 390, 100)

contenedor_preguntas = pygame.Rect(50, 350, 1180, 150)
contenedor_respuesta_a = pygame.Rect(50, 550, 300, 100)
contenedor_respuesta_b = pygame.Rect(880, 550, 300, 100)
contenedor_respuesta_c = pygame.Rect(450, 550, 300, 100)


color_rojo = 255,0,0
color_amarillo = 255, 179, 0
color_celeste = 135, 206, 235
color_verde = 0, 255, 0

#logo / fondos
logo_preguntados = pygame.image.load('Programacion 1/pygame/preguntados/logo_preguntados.png')
logo_preguntados = pygame.transform.scale(logo_preguntados, (150, 150))
fondo_inicio = pygame.image.load('Programacion 1/pygame/preguntados/maxresdefault.jpg')
#textos
font = pygame.font.SysFont('Arial Narrow', 50)
font_puntajes = pygame.font.SysFont('Arial Narrow', 40)
font_unmute = pygame.font.SysFont('Arial Narrow', 30)
font_preguntas = pygame.font.SysFont('Arial Narrow', 60)
texto_pregunta = font_preguntas.render('Pregunta', True, (255,255,255))
texto_reiniciar = font_preguntas.render('Reiniciar', True, (255,255,255))

texto_jugar = font.render('Jugar', True, (255, 255, 255))
texto_puntajes = font_puntajes.render('Ver puntajes', True, (255, 255, 255))
texto_salir = font.render('Salir', True, (255, 255, 255))
texto_mute = font_puntajes.render('Mute', True, (255, 255, 255))
texto_unmute = font_unmute.render('Unmute', True, (255, 255, 255))


#sonidos
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)

pygame.mixer.music.load('Programacion 1/pygame/preguntados/soundtrack_fondo.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.05)


sonido_on = True
jugando = False
running = True
pantalla = 'inicio'
mostrar_contenedor = False
contador_pregunta = 0
intentos = 2
puntos = 0
respuestas_incorrectas = []

def render_preguntas(index_pregunta:int):
    pregunta = lista[index_pregunta]
    texto_question = font.render(pregunta['pregunta'], True, (0,0,0))
    respuesta_a = font.render('a )' + pregunta['a'], True, (0,0,0) )
    respuesta_b = font.render('b )' + pregunta['b'], True, (0,0,0) )
    respuesta_c = font.render('c )' + pregunta['c'], True, (0,0,0) )   
    texto_puntos = font.render(f'+{puntos} puntos', True, (0,0,0))
    texto_intentos = font.render(f'{intentos} intentos', True, (0,0,0))

    screen.blit(texto_intentos, (1089, 260))
    screen.blit(texto_puntos, (1089, 138))
    screen.blit(texto_question, (60, 360) )

    if 'a' not in respuestas_incorrectas:
        screen.blit(respuesta_a, (60, 550))
    else:
        pygame.draw.rect(screen, (0,0,255), contenedor_respuesta_a)
    if 'b' not in respuestas_incorrectas:
        screen.blit(respuesta_b, (450, 550))
    else:
        pygame.draw.rect(screen, (0,0,255), contenedor_respuesta_c)
    if 'c' not in respuestas_incorrectas:
        screen.blit(respuesta_c, (880, 550))
    else:
        pygame.draw.rect(screen, (0,0,255), contenedor_respuesta_b)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse down: {event.pos}") 
            if event.type == pygame.MOUSEBUTTONUP:
                print(f"Mouse up: {event.pos}") #saber la pos del puntero
            

            if pantalla == 'inicio':
                if rect_boton_jugar.collidepoint(event.pos):
                    pantalla = 'preguntas'
                    intentos = 2
                if rect_boton_salir.collidepoint(event.pos):
                    running = False
            if pantalla == 'preguntas':
                if rect_boton_pregunta.collidepoint(event.pos):
                    mostrar_contenedor = True
                if mostrar_contenedor:
                    pregunta = lista[contador_pregunta]
                    if contenedor_respuesta_a.collidepoint(event.pos):
                        if pregunta['correcta'] == 'a':
                            contador_pregunta += 1
                            puntos += 10
                            texto_puntos = font.render(f'+{puntos} puntos', True, (0,0,0))
                            screen.blit(texto_puntos, (1089, 138))
                            mostrar_contenedor = False
                            intentos = 2
                            texto_intentos = font.render(f'{intentos} intentos', True, (0,0,0))
                            screen.blit(texto_intentos, (1089, 260))
                            respuestas_incorrectas = []
                        elif 'a' not in respuestas_incorrectas:
                            intentos -= 1
                            respuestas_incorrectas.append('a')

                    elif contenedor_respuesta_c.collidepoint(event.pos):
                        if pregunta['correcta'] == 'b':
                            contador_pregunta += 1
                            puntos += 10
                            texto_puntos = font.render(f'+{puntos} puntos', True, (0,0,0))
                            screen.blit(texto_puntos, (1089, 138))
                            mostrar_contenedor = False
                            intentos = 2
                            texto_intentos = font.render(f'{intentos} intentos', True, (0,0,0))
                            screen.blit(texto_intentos, (1089, 260))
                            respuestas_incorrectas = []
                        elif 'b' not in respuestas_incorrectas:
                            intentos -= 1
                            respuestas_incorrectas.append('b')    

                    elif contenedor_respuesta_b.collidepoint(event.pos): 
                        if pregunta['correcta'] == 'c':
                            contador_pregunta += 1
                            puntos += 10
                            texto_puntos = font.render(f'+{puntos} puntos', True, (0,0,0))
                            screen.blit(texto_puntos, (1089, 138))
                            mostrar_contenedor = False
                            intentos = 2
                            texto_intentos = font.render(f'{intentos} intentos', True, (0,0,0))
                            screen.blit(texto_intentos, (1089, 260))
                            respuestas_incorrectas = []
                        elif 'c' not in respuestas_incorrectas:
                            intentos -= 1
                            respuestas_incorrectas.append('c')    
                            
                    if intentos == 0:
                        contador_pregunta += 1
                        mostrar_contenedor = False
                        intentos = 2
                        respuestas_incorrectas = []                        

                if rect_boton_reiniciar.collidepoint(event.pos):
                    contador_pregunta = 0
                    puntos = 0
                    intentos = 2
                    respuestas_incorrectas = []

                if contador_pregunta >= len(lista):
                    pantalla = 'inicio'

            if rect_boton_sonido.collidepoint(event.pos):
                sonido_on = not sonido_on
                if sonido_on:
                    pygame.mixer.music.set_volume(0.05)
                else:
                    pygame.mixer.music.set_volume(0)
                        

    if pantalla == 'inicio':
        screen.blit(fondo_inicio, (0, 0))
        screen.blit(logo_preguntados, (550, 20))
        pygame.draw.rect(screen, (color_celeste), rect_boton_jugar, border_radius=10)
        screen.blit(texto_jugar, (580, 280))
        pygame.draw.rect(screen, (color_amarillo), rect_boton_puntajes, border_radius=10)
        screen.blit(texto_puntajes, (580, 390))
        pygame.draw.rect(screen, (color_rojo), rect_boton_salir, border_radius=10)
        screen.blit(texto_salir, (600, 500))
    if pantalla == 'preguntas':
        screen.fill((0,0,255))
        screen.blit(logo_preguntados, (100, 20))
        pygame.draw.rect(screen, (color_amarillo), rect_boton_pregunta, border_radius=10)
        screen.blit(texto_pregunta, (540, 60))
        pygame.draw.rect(screen, (color_amarillo), rect_boton_reiniciar, border_radius=10)
        screen.blit(texto_reiniciar, (540, 240))
        if mostrar_contenedor == True:
            pygame.draw.rect(screen, (255, 255, 255), contenedor_preguntas)
            pygame.draw.rect(screen, (255, 255, 255), contenedor_respuesta_a)
            pygame.draw.rect(screen, (255, 255, 255), contenedor_respuesta_b)
            pygame.draw.rect(screen, (255, 255, 255), contenedor_respuesta_c)                       
            render_preguntas(contador_pregunta)


    if sonido_on:
        pygame.draw.rect(screen, (color_verde), rect_boton_sonido)
        screen.blit(texto_mute, (1168,36))
    else:
        pygame.draw.rect(screen, (color_rojo), rect_boton_sonido)
        screen.blit(texto_unmute, (1168,36))
        


    pygame.display.flip()
    
pygame.quit()