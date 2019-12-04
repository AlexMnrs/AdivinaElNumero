import random

num = random.randint(1,100)
intentos = 0

while True:
    entrada = input("Adivina un número del 1 al 100: ")
    intentos += 1

    if not entrada.isdigit():
        print("Por favor, introduce un número.")
    elif int(entrada) <= 0 or int(entrada) >= 100:
        print("El número debe ser entre el 1 y el 100.")
    else:
        if int(entrada) == num:
            print("Eres bueno... Enhorabuena. Has hecho {0} intentos.".format(intentos))
            break
        elif int(entrada) < num:
            print("El número es mayor.")
        elif int(entrada) > num:
            print("El número es menor.")