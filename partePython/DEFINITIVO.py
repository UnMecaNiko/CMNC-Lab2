from tkinter import Tk, Frame, Button, Label, ttk
import serial
import collections
from threading import Thread
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D


#VARIABLES
global L1, L2, L3,Boton1,Boton2,Boton3
L1 = 0; L2 = 0;L3 = 0;Boton1 = 0;Boton2 = 0;Boton3 = 0
Muestras = 70 ; grafiacas = []; datos = []



#FUNCIONES BOTON
def B1():
    global Boton1, Boton2, Boton3
    Boton1 = 1;    Boton2 = 0;    Boton3 = 0
def B2():
    global Boton1, Boton2, Boton3
    Boton1 = 1;  Boton2 = 0;   Boton3 = 0
def B3():
    global Boton1, Boton2, Boton3
    Boton1 = 0;    Boton2 = 0;    Boton3 = 1
def B4():
    global Boton1, Boton2, Boton3
    Boton1 = 1;    Boton2 = 1;  Boton3 = 1

#FUNCION LED
def led1():
    global L1
    if L1 == 0:
        SerialC.write(b'11')
        L1 = 1
    else:
        SerialC.write(b'10')
        L1 = 0
        
def led2():
    global L2
    if L2 == 0:
        SerialC.write(b'21')
        L2 = 1
    else:
        SerialC.write(b'20')
        L2 = 0
        
def led3():
    global L3
    if L3 == 0:
        SerialC.write(b'31')
        
        L3 = 1
    else:
        SerialC.write(b'30')
        L3 = 0
#MODIFICACION GUI
window = Tk()  # Ventana principal
window.geometry('1200x500')
window.wm_title('Comunicaciones Lab 1 ')
window.minsize(width=1200, height=500)

frame4 = Frame(window, bd=1)
frame4.grid(column=0, row=1)
frame5 = Frame(window, bd=1)
frame5.grid(column=1, row=2)

BB1 = Button(text='Boton1', width=15, bg='white', fg='blue', command=B1).grid(column=0, row=1, pady=5, padx=10)
BB2 = Button(text='Boton2', width=15, bg='white', fg='blue', command=B2).grid(column=1, row=1, pady=5, padx=10)
BB3 = Button(text='Boton3', width=15, bg='white', fg='blue', command=B3).grid(column=2, row=1, pady=5, padx=10)
BB4 = Button(text='Boton4', width=15, bg='white', fg='blue', command=B4).grid(column=3, row=1, pady=5, padx=10)
BB5 = Button(frame5, text='LED 1', width=15, bg='black', fg='red', command=led1).grid(column=0, row=2, pady=5, padx=10)
BB6 = Button(frame5, text='LED 2', width=15, bg='black', fg='red', command=led2).grid(column=1, row=2, pady=5, padx=10)
BB7 = Button(frame5, text='LED 3', width=15, bg='black', fg='red', command=led3).grid(column=2, row=2, pady=5, padx=10)
#SERIAL
try:
    SerialC = serial.Serial('COM7', 115200)
except:
    print('Error conexion')

for x in np.arange(0,3):
    datos.append(collections.deque([0] * Muestras, maxlen=Muestras))
    datos[x]=np.arange(0,5,5/Muestras)
    grafiacas.append(Line2D([], [], color='red',))

def GetDatos():
    global Muestras
    while True:
        valorSerial = SerialC.readline().decode('ascii').strip()
        if valorSerial:
            pos = valorSerial.index(":")
            label = valorSerial[:pos]
            value = valorSerial[pos + 1:]
            if label == 'pot1':
                datos[0] = np.roll(datos[0], -1)
                datos[0][Muestras - 1] = float(value)
                print(value)

            if label == 'TEM':
                datos[1] = np.roll(datos[1], -1)
                datos[1][Muestras - 1] = float(value)
                print(value)
            if label == 'POT':
                datos[2] = np.roll(datos[2], -1)
                datos[2][Muestras - 1] = float(value)
                print(value)

#GRAFICAS FUNCION
def graficar1(*args):
    global Boton1
    if Boton1 == 1:
        grafiacas[0].set_data(range(Muestras), datos[0])
def graficar2(*args):
    global Boton2
    if Boton2 == 1:
        grafiacas[1].set_data(range(Muestras), datos[1])
def graficar3(*args):
    global Boton3
    if Boton3 == 1:
        grafiacas[2].set_data(range(Muestras), datos[2])

#GRAFICACION FIGS
figura1 = plt.figure(figsize = (3,3),facecolor='blue')
EJES = plt.axes(xlim=(0, Muestras), ylim=(0,5))
plt.title('CNY70 (Distancia)')
plt.grid()
EJES.set_xlabel('Muestra')
EJES.set_ylabel('(cm)')
grafiacas[0]=EJES.plot([],[])[0]
canvas = FigureCanvasTkAgg(figura1, master=window)
canvas._tkcanvas.grid(row=0, column=0, pady=15, padx=10)

figura2 = plt.figure(figsize = (3,3),facecolor='blue')
EJES2 = plt.axes(xlim=(0, Muestras), ylim=(20,70))
plt.title('LM35 (Temperatura)')
plt.grid()
EJES2.set_xlabel('Muestra')
EJES2.set_ylabel('(°C)')
grafiacas[1]=EJES2.plot([],[])[0]
canvas2 = FigureCanvasTkAgg(figura2, master=window)
canvas2._tkcanvas.grid(row=0, column=1, pady=15, padx=10)

figura3 = plt.figure(figsize = (3,3),facecolor='blue')
EJES3 = plt.axes(xlim=(0, Muestras), ylim=(0,5.5))
plt.title('POT (Tensión)')
plt.grid()
EJES3.set_xlabel('Muestra')
EJES3.set_ylabel('(V)')
grafiacas[2]=EJES3.plot([],[])[0]
canvas3 = FigureCanvasTkAgg(figura3, master=window)
canvas3._tkcanvas.grid(row=0, column=2, pady=15, padx=10)

Linea = Thread(target=GetDatos)
Linea.start()

#ANIMACIONES
anim = animation.FuncAnimation(figura1, graficar1, fargs=(grafiacas), interval=Muestras)
anim2 = animation.FuncAnimation(figura2, graficar2, fargs=(grafiacas), interval=Muestras)
anim3 = animation.FuncAnimation(figura3, graficar3, fargs=(grafiacas), interval=Muestras)

window.mainloop()
SerialC.close()