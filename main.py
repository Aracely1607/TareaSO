import random
import time
import libreria
import interfaz
import os


interfaz.menu()
interfaz.instrucciones()
caballos = input("¿Cuantos caballos desa que corran?(max.7):")
opcion = input("Seleccione un caballo: ")
interfaz.relleno()

#Aumenta a cada caballo un numero aleatorio de pasos entre 0 y 6
while caballos<150:
    
    caballos = caballos + random.randint(0,6)

    #Llama a la funcion caballo_* (diseño del caballo)
    #os.System("clr")
    interfaz.caballo_1(Caballo1)
    print("====================================================================================================================================================================")
    time.sleep(0.05)

#libreria.GanoCarrera(Caballo1,Caballo2,Caballo3,Caballo4,opcion)
libreria.Empate(Caballo1,Caballo2,Caballo3,Caballo4)

#Indica si Ganaste o Perdiste segun la opcion elegida
if libreria.GanoCarrera(Caballo1,Caballo2,Caballo3,Caballo4,opcion) == opcion:
    print("¡GANASTE!")
else:
    print("¡PERDISTE!")





