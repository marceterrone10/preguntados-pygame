import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marcelo Ariel
apellido: Terrone
Instancia: Examen
Division: F
Fecha: 1/03/2024
DNI: 44935738

De los 50 participantes del torneo de UTN-TETRIS, se debe ingresar los siguientes datos:
Nombre
Categoría (Principiante - Intermedio - Avanzado)
Edad (entre 18 y 99 inclusive)
Score (mayor que 0)
Nivel alcanzado (1 , 2 o 3)

Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál es la categoría que tiene más participantes.
Informe B- El Porcentaje de jugadores de la categoría avanzado sobre el total
Informe C- La categoría del participante de menor Score
Informe D- El score y nombre del avanzado con mayor edad
Informe E- Promedio de score de los participantes principiantes.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        # De los 50 participantes del torneo de UTN-TETRIS, se debe ingresar los siguientes datos:
        # Nombre
        # Categoría (Principiante - Intermedio - Avanzado)
        # Edad (entre 18 y 99 inclusive)
        # Score (mayor que 0)
        # Nivel alcanzado (1 , 2 o 3)


        contador_cat_principiante = 0
        contador_cat_intermedio = 0
        contador_cat_avanzado = 0

        min_categoria = ''
        min_categoria_score = 0
        bandera_categoria_min = True

        max_nombre_avanzado = ''
        max_score_avanzado = 0
        bandera_max_score_avanzado = True

        acumulador_score_principiante = 0

        for _ in range(50):
            
            nombre_ingresado = prompt(None, 'Ingrese su nombre:')

            categoria_ingresada = prompt(None, 'Ingrese su categoria: ')
            while categoria_ingresada != 'Principiante' and categoria_ingresada != 'Intermedio' and categoria_ingresada != 'Avanzado':
                categoria_ingresada = prompt(None, 'Re ingrese su categoria (Principiante/Intermedio/Avanzado): ')
            
            edad_ingresada = int(prompt(None, 'Ingrese su edad: '))
            while edad_ingresada < 18 or edad_ingresada > 99:
                edad_ingresada = int(prompt(None, 'Re ingrese su edad(18 a 99): '))

            score_ingresado = int(prompt(None, 'Ingrese su score: '))
            while score_ingresado < 0:
                score_ingresado = int(prompt(None, 'Re ingrese su score (Debe ser mayor a 0): '))

            nivel_alcanzado = int(prompt(None, 'Ingrese su nivel alcanzado: '))
            while nivel_alcanzado != 1 and nivel_alcanzado != 2 and nivel_alcanzado != 3:
                nivel_alcanzado = int(prompt(None, 'Re ingrese su nivel alcanzado (1/2/3): '))

            # Informe A- Cuál es la categoría que tiene más participantes.
            # Informe B- El Porcentaje de jugadores de la categoría avanzado sobre el total
            # Informe C- La categoría del participante de menor Score
            # Informe D- El score y nombre del avanzado con mayor edad
            # Informe E- Promedio de score de los participantes principiantes.
                
            if categoria_ingresada == 'Principiante':
                contador_cat_principiante += 1
                acumulador_score_principiante += score_ingresado
            elif categoria_ingresada == 'Intermedio':
                contador_cat_intermedio += 1
            else:
                contador_cat_avanzado += 1
                if bandera_max_score_avanzado == True or score_ingresado > max_score_avanzado:
                    max_score_avanzado = score_ingresado
                    max_nombre_avanzado = nombre_ingresado
                    bandera_max_score_avanzado = False


            if bandera_categoria_min == True or score_ingresado < min_categoria_score:
                min_categoria_score = score_ingresado
                min_categoria = categoria_ingresada
                bandera_categoria_min = False

        
        contador_total_categorias = contador_cat_avanzado + contador_cat_intermedio + contador_cat_principiante
        
        #INFORME A)
        if contador_cat_principiante > contador_cat_avanzado and contador_cat_principiante > contador_cat_intermedio:
            print('La categoria que tiene mas participantes es la Principiante')
        elif contador_cat_intermedio > contador_cat_avanzado:
            print('La categoria que tiene mas participantes es la Intermedio')
        else:
            print('La categoria que tiene mas participantes es la Avanzado')

        porcentaje_jugadores_cat_avanzado = (contador_cat_avanzado / contador_total_categorias) * 100

        if contador_cat_principiante != 0:
            promedio_score_principiantes = (acumulador_score_principiante / contador_cat_principiante)
        else:
            print('No hay participantes en la categoria principiante')

        #INFORME B)
        print(f'El porcentaje de jugadores de la categoria avanzado sobre el total es de {porcentaje_jugadores_cat_avanzado}%')
        #INFORME C)
        print(f'La categoria con el participante de menor score es {min_categoria}')
        #INFORME D)
        print(f'El score del avanzado con mayor edad es {max_score_avanzado} y su nombre es {max_nombre_avanzado}')
        #INFORME E)
        print(f'El promedio del score de los participantes en la categoria principiante es de {promedio_score_principiantes}')



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
