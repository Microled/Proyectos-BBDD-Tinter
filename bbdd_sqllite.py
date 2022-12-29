from tkinter import *
# Variables
ANCHO="550"
ALTO="400"
POSX="500"
POSY="150"

#ventana
ventana =Tk()
ventana.config(bg="red")
ventana.geometry(ANCHO+"x"+ALTO+"+"+POSX+"+"+POSY)
ventana.title("Ventana de Python")

#Variable Caja Texto
nombre=StringVar()
edad=IntVar()

#Etiquetas y Cajas
etiquetaNombre=Label(ventana, text="Nombre").place(x=50, y=50)
cajaNombre=Entry(ventana, textvariable=nombre).place(x=110, y=50)

etiquetaEdad=Label(ventana, text="Edad").place(x=50, y=90)
cajaEdad=Entry(ventana, textvariable=edad).place(x=110, y=90)

ventana.mainloop()
