def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_inver = palabra[::-1]
    if palabra_inver == palabra:
        return True
    else:
        return False


def run():
    palabra = input('Escribe la palabra :')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()
