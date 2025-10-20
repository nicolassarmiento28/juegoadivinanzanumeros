
import random
#juego adivinanza

def juego_adivinanza():

    # GENERAR UN NMERO DEL 1 AL 100

    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False

    #Primeras lineas de codigo
    print("Bienvenido al juego de adivinanza de numero secreto")
    print("Debes adivinar un numero secreto del 1 al 100")
    print("Intenta adivinarlo")

    while not adivinado:
        #solicitar un numero del 1 al 100
        adivinanza = input("Introduzca un numero del 1 al 100: ")

        #Verificar que la entrada sea un numero
        if adivinanza.isdigit():
            adivinanza =int(adivinanza) # lo pasamos de string a numero entero
            intentos += 1 

            # Verificar que el número esté en el rango correcto
            if adivinanza < 1 or adivinanza > 100:
                print("Por favor ingrese un número válido entre el 1 y el 100:")
                continue

            if adivinanza < numero_secreto:
                print(f"el numero secreto es mayor a {adivinanza}")
                

            elif adivinanza > numero_secreto:
                print(f"el numero secreto es menor a {adivinanza}")

            else:
                print(f"Felicitaciones has adivinado el numero secreto {adivinanza} en {intentos} intentos")

                adivinado = True  #Salir del bucle
            
        else:
            print("Por favor ingrese un numero valido entre el 1 y el 100:")

juego_adivinanza() #llamar a la funcion
