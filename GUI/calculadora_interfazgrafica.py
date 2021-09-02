
#*********************** App. Calculadora con Tkinter **************************
from tkinter import *

class Interfaz:
    def __init__(self, root, Frame):
        self.root = root
        self.root.title("Calculadora de Rose")
        #self.root.iconbitmap("calculadora.ico")
        self.miFrame = Frame(bg = "grey", cursor = "hand2")
        self.miFrame.pack()
        #Agregar Pantalla y sus características:
        self.num_pantalla = StringVar()
        self.pantalla = Entry(self.miFrame, textvariable = self.num_pantalla, background = "black", fg = "magenta", justify = "right")
        #Ubicar pantalla:
        self.pantalla.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 5)

        self.operacion = ""
        self.memoria = ""
        self.resultado = ""
        self.reset_pantalla = False
        self.num1 = 0
        self.contador_suma = 0
        self.contador_resta = 0
        self.contador_multi = 0
        self.contador_divi = 0
        self.contador_expo = 0
        self.contador_porcentaje = 0
        self.valor_porcentaje = 100
        
        boton7 = Button(self.miFrame, text = "7", width = 3, command = lambda: self.num_pulsado("7"))
        boton7.grid(row = 2, column = 1)
        boton8 = Button(self.miFrame, text = "8", width = 3, command = lambda: self.num_pulsado("8"))
        boton8.grid(row = 2, column = 2)
        boton9 = Button(self.miFrame, text = "9", width = 3, command = lambda: self.num_pulsado("9"))
        boton9.grid(row = 2, column = 3)
        botonB = Button(self.miFrame, text = "DEL", width = 3, fg = "magenta", command = lambda: self.borrar())
        botonB.grid(row = 2, column = 4)
        botonC = Button(self.miFrame, text = "C", width = 3, fg = "magenta",  command = lambda: self.cancelar())
        botonC.grid(row = 2, column = 5)

#------------- fila 3 - botones --------------------------------------------

        boton4 = Button(self.miFrame, text = "4", width = 3, command = lambda: self.num_pulsado("4"))
        boton4.grid(row = 3, column = 1)
        boton5 = Button(self.miFrame, text = "5", width = 3, command = lambda: self.num_pulsado("5"))
        boton5.grid(row = 3, column = 2)
        boton6 = Button(self.miFrame, text = "6", width = 3, command = lambda: self.num_pulsado("6"))
        boton6.grid(row = 3, column = 3)
        botonM = Button(self.miFrame, text = "x", width = 3, command = lambda: self.multiplicar(self.num_pantalla.get()))
        botonM.grid(row = 3, column = 4)
        botonD = Button(self.miFrame, text = "/", width = 3, command = lambda: self.dividir(self.num_pantalla.get()))
        botonD.grid(row = 3, column = 5)

#------------- fila 4 - botones --------------------------------------------

        boton1 = Button(self.miFrame, text = "1", width = 3, command = lambda: self.num_pulsado("1"))
        boton1.grid(row = 4, column = 1)
        boton2 = Button(self.miFrame, text = "2", width = 3, command = lambda: self.num_pulsado("2"))
        boton2.grid(row = 4, column = 2)
        boton3 = Button(self.miFrame, text = "3", width = 3, command = lambda: self.num_pulsado("3"))
        boton3.grid(row = 4, column = 3)
        botonS = Button(self.miFrame, text = "+", width = 3, command = lambda: self.sumar(self.num_pantalla.get()))
        botonS.grid(row = 4, column = 4)
        botonR = Button(self.miFrame, text = "-", width = 3, command = lambda: self.restar(self.num_pantalla.get()))
        botonR.grid(row = 4, column = 5)

#------------- fila 5 - botones --------------------------------------------

        boton0 = Button(self.miFrame, text = ".", width = 3, command = lambda: self.num_pulsado("."))
        boton0.grid(row = 5, column = 1)
        botonP = Button(self.miFrame, text = "0", width = 3, command = lambda: self.num_pulsado("0"))
        botonP.grid(row = 5, column = 2)
        botonE = Button(self.miFrame, text = "x²", width = 3, command = lambda: self.exponente(self.num_pantalla.get()))
        botonE.grid(row = 5, column = 3)
        botonPorcentaje = Button(self.miFrame, text = "%", width = 3, command = lambda: self.porcentaje(self.num_pantalla.get()))
        botonPorcentaje.grid(row = 5, column = 4)
        botonI = Button(self.miFrame, text = "=", width = 3, command = lambda: self.igual())
        botonI.grid(row = 5, column = 5)
        
    def num_pulsado(self, num):
        if self.reset_pantalla:
            self.num_pantalla.set(num)
            self.reset_pantalla = False
        else:
            valor = self.num_pantalla
            valor.set(str(valor.get()) + str(num))
    
    def borrar(self):
        valor = self.num_pantalla.get()
        valor = valor[:-1]
        self.num_pantalla.set(valor)
    
    def cancelar(self):
        self.num_pantalla.set("")

    def sumar(self, num):
        if self.contador_suma == 0:
            self.num1 = float(num)
            self.resultado = self.num1
        else:
            if self.contador_suma == 1:
                self.resultado = self.num1 + float(num)
            else:
                self.resultado = float(self.resultado) + float(num)	
                self.num_pantalla.set(self.resultado)
                self.resultado = self.num_pantalla.get()

        self.contador_resta = self.contador_suma + 1
        self.operacion = "suma"
        self.reset_pantalla = True

    def restar(self, num):
        if self.contador_resta == 0:
            self.num1 = float(num)
            self.resultado = self.num1
        else:
            if self.contador_resta == 1:
                self.resultado = self.num1 - float(num)
            else:
                self.resultado = float(self.resultado) - float(num)	
                self.num_pantalla.set(self.resultado)
                self.resultado = self.num_pantalla.get()

        self.contador_resta = self.contador_resta + 1
        self.operacion = "resta"
        self.reset_pantalla = True

    def multiplicar(self, num):
        if self.contador_multi == 0:
            self.num1 = float(num)
            self.resultado = self.num1
        else:
            if self.contador_multi == 1:
                self.resultado = self.num1 * float(num)
            else:
                self.resultado = float(self.resultado) * float(num)
            self.num_pantalla.set(self.resultado)
            self.resultado = self.num_pantalla.get()
        
        self.contador_multi = self.contador_multi + 1
        self.operacion = "multiplicacion"
        self.reset_pantalla = True

    def dividir(self, num):
        if self.contador_divi == 0:
            self.num1 = float(num)
            self.resultado = self.num1
        else:
            if self.contador_divi == 1:
                self.resultado = self.num1 / float(num)
            else:
                self.resultado = float(self.resultado) / float(num)
                self.num_pantalla.set(self.resultado)
                self.resultado = self.num_pantalla.get()
        
        self.contador_divi = self.contador_divi + 1
        self.operacion = "division"
        self.reset_pantalla = True

    def exponente(self, num):
        if self.contador_expo == 0:
            self.num1 = float(num)
            self.resultado = self.num1 * self.num1
        if self.contador_expo == 1:
            self.num_pantalla.set(float(self.resultado * self.resultado))
            self.resultado = self.num_pantalla.get()

        self.contador_expo = self.contador_expo + 1
        self.operacion = "exponente"
        self.reset_pantalla = True
    
    def porcentaje(self, num):
        if self.contador_porcentaje == 0:
            self.num1 = float(num)
            self.resultado = self.num1
        else:
            if self.contador_porcentaje == 1:
                self.resultado = self.num1 * float(num) / self.valor_porcentaje
            else:
                self.resultado = float(self.resultado) * float(num) / self.valor_porcentaje
                self.num_pantalla.set(self.resultado)
                self.resultado = self.num_pantalla.get()
        
        self.contador_porcentaje = self.contador_porcentaje + 1
        self.operacion = "porcentaje"
        self.reset_pantalla = True

    def igual(self):
        if self.operacion == "suma":
            self.num_pantalla.set(float(self.resultado + float(self.num_pantalla.get())))
            self.resultado = 0
            self.contador_suma = 0
        elif self.operacion == "resta":
            self.num_pantalla.set(float(self.resultado) - float(self.num_pantalla.get()))
            self.resultado = 0
            self.contador_resta = 0
        elif self.operacion == "multiplicacion":
            self.num_pantalla.set(float(self.resultado) * float(self.num_pantalla.get()))
            self.resultado = 0
            self.contador_multi = 0
        elif self.operacion == "division":
            self.num_pantalla.set(float(self.resultado) / float(self.num_pantalla.get()))
            self.resultado = 0
            self.contador_divi = 0
        elif self.operacion == "exponente":
            self.num_pantalla.set(float(self.resultado))
            self.resultado = 0
            self.contador_expo = 0
        elif self.operacion == "porcentaje":
            self.num_pantalla.set(float(self.resultado) * float(self.num_pantalla.get()) / self.valor_porcentaje)
            self.resultado = 0
            self.contador_porcentaje = 0

#------------ final -----------------------------------------------------------
ventana = Tk()
calculadora = Interfaz(ventana, Frame)
ventana.mainloop()