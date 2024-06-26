# Ejercitación programación orientada a objetos:

# Una empresa de tecnología nos pide desarrollar un software para su más reciente
# invención: la “SmartPen”.
# Los requisitos planteados por parte de la empresa son los siguientes:
# ● El código debe desarrollarse dentro un módulo llamado “class_boligrafo” en una
# clase llamada Bolígrafo.
# ● Los atributos serán los siguientes:
# - capacidad_tinta_maxima
# - grosor_punta
# - color
# - cantidad_tinta
# ● Al crearse una nueva instancia de la clase Bolígrafo, la misma siempre se creará con
# una capacidad de tinta máxima de 100 (El constructor no recibirá este parámetro)
# ● Al crearse una nueva instancia de la clase Bolígrafo la cantidad de tinta siempre
# comenzará siendo de 80 (El constructor no recibirá este parámetro)
# ● Al crearse una nueva instancia de la clase Bolígrafo se podrá elegir el color del
# mismo (El constructor recibirá un string indicando el color y lo guardará en el
# atributo)
# ● Al crearse una nueva instancia de la clase Bolígrafo se podrá elegir el grosor de la
# punta del mismo (El constructor recibirá un string indicando el grosor y lo guardará
# en el atributo)
# ● Los métodos de instancia serán los siguientes:
# ● escribir(texto)
# - Deberá validar si el bolígrafo cuenta con la tinta suficiente para escribir el
# texto: La tinta a ser gastada corresponde a la cantidad de caracteres (Ej: el
# texto “hola” gasta 4 de tinta)
# - En caso de contar con la tinta suficiente, deberá restarse la cantidad del
# atributo cantidad_tinta y devolver una cadena con el texto recibido por
# parámetro.
# - En caso de no contar con la tinta suficiente deberá retornar la cadena “No
# alcanza la tinta”.
# ● recargar(cantidad)
# -Deberá sumarse la cantidad de tinta recibida por parámetro al atributo
# cantidad_tinta.
# -Deberá validarse que la tinta recargada no supere el valor establecido por el
# atributo cantidad_tinta_maxima. (Ej: Si el bolígrafo tiene 50 de tinta y el
# parámetro cantidad es 60 debe establecerse cantidad_tinta en 100, no en
# 110, pues ese es el valor establecido como máximo en el atributo
# cantidad_tinta_maxima.
# -Si la cantidad recargada no excede el máximo deberá retornarse la cadena
# “Lapicera recargada”.
# - Si la cantidad recargada excede el máximo deberá retornarse la cadena “Se
# recargó la lapicera y sobró __ cantidad de tinta. (Rellenar el espacio con el
# valor que se haya excedido)
# En el módulo Main, crear un bolígrafo de tinta “Azul” y un grosor “Fino” y otro de tinta “Rojo”
# y un grosor “Grueso”
# Utilizar todos los métodos y mostrar los resultados por consola.