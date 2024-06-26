from os import system

#       ["Juan", "Pepe", "A", "A", "A"]
lista = ["A", "A", "A", "A", "A"]
#indices [0, 1, 2, 3, 4]
continuar = True
contador = 0


while continuar == True:

    opcion = input("== Menu ==\n1. Alta\n2. Listar\n3. Baja\n4. Salir\nIngrese una opcion: ")
    system("cls") 
    match opcion:
        case "1":
            if contador < len(lista):
                for i in range(len(lista)):
                    if lista[i] == "A":
                        nombre = input(f"Ingrese el {i + 1}° nombre: ")
                        lista[i] = nombre
                        contador += 1
                        break
            else:
                print("La lista esta llena!")
        case "2":
            if contador != 0:
                for nombre in lista:
                    if nombre != "A":
                        print(nombre)
            else:
                print("La lista esta vacia.")
        case "3":
            if contador != 0:
                encontrado = False
                nombre_a_eliminar = input("Ingrese el nombre a eliminar: ")
                for i in range(len(lista)):
                    if nombre_a_eliminar == lista[i]:
                        confirmacion = input(f"Esta seguro que desea eliminar a {nombre_a_eliminar}? S/N: ")
                        if confirmacion == "S":
                            encontrado = True
                            lista[i] = "A"
                            contador -= 1
                        break
                if encontrado == True:
                    print("Se elimino exitosamente.")
                else:
                    print("No se elimino a la persona.")
            else:
                print("La lista esta vacia.")
        case "4":
            continuar = False
        case _:
            print("La opcion ingresada es incorrecta.")
    
    #system("pause")
    #system("cls") 

print("Programa finalizado.")
