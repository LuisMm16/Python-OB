import tkinter


def seleccionado():
    texto_seleccion.config(text=f'La fruta seleccionada es: {fruta.get()}')

def reiniciar():
    fruta.set('Sin elegir')
    texto_seleccion.config(text='Seleccione alguna opcion')

ventana = tkinter.Tk()

fruta = tkinter.StringVar(ventana)
fruta.set('Sin elegir')

titulo = tkinter.Label(ventana, text='Seleccione su fruta preferida:')
titulo.grid(column=0, row=0, sticky=tkinter.W)

texto = tkinter.Text(ventana)
boton1 = tkinter.Radiobutton(ventana,
                             text='Manzana',
                             variable=fruta,
                             value='Manzana',
                             command=seleccionado)
boton1.grid(column=0, row=1, sticky=tkinter.W)

boton2 = tkinter.Radiobutton(ventana,
                             text='Pera',
                             variable=fruta,
                             value='Pera',
                             command=seleccionado)
boton2.grid(column=0, row=2, sticky=tkinter.W)

boton3 = tkinter.Radiobutton(ventana,
                             text='Banana',
                             variable=fruta,
                             value='Banana',
                             command=seleccionado)
boton3.grid(column=0, row=3, sticky=tkinter.W)

boton4 = tkinter.Radiobutton(ventana,
                             text='Mango',
                             variable=fruta,
                             value='Mango',
                             command=seleccionado)
boton4.grid(column=0, row=4, sticky=tkinter.W)

boton5 = tkinter.Button(ventana,
                        text='Reiniciar valores',
                        command=reiniciar)
boton5.grid(column=1, row=0, rowspan=6, sticky=tkinter.E)

texto_seleccion = tkinter.Label(ventana, text='Seleccione alguna opcion')
texto_seleccion.grid(column=0, row=6, sticky=tkinter.W)

ventana.mainloop()
