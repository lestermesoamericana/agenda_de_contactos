from tkinter import *
from Base_de_Datos import *
from funciones import *

class Interfaz():

    def __init__(self, raiz):
        # -------------------------------- Frame Raiz
        objetoFun = Funciones(raiz)
        objetoBD = Conexion()
        self.raiz = raiz
        self.raiz.title("Registro de Contactos")
        self.raiz.iconbitmap("bootloader_users_person_people_6080.ico")
        self.raiz.config(width = 300, height = 350)

        # --------------------------------- Entrys
        # esto es solo para los entrys y el cuadro de texto
        self.miID = StringVar()
        self.miNombre = StringVar()
        self.miApellido = StringVar()
        self.miPass = StringVar()
        self.miDireccion = StringVar()
        self.TextoComentario = Text(self.raiz)

        # -------------------------------- Barra de Menu
        # Creacion de la barra
        self.barraMenu = Menu(self.raiz)
        self.raiz.config(menu = self.barraMenu, width = 300, height = 350)
        
        # conectar la base de datos y salir
        self.bbddMenu = Menu(self.barraMenu, tearoff = 0)
        self.bbddMenu.add_command(label = "Conectar", command = objetoBD.crearConexion)
        self.bbddMenu.add_command(label = "Salir", command = objetoFun.salir)

        # borrar
        self.borrarMenu = Menu(self.barraMenu, tearoff = 0)
        self.borrarMenu.add_command(label = "Borrar Campos", command = lambda:objetoFun.limpiarCampos(self.miID, self.miNombre, self.miApellido, self.miPass, self.miDireccion, self.TextoComentario))

        # crud
        self.crudMenu = Menu(self.barraMenu, tearoff = 0)
        self.crudMenu.add_command(label = "Crear", command = lambda:objetoBD.crear(self.miNombre, self.miApellido, self.miPass, self.miDireccion, self.TextoComentario))
        self.crudMenu.add_command(label = "Leer", command = lambda:objetoBD.leer(self.miID, self.miNombre, self.miApellido, self.miPass, self.miDireccion, self.TextoComentario))
        self.crudMenu.add_command(label = "Actualizar", command = lambda:objetoBD.actualizar(self.miID, self.miNombre, self.miApellido, self.miPass, self.miDireccion, self.TextoComentario))
        self.crudMenu.add_command(label = "Borrar", command = lambda : objetoBD.borrar(self.miID))

        # ayuda
        self.ayudaMenu = Menu(self.barraMenu, tearoff = 0)
        self.ayudaMenu.add_command(label = "Licencia")
        self.ayudaMenu.add_command(label = "Acerca de...") 

        # Titulos de los menu
        self.barraMenu.add_cascade(label = "BBDD", menu = self.bbddMenu)
        self.barraMenu.add_cascade(label = "Borrar", menu = self.borrarMenu)
        self.barraMenu.add_cascade(label = "CRUD", menu = self.crudMenu)
        self.barraMenu.add_cascade(label = "Ayuda", menu = self.ayudaMenu)

        # -------------------------------------------- Campos y Labels
        # creamos los frame (Si deseas hacerlo por frames utiliza esta linea,
        # ya que se utiliza mas cuando estas con "grid". En mi caso yo utilice
        # el metodo "place" y por ello no utilice un segundo frame)
        #self.miFrame = Frame(self.raiz)
        #self.miFrame.pack()

        # creamos los entrys

        # Cuadro ID
        self.__validatecommand = self.raiz.register(objetoFun.is_valid_char)
        self.idLabel = Label(self.raiz, text = "id:")
        self.idLabel.place(x=-10, y=10, height=20, width=180)
        self.cuadroID = Entry(self.raiz, textvariable = self.miID, validate="key", validatecommand=(self.__validatecommand, "%S"))
        self.cuadroID.config(fg = "red", justify = "right")
        self.cuadroID.place(x=100, y=10, height=20, width=180)

        # Cuadro Nombre
        self.nombreLabel = Label(self.raiz, text = "Nombre:")
        self.nombreLabel.place(x=-26, y=40, height=20, width=180)
        self.cuadroNombre = Entry(self.raiz, textvariable = self.miNombre)
        self.cuadroNombre.config(fg = "blue", justify = "left")
        self.cuadroNombre.place(x=100, y = 40, height=20, width=180)

        # Cuadro Apellido
        self.apellidoLabel = Label(self.raiz, text = "Apellido:")
        self.apellidoLabel.place(x=-26, y=70, height=20, width=180)
        self.cuadroApellido = Entry(self.raiz, textvariable = self.miApellido)
        self.cuadroApellido.config(fg = "blue", justify = "left")
        self.cuadroApellido.place(x=100, y = 70, height=20, width=180)

        # Cuadro Contrasenya
        self.passLabel = Label(self.raiz, text = "Contraseña:")
        self.passLabel.place(x=-34, y=100, height=20, width=180)
        self.cuadroPassword = Entry(self.raiz, textvariable = self.miPass)
        self.cuadroPassword.config(show = "*", justify = "left")
        self.cuadroPassword.place(x=100, y = 100, height=20, width=180)

        # Cuadro Direccion
        self.passLabel = Label(self.raiz, text = "Direccion:")
        self.passLabel.place(x=-28, y=130, height=20, width=180)
        self.cuadroDireccion = Entry(self.raiz, textvariable = self.miDireccion)
        self.cuadroDireccion.config(fg = "blue", justify = "left")
        self.cuadroDireccion.place(x=100, y = 130, height=20, width=180)

        # Cuadro de Texto (Comentario)
        self.cuadroLabel = Label(self.raiz, text = "Observaciones:")
        self.cuadroLabel.place(x=-0, y=200, height=20, width=100)
        # Posicion del cuadro de texto
        self.TextoComentario.place(x=100, y = 160, height=100, width=180)
        self.scrollVert = Scrollbar(self.raiz, command = self.TextoComentario.yview)
        self.scrollVert.place(x=265, y = 160, height=100)
        self.TextoComentario.config(yscrollcommand = self.scrollVert.set)

        # -------------------------------------------- Botones inferiores
        # boton crear
        self.botonCrear = Button(self.raiz, text = "Crear", command = lambda:objetoBD.crear(self.miNombre, self.miApellido, self.miPass, self.miDireccion, self.TextoComentario))
        self.botonCrear.place(x=20, y = 280, height=30, width=60)

        # boton leer
        self.botonLeer = Button(self.raiz, text = "Leer", command = lambda:objetoBD.leer(self.miID, self.miNombre, self.miApellido, self.miPass, self.miDireccion, self.TextoComentario))
        self.botonLeer.place(x=90, y = 280, height=30, width=60)

        # boton leer
        self.botonModificar = Button(self.raiz, text = "Modificar", command = lambda:objetoBD.actualizar(self.miID, self.miNombre, self.miApellido, self.miPass, self.miDireccion, self.TextoComentario))
        self.botonModificar.place(x=160, y = 280, height=30, width=60)

        # boton leer
        self.botonEliminar = Button(self.raiz, text = "Eliminar", command = lambda : objetoBD.borrar(self.miID))
        self.botonEliminar.place(x=230, y = 280, height=30, width=60)


