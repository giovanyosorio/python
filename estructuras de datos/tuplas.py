# Tuplas: Son un tipo de objeto estatico dentro de python a diferencia de las listas que son un objeto dinamico, es decir son un tipo de dato que su valor no va a cambiar, al igual que cuando creamos una variable constante. Y al momento de realizar una iteracion en el codigo del proyecto tendremos mejores tiempo de cargas utilizando tuplas en vez de listas:

fruits = ("apple", "pear", "orange", "peach")

fruitToList = list(fruits)
fruitToList[0] = "berry"

fruits = tuple(fruitToList)

print(fruits)
print(type(fruits))
