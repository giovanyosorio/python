def es_primo(numero):
    contador = 0

    for i in range(1, numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        True


def run():
    numero = int(print('escribe un numero: '))
    if es_primo(numero):
        print('es primo ')
    else:
        print('no es primo')


if __name__ == '__main__':
    run()
