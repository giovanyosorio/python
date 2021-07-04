import random


def generate_password():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '0']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '?', '#', '&', '$', '¡']
    caracteres = mayusculas+minusculas+simbolos+numeros

    password = []
    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = ''.join(password)
    return password


def run():
    password = generate_password()
    print('new password is ' + ' ' + password)


if __name__ == '__main__':
    run()
