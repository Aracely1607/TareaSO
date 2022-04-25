import time

#Diseño del caballo
def caballo_1(Caballo1):
    print(Caballo1*" ","  ___ ")
    print(Caballo1*" ","/|-1-|UwU")
    print(Caballo1*" "," |   |")

def caballo_2(Caballo2):
    print(Caballo2*" ","  ___ ")
    print(Caballo2*" ","/|-2-|UwU")
    print(Caballo2*" "," |   |")

def caballo_3(Caballo3):
    print(Caballo3*" ","  ___ ")
    print(Caballo3*" ","/|-3-|UwU")
    print(Caballo3*" "," |   |")

def caballo_4(Caballo4):
    print(Caballo4*" ","  ___ ")
    print(Caballo4*" ","/|-4-|UwU")
    print(Caballo4*" "," |   |")

def menu():
    print("---------------------------------------------")
    print("---- Bienvenido a la carrera de caballos ----")
    print("---------------------------------------------\n")

def instrucciones():
    print("=========== Seleccione su caballo ===========")
    print("1. AyudanteDeSanta")
    print("2. CaballoVeloz")
    print("3. Trueno")
    print("4. ScoobyDoo")

def relleno():
    print("Cargando Carrera....")
    time.sleep(2)
    print("Alimentando a los caballos...")
    time.sleep(2)
    print("Carrera lista en...")
    time.sleep(2)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Partierooooooon!!!!!")
    time.sleep(1)