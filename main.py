import random

num = random.randint(1,100)
intentos = 0

while True:
    entrada = input("Adivina un número del 1 al 100: ")
    intentos += 1

    # Si el número del usuario no es un dígito...
    if not entrada.isdigit():
        print("Por favor, introduce un número.")
    # Si el número del usuario no está entre el 1 y el 100...
    elif int(entrada) <= 0 or int(entrada) >= 100:
        print("El número debe ser entre el 1 y el 100.")
    else:
        # Si el usuario acierta el número...
        if int(entrada) == num:
            print("Eres bueno... Enhorabuena. Has hecho {0} intentos.".format(intentos))
            break
        # Si el número del usuario es menor que el número generado aleatoriamente...
        elif int(entrada) < num:
            print("El número es mayor.")
        # Si el número del usuario es mayor que el número generado aleatoriamente...
        elif int(entrada) > num:
            print("El número es menor.")