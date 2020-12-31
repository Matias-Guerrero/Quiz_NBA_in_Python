import time
import msvcrt # Codigo para Abrir archivo desde la ventana de windows.
import os # Modulo os.system()
import pickle
import operator

# Se crea la funcion para limpiar pantalla.
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

# Funcion para guardar diccionario en archivo .pickle
def guardar_diccionario(diccionario):
    archivo = open('puntajes_dificil.pickle', 'wb')
    pickle.dump(diccionario, archivo)
    archivo.close()

def guardar_diccionario2(diccionario):
    archivo = open('puntajes_facil.pickle', 'wb')
    pickle.dump(diccionario, archivo)
    archivo.close()

# Funcion la cual ordena (de mayor a menor) un diccionario con respecto a sus valores (los cuales deben ser numeros).
def ordenar_valores(dicc):
    valores_ord = dict(sorted(dicc.items(), key=operator.itemgetter(1), reverse=True))
    return valores_ord

try:
    archivo = open('puntajes_dificil.pickle', 'rb')
    dicc_puntajes_dificil = pickle.load(archivo)
    archivo.close()
except:
    dicc_puntajes_dificil = {}

try:
    archivo = open('puntajes_facil.pickle', 'rb')
    dicc_puntajes_facil = pickle.load(archivo)
    archivo.close()
except:
    dicc_puntajes_facil = {}

borrarPantalla()
print()
print(chr(27)+"[4;37m"+"Bienvenidos al Quiz sobre la NBA.") # Texto subrayado (4) y en color negro (37m)
print(chr(27)+"[0m")
time.sleep(1)

while True:
    borrarPantalla()
    print()
    print(chr(27)+"[4;37m"+"Menu del Quiz:")
    print(chr(27)+"[0m")
    print("1. Comenzar Quiz.")
    print("2. Ver Puntuaciones.")
    print("3. Salir del Quiz.")
    print()
    try:
        desicion = input("¿Que deseas hacer?: ")
        if int(desicion) == 1:
            borrarPantalla()
            print()
            player = input("Para comenzar el quiz ingresa tu nombre o nickname: ")
            borrarPantalla()
            x = 0
            puntos = 0
            print()
            print("¿En que dificultad deseas jugar?")
            print()
            print("1. Dificil.")
            print("2. Facil.")
            print()
            try:
                desicion_dificultad = input("¿Que dificultad deseas?: ")
                if int(desicion_dificultad) == 1:
                    borrarPantalla()
                    while x < 11:
                        x = x + 1
                        if x == 1:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿En cuantos equipos jugó Shaquille O'Neal a lo largo de su carrera?")
                            time.sleep(0.5)
                            print()
                            print("[1] 4")
                            print("[2] 7")
                            print("[3] 6")
                            print("[4] 3")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()   
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 2:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Qué jugador tiene más apariciones en el mejor quinteto de la NBA?")
                            time.sleep(0.5)
                            print()
                            print("[1] Lebron James")
                            print("[2] Tim Duncan")
                            print("[3] Kobe Bryant")
                            print("[4] Michael Jordan")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 3:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Cuál es el único equipo que ha ganado hasta 17 encuentros en un mismo mes de liga regular?")
                            time.sleep(0.5)
                            print()
                            print("[1] Toronto Raptors")
                            print("[2] Los Angeles Lakers")
                            print("[3] Boston Celtics")
                            print("[4] Atlanta Hawks")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecto :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 4:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Quien es el jugador que mejor porcentaje contabilizable de triples ha registrado en una temporada?")
                            time.sleep(0.5)
                            print()
                            print("[1] Kyle Korver - Utah Jazz (2009-2010)")
                            print("[2] Steve Kerr - Chicago Bulls (1994-1995)")
                            print("[3] Dell Curry - Milwaukee Bucks (1998-1999)")
                            print("[4] J.J. Redick - Los Angeles Clippers (2015-2016)")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 5:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Con qué equipo ganó la NBA Moses Malone?.")
                            time.sleep(0.5)
                            print()
                            print("[1] New York Knicks")
                            print("[2] Philadelphia 76ers")
                            print("[3] Houston Rockets")
                            print("[4] San Antonio Spurs")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 6:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("En 2015 Orlando y Knicks superaron el récord de menos puntos conjuntados en un cuarto. ¿Cuantos puntos anotaron en total?")
                            time.sleep(0.5)
                            print()
                            print("[1] 21")
                            print("[2] 15")
                            print("[3] 17")
                            print("[4] 25")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 7:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Cual de estos jugadores no fue n°1 del draft?.")
                            time.sleep(0.5)
                            print()
                            print("[1] Chris Webber")
                            print("[2] Dikembe Mutombo")
                            print("[3] Allen Iverson")
                            print("[4] Kenyon Martin")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 8:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Quien pronuncio la siguiente frase? <<Siempre recordare esta noche como la noche en la ue Michael Jordan y yo nos combinamos para anotar 70 puntos (Jordan hizo 69 pts.)")
                            time.sleep(0.5)
                            print()
                            print("[1] Stacey King")
                            print("[2] Steve Kerr")
                            print("[3] Toni Kukoc")
                            print("[4] BJ Armstrong")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 9:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Cuántos anillos de campeón de la NBA ganó Dennis Rodman?.")
                            time.sleep(0.5)
                            print()
                            print("[1] 3")
                            print("[2] 5")
                            print("[3] 4")
                            print("[4] 6")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 10:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Cual de estos equipos tiene mas anillos de la nba?")
                            time.sleep(0.5)
                            print()
                            print("[1] Cleveland Cavaliers")
                            print("[2] New York Knicks")
                            print("[3] Milwaukee Bucks")
                            print("[4] Dallas Mavericks")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                    print()
                    print("Quiz Finalizado, gracias por responder.")
                    time.sleep(1)
                    print()
                    print("Cargando puntuacion ...")
                    time.sleep(1)
                    borrarPantalla()
                    print()
                    print(f"Has obtenido {puntos} puntos.")
                    print()
                    dicc_puntajes_dificil[player] = puntos
                    guardar_diccionario(dicc_puntajes_dificil)
                    time.sleep(1)
                    print("Para volver al menu presione cualquier tecla.")
                    msvcrt.getch()
                    continue
                elif int(desicion_dificultad) == 2:
                    borrarPantalla()
                    while x < 11:
                        x = x + 1
                        if x == 1:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Cuantos MVP de las Finales gano Michael Jordan?")
                            time.sleep(0.5)
                            print()
                            print("[1] 4")
                            print("[2] 7")
                            print("[3] 6")
                            print("[4] 5")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()   
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 2:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Que Jugador es famoso por ser el unico en anotar 100 pts en un partido?")
                            time.sleep(0.5)
                            print()
                            print("[1] Lebron James")
                            print("[2] Wilt Chamberlain")
                            print("[3] Kobe Bryant")
                            print("[4] Michael Jordan")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 3:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Cuál es la franquicia que no pertenece a los Estados Unidos?")
                            time.sleep(0.5)
                            print()
                            print("[1] Toronto Raptors")
                            print("[2] Memphis Grizzlies")
                            print("[3] Sacramento Kings")
                            print("[4] Golden State Warriors")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecto :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 4:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Que Franquicia es la que tiene el mejor record de temporada regular en la historia de la NBA?")
                            time.sleep(0.5)
                            print()
                            print("[1] Chicago Bulls")
                            print("[2] Boston Celtics")
                            print("[3] Los Angeles Lakers")
                            print("[4] Golden State Warriors")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 5:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿En qué año reveló Magic Johnson que tenía Sida?.")
                            time.sleep(0.5)
                            print()
                            print("[1] 1991")
                            print("[2] 1988")
                            print("[3] 1996")
                            print("[4] 2000")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 6:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Cual es el jugador mas joven en ganar el MVP de la temporada?")
                            time.sleep(0.5)
                            print()
                            print("[1] Kareem Abdul Jabbar")
                            print("[2] Lebron James")
                            print("[3] Derrick Rose")
                            print("[4] Magic Johnson")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 7:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Qué jugador es el que sale de perfil en el logotipo oficial de la NBA?.")
                            time.sleep(0.5)
                            print()
                            print("[1] Bob Cousy")
                            print("[2] Jerry West")
                            print("[3] Pete Maravich")
                            print("[4] Dave Bing")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 8:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Que jugador tiene mas MVP en la decada pasada?")
                            time.sleep(0.5)
                            print()
                            print("[1] Lebron James")
                            print("[2] Stephen Curry")
                            print("[3] Kevin Durant")
                            print("[4] James Harden")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 9:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Cual fue el ultimo equipo en ganar tres anillos consecutivos?.")
                            time.sleep(0.5)
                            print()
                            print("[1] Golden State Warriors")
                            print("[2] Chicago Bulls")
                            print("[3] Los Angeles Lakers")
                            print("[4] San Antonio Spurs")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                        elif x == 10:
                            print(f"Pregunta N°{x}:")
                            time.sleep(0.5)
                            print()
                            print("¿Cual de las siguientes leyendas de la NBA no gano un anillo?")
                            time.sleep(0.5)
                            print()
                            print("[1] Steve Nash")
                            print("[2] Allen Iverson")
                            print("[3] Karl Malone")
                            print("[4] Todas las anteriores")
                            time.sleep(0.5)
                            while True:
                                try:
                                    print()
                                    respuesta = int(input("Selecciona una respuesta: "))
                                    if respuesta == 4:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta Correcta :)")
                                        time.sleep(1)
                                        puntos = puntos + 1
                                        borrarPantalla()
                                        break
                                    elif respuesta == 1:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 3:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    elif respuesta == 2:
                                        time.sleep(1)
                                        print()
                                        print("Respuesta incorrecta :(")
                                        time.sleep(1)
                                        puntos = puntos
                                        borrarPantalla()
                                        break
                                    else:
                                        time.sleep(0.5)
                                        print()
                                        print("Valor mal ingresado.")
                                        continue
                                except:
                                    time.sleep(0.5)
                                    print()
                                    print("Valor mal ingresado.")
                                    continue
                    print()
                    print("Quiz Finalizado, gracias por responder.")
                    time.sleep(1)
                    print()
                    print("Cargando puntuacion ...")
                    time.sleep(1)
                    borrarPantalla()
                    print()
                    print(f"Has obtenido {puntos} puntos.")
                    print()
                    dicc_puntajes_facil[player] = puntos
                    guardar_diccionario2(dicc_puntajes_facil)
                    time.sleep(1)
                    print("Para volver al menu presione cualquier tecla.")
                    msvcrt.getch()
                    continue
                else:
                    print()
                    print("Valor mal ingresado, volviendo al menu de inicio.")
                    time.sleep(1)
                    continue
            except:
                print()
                print("Valor mal ingresado, volviendo al menu de inicio.")
                time.sleep(1)
                continue
        elif int(desicion) == 2:
            borrarPantalla()
            x = ordenar_valores(dicc_puntajes_dificil)
            y = ordenar_valores(dicc_puntajes_facil)
            print()
            print(chr(27)+"[4;37m"+"Puntuaciones:")
            print(chr(27)+"[0m")
            if len(dicc_puntajes_dificil) >= 1 or len(dicc_puntajes_facil) >= 1:
                print(chr(27)+"[4;37m"+"- Modo Dificil:")
                print(chr(27)+"[0m")
                if len(dicc_puntajes_dificil) >= 1:
                    for name in enumerate(x):
                        print(name[1], '=', x[name[1]], 'puntos.')
                else:
                    print("Sin Puntuaciones.")
                print()
                print(chr(27)+"[4;37m"+"- Modo Facil:")
                print(chr(27)+"[0m")
                if len(dicc_puntajes_facil) >= 1:
                    for name in enumerate(y):
                        print(name[1], '=', y[name[1]], 'puntos.')
                else:
                    print("Sin puntuaciones.")
                time.sleep(0.5)
                print()
                print("Para volver al menu presione cualquier tecla.")
                msvcrt.getch()
                continue
            elif len(dicc_puntajes_dificil) < 1 and len(dicc_puntajes_facil) < 1:
                print("Aun no hay puntuaciones.")
                time.sleep(0.5)
                print()
                print("Para volver al menu presione cualquier tecla.")
                msvcrt.getch()
                continue
        elif int(desicion) == 3:
            borrarPantalla()
            print()
            print("Saliendo...")
            time.sleep(1)
            break
        else:
            print()
            print("Valor mal ingresado, intentelo nuevamente.")
            time.sleep(1)
            continue
    except:
        print()
        print("Valor mal ingresado, intentelo nuevamente.")
        time.sleep(1)
        continue

exit()
msvcrt.getch() # Codigo para Abrir archivo desde la ventana de windows.