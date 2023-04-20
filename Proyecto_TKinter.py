# Se importa la biblioteca de tkinter
from tkinter import *

# Funciones del programa
def Cedula():
    try:
        global foto
        foto.destroy()
        foto = Label(v,image=icedula)
        foto.place(x=22,y=160)
    except NameError:
        foto = Label(v,image=iequis)
        foto.place(x=22,y=160)

def Vacuna():
    try:
        global foto
        foto.destroy()
        foto = Label(v,image=ivacuna)
        foto.place(x=22,y=160)
    except NameError:
        foto = Label(v,image=iequis)
        foto.place(x=22,y=160)

def Examen():
    try:
        global foto
        foto.destroy()
        foto = Label(v,image=iexamen)
        foto.place(x=22,y=160)
    except NameError:
        foto = Label(v,image=iequis)
        foto.place(x=22,y=160)

def EquisRoja():
    global foto
    foto.destroy()
    foto = Label(v,image=iequis)
    foto.place(x=22,y=160)

def Nombre():
    try:
        a = open("nom.txt","r")
        nombre = a.readline(80)
        if nombre == "":
            return("NO DEFINIDO")
        else:
            return(nombre)
    except FileNotFoundError:
        return("NO DEFINIDO")

def OpenCedula():
    a = open("cedula.txt","r")
    for u in a.readlines():
            return(u)

def OpenVacuna():
    a = open("vacuna.txt","r")
    for u in a.readlines():
            return(u)

def OpenExamen():
    a = open("examen.txt","r")
    for u in a.readlines():
            return(u)
        
def MoverVentana(event):
    v.geometry("+{0}+{1}".format(event.x_root, event.y_root))

def CambiarColor(event):
    global Cerrar
    Cerrar["bg"] = "red"

def VolverNormal(event):
   global Cerrar
   Cerrar["bg"] = "blue"

def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

# Programa
v = Tk()
# Titulo del programa e interfaz azul
v.overrideredirect(True)
v.geometry("400x500")
BarraT = Frame(v, bg="blue", relief='raised', bd=0,highlightthickness=1,highlightbackground="black")

# Boton de cerrar
Cerrar = Button(BarraT,text='x',command=v.destroy,bg="blue",padx=5,pady=2,activebackground="red",bd=0,font="bold",fg='white',activeforeground="white",highlightthickness=0)

Titulo = "TICO SEGURO COVID"
NombreT = Label(BarraT, text=Titulo, bg="blue", fg="white", font=("Arial",12))
Ventana = Canvas(v, bg="blue", highlightthickness=0)

# pack de todo lo agregado antes
BarraT.pack(expand=0, fill=X)
NombreT.pack(side=LEFT)
Cerrar.pack(side=RIGHT)
Ventana.pack(expand=1, fill=BOTH)
x_axis = None
y_axis = None

# Movimiento del cuadro creado
BarraT.bind("<B1-Motion>", MoverVentana)
Cerrar.bind("<Enter>", CambiarColor)
Cerrar.bind("<Leave>", VolverNormal)

# Cuadro blanco donde aparecen las fotos
miframe= Frame()
miframe.place(x=15,y=142)
miframe.config(bg="white")
miframe.config(width="370",height="350")

# nombre del paciente
nombre = Label(v,text=Nombre(),bd=5,bg="blue",fg="white",font=("Arial",12)).place(x=2,y=40)

# Imagenes para que se ejecuten las funciones
iblanca = PhotoImage(file="blanco.PNG")
try:
    icedula = PhotoImage(file=OpenCedula())
    icedula = resizeImage(icedula, 350, 300)
except (FileNotFoundError,TclError):
    iequis = PhotoImage(file="equis.PNG")

try:
    ivacuna = PhotoImage(file=OpenVacuna())
    ivacuna = resizeImage(ivacuna, 350, 300)
except (FileNotFoundError,TclError):
    iequis = PhotoImage(file="equis.PNG")

try:
    iexamen = PhotoImage(file=OpenExamen())
    iexamen = resizeImage(iexamen, 350, 300)
except (FileNotFoundError,TclError):
    iequis = PhotoImage(file="equis.PNG")

# Etiqueta para mostrar la iamgen blanca
foto = Label(v,image=iblanca)
foto.place(x=22,y=160)

# Botones

h = Canvas(v, width=122, height=60, bg="white") 
h.place(x=5, y=75)

bcedula = Button(v,text="CEDULA",fg="white",height=3,width=15,bg="blue",command=Cedula)
bcedula.place(x=10,y=80)

o = Canvas(v, width=122, height=60, bg="white") 
o.place(x=138, y=75)

bvacuna = Button(v,text="VACUNA",fg="white",height=3,width=15,bg="blue",command=Vacuna)
bvacuna.place(x=143,y=80)

p = Canvas(v, width=122, height=60, bg="white") 
p.place(x=270, y=75)

bexamen = Button(v,text="EXAMEN",fg="white",height=3,width=15,bg="blue",command=Examen)
bexamen.place(x=275,y=80)

v.mainloop()
