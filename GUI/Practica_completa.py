"""Desarrollo de una interfaz gráfica que conecte a una BBDD"""

#Importar la librería MySQL:
import pymysql

#Importación de las librerías Tkinter para la creación de la interfaz:
from tkinter import *
from tkinter import messagebox #Ventanas emergentes

#Creación de la raíz de la interfaz con Tkinter:
root = Tk()

#Asignación de título de la interfaz:
root.title("Registro BBDD")
miFrame = Frame (root)
miFrame.pack() 

#Crear la conexión con la BBDD SQL (usando el visor PHP my admin):
def get_connection():
    return pymysql.connect(host ="0.0.0.0", user="root", password="root", database="PROGRAMA1", cursorclass=pymysql.cursors.DictCursor)
    
#***************** Desarrollo de las funciones *********************

#Función para salir del programa:
def salir():
    respuesta = messagebox.askquestion("¿Desea salir del programa?")
    if respuesta == "yes":
        root.destroy()

#Función del submenu Licencia:
def licencia():
    messagebox.showinfo("Licencia", "Producto bajo licencia GNU")

#Función del submenu Acerca de...:
def infoAdicional():
    messagebox.showinfo("Programa de Northerose", "Conexión de interfaz a BBDD Versión 0.0.1")

#Función de los botones del CRUD:
def limpiar_campo():
    llave.set("")
    DNI.set("")
    nombre.set("")
    apellido.set("")
    contrasegna.set("")
    cuadroDireccion.delete("1.0", END)

def guardar_datos(sql, values):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(sql, values)
    connection.commit()
    connection.close()

def crear():
    respuesta = messagebox.askquestion("Aviso", "¿Deseas crear el resgistro?")
    if respuesta == "yes":
        dni = cuadroDNI.get()
        nombre = cuadroNombre.get()
        apellido = cuadroApellido.get()
        password = cuadroContrasegna.get()
        direccion = cuadroDireccion.get("1.0", "end-1c")

        sql = "INSERT INTO PERSONAS (DNI, NOMBRE, APELLIDO, PASSWORD, DIRECCION) VALUES (%s, %s, %s, %s, %s)"
        values = (dni, nombre, apellido, password, direccion)
        guardar_datos(sql, values)
        messagebox.showinfo("Aviso", "Registro creado Correctamente")
        limpiar_campo()

def actualizar():
    respuesta = messagebox.askquestion("Aviso", "¿Deseas actualizar el resgistro?")

    if respuesta == "yes":
        id_persona = llave.get()
        dni = cuadroDNI.get()
        nombre = cuadroNombre.get()
        apellido = cuadroApellido.get()
        password = cuadroContrasegna.get()
        direccion = cuadroDireccion.get("1.0", "end-1c")

        values = (dni, nombre, apellido, password, direccion, id_persona)
        sql ="UPDATE PERSONAS SET DNI=%s, NOMBRE=%s, APELLIDO=%s, PASSWORD=%s, DIRECCION=%s WHERE ID = %s"
        guardar_datos(sql, values) 
    
        messagebox.showinfo("Aviso", "Registro actualizado Correctamente")
        limpiar_campo()

def leer():
    persona_id = llave.get()
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM PERSONAS WHERE ID = %s"
    cursor.execute(sql, (persona_id))
    persona = cursor.fetchone()
    DNI.set(persona["DNI"])
    nombre.set(persona["NOMBRE"])
    apellido.set(persona["APELLIDO"])
    contrasegna.set(persona["PASSWORD"])
    cuadroDireccion.insert("1.0", persona["DIRECCION"])

def borrar():
    respuesta = messagebox.askquestion("Aviso", "¿Deseas eliminar el resgistro?")

    if respuesta == "yes":
        id_persona = llave.get()
        values = (id_persona)
        sql ="DELETE FROM PERSONAS WHERE ID = %s"
        guardar_datos(sql, values) 
        messagebox.showinfo("Aviso", "El registro ha sido borrado")
        limpiar_campo()


#Creación de la barra de menú:
barraMenu = Menu(root) #Ubicar las opciones de la barra de menú dentro de la raíz de la interfaz

#la variable menú contendrá la configuración de las opciones que se agregarán a la barra:
root.config(menu = barraMenu, width = 300, height = 300)

#Asignación del contenido(opciones) de la barra de menú:
menuBBDD = Menu(barraMenu, tearoff = 0)
menuBBDD.add_command(label = "Conectar", command = get_connection)
menuBBDD.add_separator() #Agregado de separador dentro del submenú
menuBBDD.add_command(label = "Salir", command = salir)

menuBorrar = Menu(barraMenu, tearoff = 0)
menuBorrar.add_command(label = "Borrar Campo", command = limpiar_campo)

menuCRUD = Menu(barraMenu, tearoff = 0)
menuCRUD.add_command(label = "Crear", command = crear)
menuCRUD.add_command(label = "Leer", command = leer)
menuCRUD.add_command(label = "Actualizar", command = actualizar)
menuCRUD.add_command(label = "Borar", command = borrar)

menuAyuda = Menu(barraMenu, tearoff = 0)
menuAyuda.add_command(label = "Licencia", command = licencia)
menuAyuda.add_command(label = "Acerca del Programa", command = infoAdicional)

#Orden de aparición en la barra de menú(agregado de etiqueta(titulo con su correspondiente configuración):
barraMenu.add_cascade(label = "BBDD", menu = menuBBDD) 
barraMenu.add_cascade(label = "Borrar", menu = menuBorrar)
barraMenu.add_cascade(label = "CRUD", menu = menuCRUD)
barraMenu.add_cascade(label = "Ayuda", menu = menuAyuda)

#Creación de los Entry (campos de texto):

#Declaración de variables y tipo de dato que almacenará:
llave = StringVar() 
DNI = StringVar()
nombre = StringVar()
apellido = StringVar()
contrasegna = StringVar()

#Configuración y posición de cada campo de texto:
cuadroID = Entry(miFrame, textvariable = llave)
cuadroID.grid(row = 0, column = 1, padx = 10, pady = 10)

cuadroDNI = Entry(miFrame, textvariable = DNI)
cuadroDNI.grid(row = 1, column = 1, padx = 10, pady = 10)

cuadroNombre = Entry(miFrame, textvariable = nombre)
cuadroNombre.grid(row = 2, column = 1, padx = 10, pady = 10)

cuadroApellido = Entry(miFrame, textvariable = apellido)
cuadroApellido.grid(row = 3, column = 1, padx = 10, pady = 10)

cuadroContrasegna = Entry(miFrame, textvariable = contrasegna)
cuadroContrasegna.grid(row = 4, column = 1, padx = 10, pady = 10)
cuadroContrasegna.config(show = "*")

#El campo dirección comprende un scrollbar:
cuadroDireccion = Text(miFrame, width = 20, height = 5)
cuadroDireccion.grid(row = 5, column = 1, padx = 10, pady = 10)
scrollvertical = Scrollbar(miFrame, command = cuadroDireccion.yview) #Creación del scrollbar
scrollvertical.grid(row = 5, column = 2, sticky = "nsew") #Ubicación y dimensiones("nsew") del scrollbar
cuadroDireccion.config(yscrollcommand = scrollvertical.set)#Posicionamiento del scrollbar según el texto

#Creación de labels que preceden el cuadro de texto:
llaveLabel = Label(miFrame, text = "ID: ")
llaveLabel.grid(row = 0, column = 0, sticky = E, padx = 10, pady = 10)

dniLabel = Label(miFrame, text = "DNI: ")
dniLabel.grid(row = 1, column = 0, sticky = E, padx = 10, pady = 10)

nombreLabel = Label(miFrame, text = "Nombre: ")
nombreLabel.grid(row = 2, column = 0, sticky = E, padx = 10, pady = 10)

apellidoLabel = Label(miFrame, text = "Apellido: ")
apellidoLabel.grid(row = 3, column = 0, sticky = E, padx = 10, pady = 10)

contrasegnaLabel = Label(miFrame, text = "Contraseña: ")
contrasegnaLabel.grid(row = 4, column = 0, sticky = E, padx = 10, pady = 10)

direccionLabel = Label(miFrame, text = "Dirección: ")
direccionLabel.grid(row = 5, column = 0, sticky = E, padx = 10, pady = 10)

#Creación de un frame para ubicar los botones de la parte inferior de la ventana:
framebotones = Frame(root)
framebotones.pack()

#Creación de los botones de acción de la parte inferior de la ventana:
botonCreate = Button(framebotones, text = "CREATE", command = crear)
botonCreate.grid(row = 1, column = 0, sticky = E, padx = 10, pady = 10) 

botonRead = Button(framebotones, text = "READ", command = leer)
botonRead.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

botonUpdate = Button(framebotones, text = "UPDATE", width = 5, command = actualizar)
botonUpdate.grid(row = 1, column = 2, sticky = E, padx = 10, pady = 10)

botonDelete = Button(framebotones, text = "DELETE", width = 5, command = borrar)
botonDelete.grid(row = 1, column = 3, sticky = E, padx = 10, pady = 10)

root.mainloop()