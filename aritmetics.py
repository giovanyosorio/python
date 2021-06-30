menu = """

BIENVENIDO CONVERSOR DE MONEDAS .

1_ DOLARES A PESO COLOMBIANO
2_ DOLARES A PESO ARGENTINO
3_ DOLARES A PESOS MEXICANOS 

ELIGE UNA OPCION: """

opcion = int(input(menu))

if opcion == 1:

    pesos = input('ingresa dolares ? : ')
    pesos = float(pesos)
    valor_colombiano = 3875
    dolares = pesos * valor_colombiano
    dolares = str(dolares)
    print(' tienes en dolares $ ' + dolares)

elif opcion == 2:

    pesos = input('ingresa dolares ? : ')
    pesos = float(pesos)
    valor_colombiano = 95
    dolares = pesos * valor_colombiano
    dolares = str(dolares)
    print(' tienes en dolares $ ' + dolares)


elif opcion == 3:

    pesos = input('ingresa dolares ? : ')
    pesos = float(pesos)
    valor_colombiano = 20
    dolares = pesos * valor_colombiano
    dolares = str(dolares)
    print(' tienes en dolares $ ' + dolares)

else:
    print('ingresa una opcion correca')
