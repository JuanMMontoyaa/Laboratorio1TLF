import tkinter as tk
def mostrar_texto():
    texto = int(entry.get())
    if texto ==2:
        for widget in contenedor.winfo_children():
            widget.destroy()
        
        textC1 = tk.Label(contenedor, text="Ingresa el conjunto 1: ")
        textC1.pack()
        conjunto1 = tk.Entry(contenedor)
        conjunto1.pack()
        
        textC2 = tk.Label(contenedor, text="Ingresa el conjunto 2: ")
        textC2.pack()
        conjunto2 = tk.Entry(contenedor)
        conjunto2.pack()
        textC3 = tk.Label(contenedor, text="escribe la operacion que deseas hacer")
        textC3.pack()
        resultado = tk.Entry(contenedor)
        resultado.pack()
        resolver= tk.Button(contenedor, text="resolver", command= lambda: calcular2(conjunto1, conjunto2, resultado))
        resolver.pack()

    elif texto == 3:
        for widget in contenedor.winfo_children():
        # Destruir cada widget
            widget.destroy()
        textC1 = tk.Label(contenedor, text="Ingresa el conjunto 1: ")
        textC1.pack()
        conjunto1 = tk.Entry(contenedor)
        conjunto1.pack()
        
        textC2 = tk.Label(contenedor, text="Ingresa el conjunto 2: ")
        textC2.pack()
        conjunto2 = tk.Entry(contenedor)
        conjunto2.pack()
        
        textC3 = tk.Label(contenedor, text="Ingresa el conjunto 3: ")
        textC3.pack()
        conjunto3 = tk.Entry(contenedor)
        conjunto3.pack()
        textC4 = tk.Label(contenedor, text="escribe la operacion que deseas hacer")
        textC4.pack()
        resultado = tk.Entry(contenedor)
        resultado.pack()
        resolver= tk.Button(contenedor, text="resolver", command=lambda:calcular3(conjunto1, conjunto2, conjunto3, resultado))
        resolver.pack()

    else:
        for widget in contenedor.winfo_children():
        # Destruir cada widget
            widget.destroy()
        textC3 = tk.Label(contenedor, text="solo se pueden de a 2 o 3 conjuntos")
        textC3.pack()



def calcular2(conjunto1, conjunto2, operacion):
    con1 = conjunto1.get()
    con2 = conjunto2.get()
    oper = operacion.get()

    A = []
    B = []
    for i in range(len(con1)):
        if con1[i] != ',' and con1[i] != ' ':
            A.append(con1[i])
    print(A)
    
    for i in range(len(con2)):
        if con2[i] != ',' and con2[i] != ' ':
            B.append(con2[i])
    print(B)





def calcular3(conjunto1, conjunto2, conjunto3, operacion):
    con1 = conjunto1.get()
    con2 = conjunto2.get()
    con3 = conjunto3.get()
    oper = operacion.get()

    A = []
    B = []
    C = []
    for i in range(len(con1)):
        if con1[i] != ',' and con1[i] != ' ':
            A.append(con1[i])
    print(A)
    
    for i in range(len(con2)):
        if con2[i] != ',' and con2[i] != ' ':
            B.append(con2[i])
    print(B)
    for i in range(len(con3)):
        if con3[i] != ',' and con3[i] != ' ':
            C.append(con3[i])
    print(B)

root = tk.Tk()
root.geometry("400x400")
etiqueta = tk.Label(root, text="ingresa la cantidad de conjuntos (entre 2 y 3)")
etiqueta.pack()
entry = tk.Entry(root)
entry.pack()
# Crear un botón para mostrar el texto ingresado
boton = tk.Button(root, text="verificar", command=mostrar_texto)
boton.pack()
contenedor = tk.Frame(root, borderwidth=2, relief="groove")
contenedor.pack(padx=10, pady=10)
root.mainloop()