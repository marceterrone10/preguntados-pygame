'''
Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
a. Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
b. Mostrar la cantidad de números positivos y negativos.
c. Mostrar la sumatoria de los números pares.
d. Informar el mayor de los números impares.
e. Listar todos los números ingresados.
f. Listar todos los números pares.
g. Listar los números de las posiciones impares.  
h. Salir
Notas:
- Solo se podrá ingresar a las opciones b-g, siempre y cuando el usuario haya ingresado los datos solicitados.
- Todas las opciones deberán ser programadas en funciones: habrá funciones específicas (por ejemplo para determinar 
si un número es positivo o negativo) y funciones de nivel general (por ejemplo una función que liste los números pares). 
Tener en cuenta las características de la programación funcional.
'''

continuar = True
lista = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
contador = 0
contador_positivos = 0
contador_negativos = 0


while continuar == True:

    opcion = int(input("== Menu ==\n1. Ingrese los numeros\n2. Mostrar la cantidad de numeros positivos y negativos\n3. Mostrar la sumatoria de numeros pares\n4. Informar el numero mayor de los negativos\n5. Listar numeros \n6. Listar numeros pares \n7. Listar los numeros inpares \n8. Salir \nIngrese una opcion: "))

    match opcion:
        case 1:
            if contador < len(lista):
                for i in range(len(lista)):
                    if lista[i] == 'A':
                        numero = int(input('Ingrese un numero entre -1000 y 1000: '))
                        while numero < -1000 or numero > 1000:
                            numero = int(input('Re ingrese un numero entre -1000 y 1000: '))
                        lista[i] = numero
                        contador += 1
                        if numero < 0:
                            contador_negativos += 1
                        else:
                            contador_positivos += 1
                        break
            else:
                print('La lista esta llena!')
        case 2:
            if contador != 0:
                print(f'La cantidad de numeros positivos es de {contador_positivos}')
                print(f'La cantidad de numeros negativos es de {contador_negativos}')
            else:
                print('La lista esta vacia')
        case 3:
            if contador != 0:
                acumulador_numeros_pares = 0
                for numero in lista:
                    if numero != 'A' and numero % 2 == 0:
                        acumulador_numeros_pares += numero
                print(acumulador_numeros_pares)
            else:
                print('La lista esta vacia')
        case 4:
            if contador != 0:
                bandera_minimo = True
                numero_mayor_negativo = 0
                if numero < 0:
                    if bandera_minimo == True or numero_mayor_negativo > numero:
                        numero_mayor_negativo = numero
                        bandera_minimo = False
                print(f'El numero mayor negativo es {numero_mayor_negativo}')
            else:
                print('La lista esta vacia!')
        case 5:
            if contador != 0:
                for numero in lista:
                    if numero != 'A':
                        print(numero)
            else:
                print('La lista esta vacia!')
        case 6:
            if contador != 0:
                for numero in lista:
                    if numero != 'A' and numero % 2 == 0:
                        print(numero)
            else:
                print('La lista esta vacia!')
        case 7:
            if contador != 0:
                for i in range(len(lista)):
                    if i != 'A' and i % 2 != 0:
                        print(lista[i])
            else:
                print('La lista esta vacia!')
        case 8:
            continuar = False

                       

                
                  
                  
