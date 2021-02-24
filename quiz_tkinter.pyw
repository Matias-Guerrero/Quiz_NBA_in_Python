from tkinter import *
import time
import msvcrt # Codigo para Abrir archivo desde la ventana de windows.
import pickle
import operator
from tkinter import messagebox as MessageBox


# Funcion para guardar diccionario en archivo .pickle
def guardar_diccionario(diccionario, file):
    archivo = open(file, 'wb')
    pickle.dump(diccionario, archivo)
    archivo.close()

# Funcion la cual ordena (de mayor a menor) un diccionario con respecto a sus valores (los cuales deben ser numeros).
def ordenar_valores(dicc):
    valores_ord = dict(sorted(dicc.items(), key=operator.itemgetter(1), reverse=True))
    return valores_ord

# Funcion la cual crea una nueva ventana mostrando las puntuaciones de otros jugadores.
def ventana_puntuaciones():
    flash_root= Tk()
    flash_root.title("Puntuaciones")
    flash_root.resizable(0,0)
    flash_root.config(bd=50)

    x = ordenar_valores(dicc_puntajes_dificil)
    y = ordenar_valores(dicc_puntajes_facil)

    Label(flash_root, text="Modo Dificil", font=("Verdana", 12)).pack()
    if len(dicc_puntajes_dificil) >= 1 or len(dicc_puntajes_facil) >= 1:
                if len(dicc_puntajes_dificil) >= 1:
                    for name in enumerate(x):
                        valores = '> ' + name[1] + ' = ' + str(x[name[1]]) + ' puntos.'
                        Label(flash_root, text=valores).pack(side="top", anchor="w")
                else:
                    Label(flash_root, text="Sin Puntuaciones.").pack()
    
    Label(flash_root, text="----------").pack()
    Label(flash_root, text="Modo Facil", font=("Verdana", 12)).pack()
    if len(dicc_puntajes_dificil) >= 1 or len(dicc_puntajes_facil) >= 1:
                if len(dicc_puntajes_dificil) >= 1:
                    for name in enumerate(x):
                        valores = '> ' + name[1] + ' = ' + str(x[name[1]]) + ' puntos.'
                        Label(flash_root, text=valores).pack(side="top", anchor="w")
                else:
                    Label(flash_root, text="Sin Puntuaciones.").pack()
    
    Label(flash_root, text="").pack()
    Button(flash_root, text="Volver al Menu Principal", command=flash_root.destroy).pack()

    flash_root.mainloop()

# Funcion la cual crea el menu principal.
def menu_principal():
    root.config(bd=0)

    # Titulo de Quiz
    l1 = Label(root, text="Bienvenidos al Quiz sobre la NBA.", font=("Verdana",20), fg="red")
    l1.grid(row=0, column=0)
    l2 = Label(root, text="")
    l2.grid(row=1,column=0)
    l3 = Label(root, text="¿Que deseas hacer?", font=("Verdana",12))
    l3.grid(row=2,column=0)
    l4 = Label(root, text="")
    l4.grid(row=3,column=0)

    # Botones Menu Principal
    Button(root, text="Comenzar Quiz.", height=4).grid(row=4, column=0, sticky=W+E+N+S)
    Button(root, text="Ver puntuaciones.", command=lambda: [clear(), mostrar_puntuaciones()], height=4).grid(row=5, column=0, sticky=W+E+N+S)
    Button(root, text="Salir.", command=root.destroy, height=4).grid(row=6, column=0, sticky=W+E+N+S)

# Funcion para ver las puntuaciones.
def mostrar_puntuaciones():
    root.config(bd=50)

    x = ordenar_valores(dicc_puntajes_dificil)
    y = ordenar_valores(dicc_puntajes_facil)

    Label(root, text="PUNTUACIONES:", font=("Verdana", 16)).grid(column=0)
    Label(root, text="Modo Dificil", font=("Verdana", 12)).grid(column=0)
    if len(dicc_puntajes_dificil) >= 1 or len(dicc_puntajes_facil) >= 1:
                if len(dicc_puntajes_dificil) >= 1:
                    for name in enumerate(x):
                        valores = '> ' + name[1] + ' = ' + str(x[name[1]]) + ' puntos.'
                        Label(root, text=valores).grid(column=0)
                else:
                    Label(root, text="Sin Puntuaciones.").grid(column=0)
    
    Label(root, text="----------").grid(column=0)
    Label(root, text="Modo Facil", font=("Verdana", 12)).grid(column=0)
    if len(dicc_puntajes_dificil) >= 1 or len(dicc_puntajes_facil) >= 1:
                if len(dicc_puntajes_dificil) >= 1:
                    for name in enumerate(x):
                        valores = '> ' + name[1] + ' = ' + str(x[name[1]]) + ' puntos.'
                        Label(root, text=valores).grid(column=0)
                else:
                    Label(root, text="Sin Puntuaciones.").grid(column=0)
    
    Label(root, text="").grid(column=0)
    Button(root, text="Volver al Menu Principal", command=lambda: [clear(), menu_principal()]).grid(column=0)

    root.mainloop()

# Funcion para ventana emergente "Acerca de"
def acerca_de():
    MessageBox.showinfo("Acerca de","Quiz creado por Matias Guerrero.")

def clear(): 
    list = root.grid_slaves() 
    for l in list: 
        l.destroy()


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

# Configuracion de la raiz
root = Tk()
root.title("Quiz NBA")
root.resizable(0,0)
root.iconbitmap("NBA.ico")

# Menu Superior
menubar = Menu(root)
root.config(menu=menubar)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Acerca de", command=acerca_de)

menubar.add_cascade(menu=helpmenu, label="Ayuda")

menu_principal()

# Finalmente bucle de la aplicacion
root.mainloop()