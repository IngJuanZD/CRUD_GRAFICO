from tkinter import *
from tkinter import ttk, messagebox, filedialog
import tkinter as tk
import json
import os
from types import FrameType
from git import Repo
from os import close, remove
import shutil

from git.objects import commit

######Repara el uso inadecuado de varibles globales
#Error si no setiene el contenido de DCWA hay que bloquear repoL por que no funciona.
#Fallo cuando actualizo repocitorio
local_repo_directory = os.path.join(os.getcwd(), 'DCWA')
destination = 'master'
productos_dicc = {}

# Generar a "producto_dicc"
archivo = "./logo1.png"
imgNueva360 = any
imgNuevaPorta = any
btauxG = 0
btauxP = 0


def loadProductos():
    # abrir json solo lectura y guardar el contenido en db
    db = open("./DCWA/json/catalogo-dcw.json", "r")
    productos = db.read()  # leer json y pasarlo a productos
    # almacenar json en formato de diccionario para usar lo de python
    global productos_dicc
    productos_dicc = json.loads(productos)
    db.close()  # cerramos archivo

# Funcion que verifica si exixte o no el repocitorio y lo clona de ser necesario


def sincronizar():
    global local_repo_directory
    print("Dentro de Sincronizar")
    if os.path.exists(local_repo_directory):
        print("Directorio existente, bajando cambios desde la rama " + destination)        
        repoL = Repo(local_repo_directory)
        origin = repoL.remotes.origin
        origin.pull(destination)
    else:
        print("Directorio no existente, clonado repositorio ")
#REMPLAZAR DATOS        
        Repo.clone_from("https://github.com/IngJuanZD/DCWA.git",
                        local_repo_directory, branch=destination)
    print("Clonado listo")
    loadProductos()


def buscar():
    print("Dentro de Buscar")
    loadProductos()
    ID_b = int(txtid.get())
    global productos_dicc, updateimg_btn_360, updateimg_btn_portada
    ID_aux = len(productos_dicc) - 1
    print(len(productos_dicc))
    if ID_b <= ID_aux:
        limpiar()
        updateimg_btn_360.destroy()    
        updateimg_btn_portada.destroy()    
        print("Nombre: " + productos_dicc[ID_b]["nombre"])
        id_entry.insert(0, productos_dicc[ID_b]["id"])
        codigo_entry.insert(0, productos_dicc[ID_b]["codigo"])
        nombre_entry.insert(0, productos_dicc[ID_b]["nombre"])
        desc_entry.insert(0, productos_dicc[ID_b]["descripcion"])
        colores_entry.insert(0, productos_dicc[ID_b]["colores"])
        filtros_combobox.insert(0, productos_dicc[ID_b]["filtro"])
        foto360_entry.insert(0, productos_dicc[ID_b]["foto360"])
        fotoporta_entry.insert(0, productos_dicc[ID_b]["fotoportada"])
        manaul_combobox.insert(0, productos_dicc[ID_b]["manual"])
        manualUrl_entry.insert(0, productos_dicc[ID_b]["urlM"])
        materiales_entry.insert(0, productos_dicc[ID_b]["materiales"])
        medidas_entry.insert(0, productos_dicc[ID_b]["medidas"])
        peso_entry.insert(0, productos_dicc[ID_b]["peso"])
        nota_combobox.insert(0, productos_dicc[ID_b]["nota"])
        notatxt_entry.insert(0, productos_dicc[ID_b]["txtnota"])
        precio_entry.insert(0, productos_dicc[ID_b]["precio"])
        promo_combobox.insert(0, productos_dicc[ID_b]["promo"])
        precioPromo_entry.insert(0, productos_dicc[ID_b]["precioPromo"])
        urlComp_entry.insert(0, productos_dicc[ID_b]["urlComp"])
        # Foto 360
        global archivo
        global foto360_view
        archivo = "./DCWA/" + productos_dicc[ID_b]["foto360"]
        foto360_view = PhotoImage(file=archivo)
        foto360_view = foto360_view.zoom(1)
        foto360_view = foto360_view.subsample(3)
        foto360_lable_view = Label(vp, image=foto360_view)
        foto360_lable_view.grid(column=8, row=2, padx=5,
                                pady=(25, 5), rowspan=4)
        # Fotos
        archivo = "./DCWA/" + productos_dicc[ID_b]["fotoportada"]
        global fotoPorta_view
        fotoPorta_view = PhotoImage(file=archivo)
        fotoPorta_view = fotoPorta_view.subsample(5)
        fotoPorta_lable_view = Label(vp, image=fotoPorta_view)
        fotoPorta_lable_view.grid(column=8, row=6, padx=5, pady=5, rowspan=5)
        # Bloque escritura
        codigo_entry.config(state="readonly")
        nombre_entry.config(state="readonly")
        desc_entry.config(state="readonly")
        colores_entry.config(state="readonly")
        filtros_combobox.config(state="disabled")
        foto360_entry.config(state="readonly")
        fotoporta_entry.config(state="readonly")
        manaul_combobox.config(state="disabled")
        manualUrl_entry.config(state="readonly")
        materiales_entry.config(state="readonly")
        medidas_entry.config(state="readonly")
        peso_entry.config(state="readonly")
        nota_combobox.config(state="disabled")
        notatxt_entry.config(state="readonly")
        precio_entry.config(state="readonly")
        promo_combobox.config(state="disabled")
        precioPromo_entry.config(state="readonly")
        urlComp_entry.config(state="readonly")
    else:
        messagebox.showerror(
            message=f" ID: {txtid.get()}\n No encontrado!", title="No Encontrado")
        limpiar()


def nuevo():
    print("Dentro de Nuevo")
    loadProductos()
    global productos_dicc
    ID = len(productos_dicc)
    id_entry.insert(0, ID)
    codigo_entry.insert(0, f"DCW{ID+1}")
    datos = ["codigo", "colores", "descripcion", "filtro", "foto360", "fotoportada", "id", "manual", "materiales",
             "medidas", "nombre", "nota", "peso", "precio", "precioPromo", "promo", "txtnota", "urlComp", "urlM"]
    NuevoPro = dict.fromkeys(datos)  # Agregar los campos sin valor definido    
    id_entry.config(state="readonly")
    codigo_entry.config(state="readonly")
    # Funcion agregar nueva imagen
    # global imgNueva360
    # global imgNuevaPorta
    # global idNueva
    # idNueva = ID+1
    # imgNueva360 = filedialog.askopenfilename(filetypes=[("360", '.gif')])
    # imgNuevaPorta = filedialog.askopenfilename(filetypes=[("Portada", '.png')])
    productos_dicc.insert(ID, NuevoPro)  # Agregar el nuevo producto
    # Bloque id y codigo generados automaticos    
    # foto360_entry.insert(0, f"img/Productos/DCW{ID+2}.gif")
    # fotoporta_entry.insert(0, f"img/Productos/DCW{ID+2}.png")
    # foto360_entry.config(state="readonly")
    # fotoporta_entry.config(state="readonly")
    global updateimg_btn_portada
    global updateimg_btn_360
    updateimg_btn_360 = Button(vp, text="Cambiar Fotos 360", command=foto360_update)
    updateimg_btn_360.grid(column=2, row=5, pady=5, columnspan=2, sticky="ew")
    updateimg_btn_portada = Button(vp, text="Cambiar Fotos Portada", command=portada_update)
    updateimg_btn_portada.grid(column=5, row=5, pady=5, columnspan=2, sticky="ew")
    productos_dicc[ID][datos[0]] = txtcodigo.get()
    productos_dicc[ID][datos[6]] = f"{ID}"
    


def modificar():
    print("Dentro de Modificar")
    id_entry.config(state="readonly")
    codigo_entry.config(state="readonly")
    nombre_entry.config(state="normal")
    desc_entry.config(state="normal")
    colores_entry.config(state="normal")
    filtros_combobox.config(state="normal")
    foto360_entry.config(state="normal")
    fotoporta_entry.config(state="normal")
    manaul_combobox.config(state="normal")
    manualUrl_entry.config(state="normal")
    materiales_entry.config(state="normal")
    medidas_entry.config(state="normal")
    peso_entry.config(state="normal")
    nota_combobox.config(state="normal")
    notatxt_entry.config(state="normal")
    precio_entry.config(state="normal")
    promo_combobox.config(state="normal")
    precioPromo_entry.config(state="normal")
    urlComp_entry.config(state="normal")
    global updateimg_btn_portada
    global updateimg_btn_360
    updateimg_btn_360 = Button(vp, text="Cambiar Fotos 360", command=foto360_update)
    updateimg_btn_360.grid(column=2, row=5, pady=5, columnspan=2, sticky="ew")
    updateimg_btn_portada = Button(vp, text="Cambiar Fotos Portada", command=portada_update)
    updateimg_btn_portada.grid(column=5, row=5, pady=5, columnspan=2, sticky="ew")
    

def foto360_update():
    print("Boton update 360")
    global imgNueva360, foto360_entry, idNueva, btauxG
    idNueva = txtid.get()+1
    btauxG = 1
    imgNueva360 = filedialog.askopenfilename(filetypes=[("360", '.gif')])
    foto360_entry.insert(0, f"img/Productos/DCW{idNueva}.gif")    
    

def portada_update():
    print("Boton update Portada")
    global imgNuevaPorta , fotoporta_entry, idNueva, btauxP
    idNueva = txtid.get()+1
    btauxP = 1
    imgNuevaPorta = filedialog.askopenfilename(filetypes=[("Portada", '.png')])        
    fotoporta_entry.insert(0, f"img/Productos/DCW{idNueva}.png")

##################################

##################################
def tomardatos():
    print("Dentro de Guardar")    
    # Imagenes
    global imgNueva360, imgNuevaPorta, idNueva, btauxG, btauxP, local_repo_directory
    idNueva = txtid.get() + 1
    if btauxG == 1:
        dirimg360 = f"./DCWA/img/Productos/DCW{idNueva}.gif"
        imghtml360 = f"img/Productos/DCW{idNueva}.gif"
        shutil.copy(imgNueva360, dirimg360)
        productos_dicc[txtid.get()]["foto360"] = imghtml360
    else:
        productos_dicc[txtid.get()]["foto360"] = txtfoto360.get()
    if btauxP == 1:
        dirimgPorta = f"./DCWA/img/Productos/DCW{idNueva}.png"
        imghtmlPorta = f"img/Productos/DCW{idNueva}.png"
        shutil.copy(imgNuevaPorta, dirimgPorta)
        productos_dicc[txtid.get()]["fotoportada"] = imghtmlPorta
    else:
        productos_dicc[txtid.get()]["fotoportada"] = txtfotoporta.get()
    # Tomando todo los datos
    productos_dicc[txtid.get()]["nombre"] = txtnombre.get()
    productos_dicc[txtid.get()]["descripcion"] = txtdesc.get()
    productos_dicc[txtid.get()]["colores"] = txtcolores.get()
    productos_dicc[txtid.get()]["filtro"] = txtfiltros.get()    
    productos_dicc[txtid.get()]["manual"] = txtmanual.get()
    productos_dicc[txtid.get()]["urlM"] = txtmanualUrl.get()
    productos_dicc[txtid.get()]["materiales"] = txtmateriales.get()
    productos_dicc[txtid.get()]["medidas"] = txtmedidas.get()
    productos_dicc[txtid.get()]["peso"] = txtpeso.get()
    productos_dicc[txtid.get()]["nota"] = txtnota .get()
    productos_dicc[txtid.get()]["txtnota"] = txtnotatxt.get()
    productos_dicc[txtid.get()]["precio"] = txtprecio.get()
    productos_dicc[txtid.get()]["promo"] = txtpromo.get()
    productos_dicc[txtid.get()]["precioPromo"] = txtprecioPromo.get()
    productos_dicc[txtid.get()]["urlComp"] = txturlComp.get()
    print("Guardado datos en local.")
    ######
    repoL = Repo(local_repo_directory)
    # Abre y sobre escribe
    Archivo = "./DCWA/json/catalogo-dcw.json"
    with open(Archivo, 'w') as f:
        json.dump(productos_dicc, f, indent=2)
    ######
    buscar()


# Funcion que crea commit de manera local
Txt_entry = any
cambio = any
commint = any

#Esta funcion ayuda a comfirmar antes de guardartodo los datos y luego genreo un commint local 
#Re ordenar funciones relacionada a guardar 
def guardar():
    # Nueva ventana de confirmacion de guardado 
    app.withdraw()
    global commint
    commint=tk.Toplevel()    
    commint.config(background="#979DA6")    
    # VP -> ventana principal
    commintv = Frame (commint)
    commintv.grid(column=0, row=0, padx=(50, 50), pady=(20, 20))
    commintv.columnconfigure(0, weight=1)
    commintv.rowconfigure(0, weight=1)
    commintv.config(bg="#979DA6")
    global cambio, Txt_entry 
    cambio = Label(commintv, text="Que cambios se realisaron: :", bg="#979DA6")
    cambio.grid(column=1, row=2, padx=5, pady=(25, 5), sticky=E)
    Txt_entry = Entry(commintv, )
    Txt_entry.grid(column=2, row=2, padx=5, pady=(25, 5), columnspan= 3, sticky=E)
    conf_btn = Button(commintv, text="Confirmar", command=botonconfir)
    conf_btn.grid(column=6, row=2, padx=5, pady=(25, 5), sticky=E)    
    cancelar_btn = Button(commintv, text="Cancelar", command=botoncancelar)
    cancelar_btn.grid(column=7, row=2, padx=5, pady=(25, 5), sticky=E)    
    


def botonconfir():
    print("Commint confirmado....")
    tomardatos()
    global local_repo_directory
    repoL = Repo(local_repo_directory)
    repoL.git.add(update=True)    
    repoL.git.commit("-m", f"Actualizando: ID {txtid.get()}, {Txt_entry.get()}")        
    app.deiconify() 
    global commint
    commint.destroy()
    messagebox.showwarning(message="Datos Guardados", title="Estado del guardado")        

def botoncancelar():
    print("Commint cancelar....")
    limpiar()
    app.deiconify() 
    commint.destroy()
    messagebox.showwarning(message="Datos No Guardados", title="Estado del guardado")                 
        
        
    

# Funcion para el push a github
# def publicar():
#     # message forma de agregar concatenar el contenidod e variable
#     public = messagebox.askyesno(message=f" Deseas actualizar la página.", title="Actualización")
#     if public == True:        
#         guardar()
#         global repoL        
#         repoL.git.push("--set-upstream", 'origin', destination)                              
#         messagebox.showinfo(message="Datos actualizado en decorationcw.com.mx", title="Estado de actualización")        
#         limpiar()
#     else:
#         messagebox.showwarning(message="Actualizacíon cancelada", title="Estado de actualización")        
#         print("Actualización Cancelada")
#         limpiar()


    


def borrar():
    print("Dentro de Borrar")
    # message forma de agregar concatenar el contenidod e variable
    borrarP = messagebox.askyesno(
        message=f" Borrar id: {txtid.get()}\n Producto: {txtnombre.get()}", title="Eliminar Producto")
    if borrarP == True:
        print("Borrando....")
        remove(f"./DCWA/img/Productos/DCW{txtid.get()+1}.png")
        remove(f"./DCWA/img/Productos/DCW{txtid.get()+1}.gif")
        del productos_dicc[txtid.get()]
        Archivo = "./DCWA/json/catalogo-dcw.json"
        with open(Archivo, 'w') as f:
            json.dump(productos_dicc, f, indent=2)
        messagebox.showwarning(message="Datos Borrados", title="Borrar")        
        limpiar()
    else:
        print("No borro...")
        messagebox.showwarning(message="Datos No Borrados", title="Borrar")
        limpiar()


def limpiar():
    print("Dentro de limpiar")
    # desbloquea    
    id_entry.config(state="normal")
    codigo_entry.config(state="normal")
    nombre_entry.config(state="normal")
    desc_entry.config(state="normal")
    colores_entry.config(state="normal")
    filtros_combobox.config(state="normal")
    foto360_entry.config(state="normal")
    fotoporta_entry.config(state="normal")
    manaul_combobox.config(state="normal")
    manualUrl_entry.config(state="normal")
    materiales_entry.config(state="normal")
    medidas_entry.config(state="normal")
    peso_entry.config(state="normal")
    nota_combobox.config(state="normal")
    notatxt_entry.config(state="normal")
    precio_entry.config(state="normal")
    promo_combobox.config(state="normal")
    precioPromo_entry.config(state="normal")
    urlComp_entry.config(state="normal")
    # limpiar    
    global updateimg_btn_360, updateimg_btn_portada
    updateimg_btn_360.destroy()    
    updateimg_btn_portada.destroy()    
    id_entry.delete(0, END)
    codigo_entry.delete(0, END)
    nombre_entry.delete(0, END)
    desc_entry.delete(0, END)
    colores_entry.delete(0, END)
    filtros_combobox.delete(0, END)
    foto360_entry.delete(0, END)
    fotoporta_entry.delete(0, END)
    manaul_combobox.delete(0, END)
    manualUrl_entry.delete(0, END)
    materiales_entry.delete(0, END)
    medidas_entry.delete(0, END)
    peso_entry.delete(0, END)
    nota_combobox.delete(0, END)
    notatxt_entry.delete(0, END)
    precio_entry.delete(0, END)
    promo_combobox.delete(0, END)
    precioPromo_entry.delete(0, END)
    urlComp_entry.delete(0, END)
    # Foto 360
    global foto360_view
    foto360_view = PhotoImage(file="./360.png")
    foto360_view = foto360_view.zoom(1)
    foto360_view = foto360_view.subsample(3)
    foto360_lable_view = Label(vp, image=foto360_view)
    foto360_lable_view.grid(column=8, row=2, padx=5, pady=(25, 5), rowspan=4)
    # Fotos
    global fotoPorta_view
    fotoPorta_view = PhotoImage(file="./logo1.png")
    fotoPorta_view = fotoPorta_view.subsample(5)
    fotoPorta_lable_view = Label(vp, image=fotoPorta_view)
    fotoPorta_lable_view.grid(column=8, row=6, padx=5, pady=5, rowspan=5)
    id_entry.icursor(0)
    id_entry.focus()


#app ()
app = Tk()
# app.geometry("1080x680")
app.title("CRUD | DECORATIONCW")
app.config(background="#979DA6")
# VP -> ventana principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(20, 20))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)
vp.config(bg="#979DA6")

# Foto 360
foto360_view = PhotoImage(file="./360.png")
foto360_view = foto360_view.zoom(1)
foto360_view = foto360_view.subsample(3)
foto360_lable_view = Label(vp, image=foto360_view)
foto360_lable_view.grid(column=8, row=2, padx=5, pady=(25, 5), rowspan=4)

# Fotos
fotoPorta_view = PhotoImage(file=archivo)
fotoPorta_view = fotoPorta_view.subsample(5)
fotoPorta_lable_view = Label(vp, image=fotoPorta_view)
fotoPorta_lable_view.grid(column=8, row=6, padx=5, pady=5, rowspan=5)


# ETIQUETAS DE CADA DATO
id_lable = Label(vp, text="ID:", bg="#979DA6")
codigo_lable = Label(vp, text="Codigo:", bg="#979DA6")
nombre_lable = Label(vp, text="Nombre:", bg="#979DA6")
desc_lable = Label(vp, text="Descripción:", bg="#979DA6")
colores_lable = Label(vp, text="Colores:", bg="#979DA6")
filtros_lable = Label(vp, text="Filtros:", bg="#979DA6")
foto360_lable = Label(vp, text="Foto 360º :", bg="#979DA6")

fotoporta_lable = Label(vp, text="Foto de portada :", bg="#979DA6")

manual_lable = Label(vp, text="Manual:", bg="#979DA6")
manualUrl_lable = Label(vp, text="Url:", bg="#979DA6")
materiales_lable = Label(vp, text="Materiales:", bg="#979DA6")
medidas_lable = Label(vp, text="Medidas:", bg="#979DA6")
peso_lable = Label(vp, text="Peso:", bg="#979DA6")
nota_lable = Label(vp, text="Lleva Notas:", bg="#979DA6")
notatxt_lable = Label(vp, text="Nota:", bg="#979DA6")
precio_lable = Label(vp, text="Presio ($0.0):", bg="#979DA6")
promo_lable = Label(vp, text="Promo:", bg="#979DA6")
precioPromo_lable = Label(vp, text="Presio ($0.0):", bg="#979DA6")
urlComp_lable = Label(vp, text="Url MercadoLibre:", bg="#979DA6")
# POSICIONANDO LABLES
id_lable.grid(column=1, row=2, padx=5, pady=(25, 5), sticky=E)
codigo_lable.grid(column=3, row=2, padx=5, pady=(25, 5), sticky=E)
nombre_lable.grid(column=5, row=2, padx=5, pady=(25, 5), sticky=E)
desc_lable.grid(column=1, row=3, padx=5, pady=5, sticky=E)
colores_lable.grid(column=1, row=4, padx=5, pady=5, sticky=E)
filtros_lable.grid(column=3, row=4, padx=5, pady=5, sticky=E)
foto360_lable.grid(column=1, row=5, padx=5, pady=5, sticky=E)


fotoporta_lable.grid(column=4, row=5, padx=5, pady=5, sticky=E)
manual_lable.grid(column=1, row=6, padx=5, pady=5, sticky=E)
manualUrl_lable.grid(column=3, row=6, padx=5, pady=5, sticky=E)
materiales_lable.grid(column=1, row=7, padx=5, pady=5, sticky=E)
medidas_lable.grid(column=3, row=7, padx=5, pady=5, sticky=E)
peso_lable.grid(column=5, row=7, padx=5, pady=5, sticky=E)
nota_lable.grid(column=1, row=8, padx=5, pady=5, sticky=E)
notatxt_lable.grid(column=3, row=8, padx=5, pady=5, sticky=E)
precio_lable.grid(column=1, row=9, padx=5, pady=5, sticky=E)
promo_lable.grid(column=3, row=9, padx=5, pady=5, sticky=E)
precioPromo_lable.grid(column=5, row=9, padx=5, pady=5, sticky=E)
urlComp_lable.grid(column=1, row=10, padx=5, pady=5, sticky=E)

# DATOS DE VARIABLES TEMPORALES
txtid = IntVar()
txtcodigo = StringVar()
txtnombre = StringVar()
txtdesc = StringVar()
txtcolores = StringVar()
txtfiltros = StringVar()
txtfoto360 = StringVar()
txtfotoporta = StringVar()
txtmanual = StringVar()
txtmanualUrl = StringVar()
txtmateriales = StringVar()
txtmedidas = StringVar()
txtpeso = StringVar()
txtnota = StringVar()
txtnotatxt = StringVar()
txtprecio = StringVar()
txtpromo = StringVar()
txtprecioPromo = StringVar()
txturlComp = StringVar()

# DATOS I/O
id_entry = Entry(vp, textvariable=txtid)
id_entry.bind("<Key-Return>", lambda _: buscar())
id_entry.bind("<Return>", lambda _: buscar())
codigo_entry = Entry(vp, textvariable=txtcodigo)
nombre_entry = Entry(vp, textvariable=txtnombre)
desc_entry = Entry(vp, textvariable=txtdesc)
colores_entry = Entry(vp, textvariable=txtcolores)
filtros_combobox = ttk.Combobox(vp, textvariable=txtfiltros, values=[
                                "H_", "O_", "I_", "M_", "B_", "K_"])
foto360_entry = Entry(vp, textvariable=txtfoto360)
fotoporta_entry = Entry(vp, textvariable=txtfotoporta)
manaul_combobox = ttk.Combobox(vp, textvariable=txtmanual, values=["Si", "No"])
manualUrl_entry = Entry(vp, textvariable=txtmanualUrl)
materiales_entry = Entry(vp, textvariable=txtmateriales)
medidas_entry = Entry(vp, textvariable=txtmedidas)
peso_entry = Entry(vp, textvariable=txtpeso)
nota_combobox = ttk.Combobox(vp, textvariable=txtnota, values=["Si", "No"])
notatxt_entry = Entry(vp, textvariable=txtnotatxt)
precio_entry = Entry(vp, textvariable=txtprecio)
promo_combobox = ttk.Combobox(vp, textvariable=txtpromo, values=["Si", "No"])
precioPromo_entry = Entry(vp, textvariable=txtprecioPromo)
urlComp_entry = Entry(vp, textvariable=txturlComp)
# POSICIONANDO ENTRY
id_entry.grid(column=2, row=2, pady=(25, 5), sticky="ew")
codigo_entry.grid(column=4, row=2, pady=(25, 5), sticky="ew")
nombre_entry.grid(column=6, row=2, pady=(25, 5), sticky="ew")
desc_entry.grid(column=2, row=3, pady=5, columnspan=5, sticky="ew")
colores_entry.grid(column=2, row=4, pady=5, sticky="ew")
filtros_combobox.grid(column=4, row=4, pady=5, sticky="ew")
foto360_entry.grid(column=2, row=5, pady=5, columnspan=2, sticky="ew")
fotoporta_entry.grid(column=5, row=5, pady=5, columnspan=2, sticky="ew")
manaul_combobox.grid(column=2, row=6, pady=5, sticky="ew")
manualUrl_entry.grid(column=4, row=6, pady=5, columnspan=2, sticky="ew")
materiales_entry.grid(column=2, row=7, pady=5, sticky="ew")
medidas_entry.grid(column=4, row=7, pady=5, sticky="ew")
peso_entry.grid(column=6, row=7, pady=5, sticky="ew")
nota_combobox.grid(column=2, row=8, pady=5, sticky="ew")
notatxt_entry.grid(column=4, row=8, pady=5, sticky="ew")
precio_entry.grid(column=2, row=9, pady=5, sticky="ew")
promo_combobox.grid(column=4, row=9, pady=5, sticky="ew")
precioPromo_entry.grid(column=6, row=9, pady=5, sticky="ew")
urlComp_entry.grid(column=2, row=10, pady=5, columnspan=5, sticky="ew")

# BOTONES
sic_btn = Button(vp, text="Descarga", command=sincronizar, bg="#3EB595")
sic_btn.grid(column=1, row=1,)
buscar_btn = Button(vp, text="Buscar", command=buscar, bg="#F2C53D")
buscar_btn.grid(column=2, row=1)
nuevo_btn = Button(vp, text="Nuevo", command=nuevo, bg="#6593A6")
nuevo_btn.grid(column=3, row=1)
modificar_btn = Button(vp, text="Modificar", command=modificar, bg="#F29F05")
modificar_btn.grid(column=4, row=1)
guardar_btn = Button(vp, text="Guardar", command=guardar, bg="#A6BF4B")
guardar_btn.grid(column=5, row=1)
#publicar_btn = Button(vp, text="Publicar", command=publicar, bg="#668C4A")
#publicar_btn.grid(column=6, row=1)
borrar_btn = Button(vp, text="Borrar", command=borrar, bg="#812F33")
borrar_btn.grid(column=6, row=1)
limpiar_btn = Button(vp, text="Limpiar", command=limpiar, bg="#8C0082")
limpiar_btn.grid(column=7, row=1)
updateimg_btn_360 = Button(vp, text="Cambiar Fotos 360", command=foto360_update)    
updateimg_btn_360.grid(column=2, row=11)
updateimg_btn_portada = Button(vp, text="Cambiar Fotos Portada", command=portada_update)    
updateimg_btn_portada.grid(column=3, row=11)
limpiar()

app.mainloop()
