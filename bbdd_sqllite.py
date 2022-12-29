# VENTANA BÁSICA CON PYTHON
# TEXTO
# IMPORTAMOS MODULO

from tkinter import *
# Variables
ANCHO="550"
ALTO="540"
POSX="500"
POSY="150"

colorFondo="#007"
colorLetra="#FFF"
colorVentana="blue"

#ventana
ventana =Tk()
ventana.config(bg=colorVentana)
ventana.geometry(ANCHO+"x"+ALTO+"+"+POSX+"+"+POSY)
ventana.title("Ventana de Python")

#Variable Caja Texto
nombre=StringVar()
edad=IntVar()

#Etiquetas y Cajas
etiquetaNombre=Label(ventana, text="Nombre").place(x=50, y=50)
cajaNombre=Entry(ventana, textvariable=nombre).place(x=110, y=50)

etiquetaTexto=Label(ventana, text="Texto amplio", bg=colorFondo, fg=colorLetra).place (x=50, y=130)

etiquetaEdad=Label(ventana, text="Edad").place(x=50, y=90)
cajaEdad=Entry(ventana, textvariable=edad).place(x=110, y=90)

#Text
text=Text(ventana)
text.place(x=130, y=130, width=380)

ventana.mainloop()
