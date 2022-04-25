import random
import time
import libreria
import interfaz
import os

#Todos los caballos parten desde los 0 pasos
Caballo1 = 0
Caballo2 = 0
Caballo3 = 0
Caballo4 = 0

interfaz.menu()
interfaz.instrucciones()
opcion = input("Seleccione un caballo: ")
interfaz.relleno()

#Aumenta a cada caballo un numero aleatorio de pasos entre 0 y 6
while Caballo1<150 and Caballo2<150 and Caballo3<150 and Caballo4<150:
    
    Caballo1 = Caballo1 + random.randint(0,6)
    Caballo2 = Caballo2 + random.randint(0,6)
    Caballo3 = Caballo3 + random.randint(0,6)
    Caballo4 = Caballo4 + random.randint(0,6)

    #Llama a la funcion caballo_* (diseño del caballo)
    os.System("clr")
    interfaz.caballo_1(Caballo1)
    interfaz.caballo_2(Caballo2)
    interfaz.caballo_3(Caballo3)
    interfaz.caballo_4(Caballo4)
    print("====================================================================================================================================================================")
    time.sleep(0.05)

#libreria.GanoCarrera(Caballo1,Caballo2,Caballo3,Caballo4,opcion)
libreria.Empate(Caballo1,Caballo2,Caballo3,Caballo4)

#Indica si Ganaste o Perdiste segun la opcion elegida
if libreria.GanoCarrera(Caballo1,Caballo2,Caballo3,Caballo4,opcion) == opcion:
    print("¡GANASTE!")
else:
    print("¡PERDISTE!")





