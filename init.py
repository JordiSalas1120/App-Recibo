import datetime
from tkinter import *
from tkinter import filedialog, messagebox
Nro_registro = 0
precios_pecheras = [60,30,20]
precios_jaquimas = [300,150,100]
precios_monturas = [2500,2100,1500]

operador = ''#donde se alamacenan los digitos de calculadora registrados
#con global podemos utilizar la variable dentro una funcion
def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)
def obtener_resultado():
    global operador 
    resultado = str(eval(operador))#con eval evaluara si es operacion y la hara sin importar que sea un string
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ''
def revisar_checkbuton():
    x=0
    for c in cuadros_monturas: 
        if variables_monturas[x].get() == 1:#revisamos si el che esta activado en las variables que creamos al crear el check
            cuadros_monturas[x].config(state=NORMAL)
            if cuadros_monturas[x].get() == '0':
                cuadros_monturas[x].delete(0,END)
            cuadros_monturas[x].focus()#colocar elcursos en ese elemento seleccionado
        else:
            cuadros_monturas[x].config(state=DISABLED)
            texto_monturas[x].set('0')
        x += 1
    x=0
    for c in cuadros_jaquimas: 
        if variables_jaquimas[x].get() == 1:#revisamos si el che esta activado en las variables que creamos al crear el check
            cuadros_jaquimas[x].config(state=NORMAL)
            if cuadros_jaquimas[x].get() == '0':
                cuadros_jaquimas[x].delete(0,END)
            cuadros_jaquimas[x].focus()#colocar elcursos en ese elemento seleccionado
        else:
            cuadros_jaquimas[x].config(state=DISABLED)
            texto_jaquimas[x].set('0')
        x += 1
    x=0
    for c in cuadros_pecheras: 
        if variables_pecheras[x].get() == 1:#revisamos si el che esta activado en las variables que creamos al crear el check
            cuadros_pecheras[x].config(state=NORMAL)
            if cuadros_pecheras[x].get() == '0':
                cuadros_pecheras[x].delete(0,END)
            cuadros_pecheras[x].focus()#colocar elcursos en ese elemento seleccionado
        else:
            cuadros_pecheras[x].config(state=DISABLED)
            texto_pecheras[x].set('0')
        x += 1

def total():
    total_pecheras = 0
    p=0
    for cant in texto_pecheras:
        total_pecheras = total_pecheras + (float(cant.get())* precios_pecheras[p])
        p+=1

    j=0
    total_jaquimas =0
    for cant in texto_jaquimas:
        total_jaquimas = total_jaquimas + (float(cant.get())* precios_jaquimas[j])
        j+=1

    m=0
    total_monturas = 0
    for cant in texto_monturas:
        total_monturas = total_monturas + (float(cant.get())* precios_monturas[m])
        m+=1
    total = total_monturas+total_jaquimas+total_pecheras
    var_costo_pechera.set(f'${round(total_pecheras,2)}')
    var_costo_jaquima.set(f'${round(total_jaquimas,2)}')
    var_costo_montura.set(f'${round(total_monturas,2)}')
    var_total.set(f'${round(total,2)}')
#funcion para rear el recibo
def recibo():
    global Nro_registro
    
    texto_recibo.delete(1.0,END)
    numero_recibo = f'Nro Recibo: {Nro_registro}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{numero_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*'*66+'\n')
    texto_recibo.insert(END, f'Product.\t\tCant \tCosto \tCosto Items\n')
    texto_recibo.insert(END, f'-'*77+'\n')

    x=0
    for pechera in texto_pecheras:
        if pechera.get() != '0':
            texto_recibo.insert(END, f'{lista_pecheras[x]}\t\t{pechera.get()}\t {precios_pecheras[x]}\t{int(pechera.get()) * precios_pecheras[x]}\n')
        x+=1 

    x=0
    for jaquima in texto_jaquimas:
        if jaquima.get() != '0':
            texto_recibo.insert(END, f'{lista_jaquimas[x]}\t\t{jaquima.get()}\t {precios_jaquimas[x]}\t{int(jaquima.get()) * precios_jaquimas[x]}\n')
        x+=1    

    x=0
    for montura in texto_monturas:
        if montura.get() != '0':
            texto_recibo.insert(END, f'{lista_monturas[x]}\t\t{montura.get()}\t {precios_monturas[x]}\t{int(montura.get()) * precios_monturas[x]}\n')
        x+=1  
    texto_recibo.insert(END, f'-'*77+'\n')
    texto_recibo.insert(END,f'\n')
    texto_recibo.insert(END, f'Total:\t\t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*'*66+'\n')
    Nro_registro+=1

def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Recibo Guardado')
#iniciar tkinder
aplicacion  = Tk()



#tamanho de la ventana
aplicacion.geometry('1300x700+20+0')

#evitar maximizar
aplicacion.resizable(0,0)

#titulo de la ventana
aplicacion.title('Back Horse-Sistema de Facturacion')

#color de fondo de la ventana
aplicacion.config(bg='gray61')

#panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)#le decimos donde colocarlo

etiqueta_titulo = Label(panel_superior, text='SISTEMA DE FACTURACION', fg='gray2',
                        font=('Dosis',58), bg='gray61', width=23)

etiqueta_titulo.grid(row=0, column=0)


#panel izquierdo
panel_izquierdo = Frame(aplicacion,bd=1,relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel_costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='gray64', padx=225)
panel_costos.pack(side=BOTTOM)

#panel pechera
panel_pecheras = LabelFrame(panel_izquierdo, text='Pechera', font=('Dosis', 19, 'bold' ), bd=1, relief=FLAT, fg='gray64')
panel_pecheras.pack(side=LEFT)


#panel jaquimas
panel_jaquimas = LabelFrame(panel_izquierdo, text='Jaquima', font=('Dosis', 19, 'bold' ), bd=1, relief=FLAT, fg='gray64')
panel_jaquimas.pack(side=LEFT)

#panel monturas
panel_monturas = LabelFrame(panel_izquierdo, text='Montura', font=('Dosis', 19, 'bold' ), bd=1, relief=FLAT, fg='gray64')
panel_monturas.pack(side=LEFT)


panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

panel_calculadora=Frame(panel_derecha, bd=1,relief=FLAT, bg='gray64')
panel_calculadora.pack()

panel_recibo=Frame(panel_derecha, bd=1,relief=FLAT, bg='gray64')
panel_recibo.pack()

panel_botones=Frame(panel_derecha, bd=1,relief=FLAT, bg='gray64')
panel_botones.pack()


#Lista de productos
lista_pecheras=['pechera G', 'Pechera M', 'Pechera P']
lista_jaquimas=['Jaquima G', 'Jaquima M', 'Jaquima P']
lista_monturas=['Montura de Primera', 'Montura de Estandar', 'Montura Economica']


#generar items pecheras
variables_pecheras = []
cuadros_pecheras=[]
texto_pecheras=[]
cont = 0
for pechera in lista_pecheras:
    #crear checkbuttom
    variables_pecheras.append('')
    variables_pecheras[cont] = IntVar()#la convertimos en entero con funcion de tkinter
    pechera = Checkbutton(panel_pecheras, 
        text=pechera.title(), 
        font=('Dosis', 19,'bold'), 
        onvalue=1, 
        offvalue=0,
        variable=variables_pecheras[cont],command=revisar_checkbuton)
    pechera.grid(row=cont, column=0, sticky=W)#se le puso el sticky W para que se justifique a la izquierda


    #crear cuadros de entrada
    cuadros_pecheras.append('')#solo para crearla
    texto_pecheras.append('')
    texto_pecheras[cont] = StringVar()
    texto_pecheras[cont].set('0')
    cuadros_pecheras[cont] = Entry(panel_pecheras,
                                   font=('Dosis', 16, 'bold'),
                                   bd=1,
                                   width=5,
                                   state=DISABLED,
                                   textvariable=texto_pecheras[cont])
    cuadros_pecheras[cont].grid(row=cont, column=1)#le colocamosel recuadro en cada checkbox

    cont += 1



#generar items jaquimas
variables_jaquimas = []
cuadros_jaquimas=[]
texto_jaquimas=[]
cont = 0
for jaquima in lista_jaquimas:
    variables_jaquimas.append('')
    variables_jaquimas[cont] = IntVar()#la convertimos en entero con funcion de tkinter
    jaquima = Checkbutton(panel_jaquimas, text=jaquima.title(), font=('Dosis', 19,'bold'), onvalue=1, offvalue=0,variable=variables_jaquimas[cont],command=revisar_checkbuton)
    jaquima.grid(row=cont, column=0, sticky=W)#se le puso el sticky W para que se justifique a la izquierda

    #crear cuadros de entrada
    cuadros_jaquimas.append('')#solo para crearla
    texto_jaquimas.append('')
    texto_jaquimas[cont] = StringVar()
    texto_jaquimas[cont].set('0')
    cuadros_jaquimas[cont] = Entry(panel_jaquimas,
                                   font=('Dosis', 16, 'bold'),
                                   bd=1,
                                   width=5,
                                   state=DISABLED,
                                   textvariable=texto_jaquimas[cont])
    cuadros_jaquimas[cont].grid(row=cont, column=1)#le colocamosel recuadro en cada checkbox
    cont += 1

#generar items monturas
variables_monturas = []
cuadros_monturas = []
texto_monturas = []
cont = 0
for montura in lista_monturas:
    variables_monturas.append('')
    variables_monturas[cont] = IntVar()#la convertimos en entero con funcion de tkinter
    montura = Checkbutton(panel_monturas, text=montura.title(), font=('Dosis', 19,'bold'), onvalue=1, offvalue=0,variable=variables_monturas[cont],command=revisar_checkbuton)
    montura.grid(row=cont, column=0, sticky=W)#se le puso el sticky W para que se justifique a la izquierda


    cuadros_monturas.append('')#solo para crearla
    texto_monturas.append('')
    texto_monturas[cont] = StringVar()
    texto_monturas[cont].set('0')
    cuadros_monturas[cont] = Entry(panel_monturas,
                                   font=('Dosis', 16, 'bold'),
                                   bd=1,
                                   width=5,
                                   state=DISABLED,
                                   textvariable=texto_monturas[cont])
    cuadros_monturas[cont].grid(row=cont, column=1)#le colocamosel recuadro en cada checkbox
    
    cont += 1


#variables
var_costo_pechera = StringVar()
var_costo_jaquima = StringVar()
var_costo_montura = StringVar()
var_subtotal = StringVar()
var_total = StringVar()

#etiquetas de costos y campos de entrada
etiqueta_costo_pechera = Label(panel_costos, text='Costos Pechera',font=('Dosis', 12, 'bold'), bg='gray64', fg='white')
etiqueta_costo_pechera.grid(row=0, column=0)


texto_costo_pechera = Entry(panel_costos,
                            font=('Dosis', 12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_pechera)
texto_costo_pechera.grid(row=0, column=1)


   
#variables

#etiquetas de costos y campos de entrada
etiqueta_costo_jaquima = Label(panel_costos, text='Costos Jaquima',font=('Dosis', 12, 'bold'), bg='gray64', fg='white')
etiqueta_costo_jaquima.grid(row=1, column=0)


texto_costo_jaquima = Entry(panel_costos,
                            font=('Dosis', 12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_jaquima)
texto_costo_jaquima.grid(row=1, column=1)

#etiquetas de costos y campos de entrada
etiqueta_costo_montura = Label(panel_costos, text='Costos Montura',font=('Dosis', 12, 'bold'), bg='gray64', fg='white')
etiqueta_costo_montura.grid(row=2, column=0)


texto_costo_montura = Entry(panel_costos,
                            font=('Dosis', 12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_montura)
texto_costo_montura.grid(row=2, column=1)


#etiquetas de sub total
etiqueta_total = Label(panel_costos, text='Total',font=('Dosis', 12, 'bold'), bg='gray64', fg='white')
etiqueta_total.grid(row=2, column=3)


texto_total = Entry(panel_costos,
                            font=('Dosis', 12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_total)
texto_total.grid(row=2, column=4)
columnas = 0
#botones
botones = ['total', 'recibo','guardar','resetear']#ya que entraran en loop
botonesCreados = []
#bobotn.tittle le pone a lo que sea que esta de titulo o sea lo recorrido
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14,'bold'),
                   fg='white',
                   bg='azure4',
                   width=9)
    botonesCreados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas+=1
botonesCreados[0].config(command=total)
botonesCreados[1].config(command=recibo)
botonesCreados[2].config(command=guardar)
#area del recibo
texto_recibo = Text(panel_recibo,
                    bd=1,
                    width=42,
                    height=10,
                    font=('Dosis', 14,'bold'))

texto_recibo.grid(row=0,
                  column=0)


#calculadora
visor_calculadora= Entry(panel_calculadora,
                         width=42,
                         bd=1,
                          font=('Dosis', 14,'bold'))
visor_calculadora.grid(row=0,column=0,columnspan=4)#columspan es para hacer una ampliacion de la columna
botones_calculadora = ['7','8','9','+',
                       '4','5','6','-',
                       '1','2','3','x',
                       'R','Borrar','0','/']

botones_guardados = []
fila =1
columnas = 0
for boton in botones_calculadora:
    if boton == 'Borrar':
        boton = Button(panel_calculadora,
                        text=boton.title(),
                        bd=1,
                        font=('Dosis', 16),
                        fg='red',
                        bg='gray64',
                        width=8)
    else:
        boton = Button(panel_calculadora,
                        text=boton.title(),
                        bd=1,
                        font=('Dosis', 14,'bold'),
                        fg='white',
                        bg='gray64',
                        width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila,
               column=columnas)
    if columnas ==3:
        fila+=1
    columnas+=1
    if columnas == 4:
        columnas = 0
#hacemos llamado a la funcion boton
botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton(''))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))
botones_guardados[1].config(command=lambda : click_boton('8'))


#evitar que la pantalla  se cierra
aplicacion.mainloop()