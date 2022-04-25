#El primer caballo que llegue a 150 pasos gana.
def GanoCarrera(Caballo1,Caballo2,Caballo3,Caballo4,opcion):
    if Caballo1 >=150 and (Caballo1 > Caballo2 and Caballo3 and Caballo4):
        print("Gano el Caballo 1 - AyudanteDeSanta y tu opcion fue", opcion)

    if Caballo2 >=150 and (Caballo2 > Caballo1 and Caballo3 and Caballo4):
        print("Gano el Caballo 2 - CaballoVeloz y tu opcion fue", opcion)

    if Caballo3 >=150 and (Caballo3 > Caballo1 and Caballo2 and Caballo4):
        print("Gano el Caballo 3 - Trueno y tu opcion fue", opcion)

    if Caballo4 >=150 and (Caballo4 > Caballo1 and Caballo2 and Caballo3):
        print("Gano el Caballo 4 - ScoobyDoo y tu opcion fue", opcion)



#Si 2 caballo llegan al mismo tiempo se declara un empate
def Empate(Caballo1,Caballo2,Caballo3,Caballo4):
    if Caballo1 == Caballo2:
        Caballo1>=150
        print("empate")
    if Caballo1 == Caballo3:
        Caballo1>=150
        print("empate")
    if Caballo1 == Caballo4:
        Caballo1>=150
        print("empate")
    if Caballo2 == Caballo3:
        Caballo2>=150
        print("empate")
    if Caballo2 == Caballo4:
        Caballo2>=150
        print("empate")
    if Caballo3 == Caballo4:
        Caballo3>=150
        print("empate")



