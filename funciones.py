# para los mensajes emergentes
from tkinter import *
from tkinter import messagebox

class Funciones():
    def __init__(self, ventana):
        self.ventana = ventana

    def salir(self):
        valor = messagebox.askquestion("Salir","Desea salir de la aplicacion?")

        if valor == "yes":
            self.ventana.destroy()
    
    def limpiarCampos(self, campo1, campo2, campo3, campo4, campo5, textoCom):
        campo1.set("")
        campo2.set("")
        campo3.set("")  
        campo4.set("")
        campo5.set("")
        textoCom.delete(1.0, END)
    
    # Funcion para que solo sean numeros
    def is_valid_char(self,char):
        return char in "0123456789"
