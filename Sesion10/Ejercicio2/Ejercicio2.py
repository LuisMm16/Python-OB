import tkinter as tk

ventana = tk.Tk()

pop = tk.IntVar(ventana, value=0)
rock = tk.IntVar(ventana, value=0)
edm = tk.IntVar(ventana, value=0)
salsa = tk.IntVar(ventana, value=0)

titulo = tk.Label(ventana, text='Seleccione que generos escucha con regularidad:')
titulo.grid(column=0, row=0)

boton1 = tk.Checkbutton(ventana, text='Pop', variable=pop)
boton1.grid(column=0, row=1)

boton2 = tk.Checkbutton(ventana, text='Rock', variable=rock)
boton2.grid(column=0, row=2)

boton3 = tk.Checkbutton(ventana, text='EDM', variable=edm)
boton3.grid(column=0, row=3)

boton4 = tk.Checkbutton(ventana, text='Salsa', variable=salsa)
boton4.grid(column=0, row=4)

ventana.mainloop()