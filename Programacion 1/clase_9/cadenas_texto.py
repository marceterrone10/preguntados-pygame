tupla = (1, 2, 3)
lista = [1, 2, 3]
#la tupla es inmutable y la lista es mutable
numero_a = 5
numero_b = 10

texto = "Los numeros son: {} {} ".format(numero_a, numero_b)
print(texto)
#con el .format le pasas los valores entre el()
#tambien puedo poner entre los {} las letras y en el () ponerle la letra y su igualdad

#f-string
numero = 5
texto = f"Mi numero es: {numero}"
print(texto)

#f-string con funciones
def imprimir():
    return "Hola"

texto = f"Mi numero es : {imprimir()}" 
print(texto)

#formateo de cadena #se imrpime el hola tres veces
saludo = "Hola" * 3
print(saludo)

#string dentro de otro string  #in/not
resultado = "Cielo" in "Rascacielos"
print(resultado)

#castear datos a string (str)
lista = [1,2,3]
print(type(str(lista)))

#mostrar letras por separado
saludo = "Hola mundo"

#normal
for letra in saludo:
    print(letra)

#con la funcion len
for i in range(len(saludo)):
    print(saludo(i))

#imprimir solo una palabra de un texto/str
saludo = "Hola mundo"
subcadena = saludo[5:10] #dentro del [] le decis el rango de la palabra a imprimir

print(subcadena)

#para borrar un texto #del=borrar
text = "Este es un texto de ejemplo"
del text

#remplazar  #dentro del () le pones la letra que deseas remplazar y luego por la letra que deseas insertar en ese lugar
saludo = "Hola mundo"
saludo = saludo.replace("o", "r")

print(saludo)

#split divide cadenas en subcadenas
saludo = "Hola mundo Adios"
saludo = saludo.split(" ")

print(saludo)
print(type(saludo))

#join #unir iterables y devolverlos en string
saludo = ["Hola", "mundo", "Adios"]
separador = ", "

resultado = separador.join(saludo)
print(resultado)

#zfil  #rellena con 0 adelante del string #el numero que se ingresa en el () son la cantidad de 0 pero se cuentan los digitos del str, osea que si queremos cuatro ceros pondremos 6
edad = "15" 
edad = edad.zfill()

#isalpha #te da un booleano por cada caracter alfabetico (si hay un espacio da FALSE)
saludo = "Hola mundo"
resultado = saludo.isalpha()

print(resultado)

#isalnum
saludo = "Hola mundo2"
resultado = saludo.isalnum()

print(resultado)

#count  #cuenta la cantidad de un caracter en especifico que le pases en el ()
saludo = "Hola mundo2"
resultado = saludo.count()

print(resultado)

#slice
saludo = "Hola mundo"
sub_string = saludo[5:]

print(sub_string)
