def run():
    # nombre = input('escribe tu nombre: ')
    # for letra in nombre:
    #     print(letra)
    frase = input(' escribe una frase : ')
    for caracter in frase:
        print(caracter.upper().replace('', '-'))


if __name__ == '__main__':
    run()
