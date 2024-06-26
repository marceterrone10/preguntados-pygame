#Listas anidadas

#Indices    [     0     ,       1    ,        2    ]
personas = [['Ana', 23], ['Raul', 30], ['Pepe', 18]]

print(f'La edad de Raul es {personas[1][1]}')


for per in personas:
    print(f'{per[0]} tiene {per[1]} anos')

#===================================================================


for indice in range(len(personas)):
    print(f'{personas[indice][0]} tiene {personas[indice][1]} anos')

for i in range(len(personas)):
    for j in range(len(personas[i])):
        if j == 0:
            nombre = personas[i][j]
        else:
            edad = personas[i][j]
    print(f"{nombre} tiene {edad} años")