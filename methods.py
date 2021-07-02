nombre = input('cual es tu nombre ')
print(nombre.capitalize())  # primera en mayuscula

print(nombre.upper())  # todas en mayusculas
print(nombre.lower())  # todas en minusculas

print(nombre.strip())  # eliminar espacios basura

# indices
print(nombre.replace('o', 'a'))  # replace all vocals o with a
print(nombre[0])

print(nombre.__len__())  # canidad de caracteres
