import os
os.system

menu="""

-----------------------------------

1-Comprar entradas
2-Mostrar ubicaciones disponibles
3-Ver listado de asistentes
4-Mostrar ganancias totales
5-Salir

-----------------------------------
"""

int(input(menu))
opc=int(input)
while opc==1:
    try:
        int(input(opc))
        if opc==1:
            print("Comprar entradas")

        listaEntradas=['Platinum $120000','Gold 80000','Silver $50000']
        print("¿Que entradas desea comprar?")

        print("-----Valor de cada entrada-----\n")
        print(listaEntradas)

        Platinum=120000
        Gold=80000
        Silver=50000
  
        listaPlatinum=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        listaGold=[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
        listaSilver=[52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
        listaEntDisp=[listaPlatinum,listaGold,listaSilver]

        EntPlatinum=int(input *(Platinum))
        listaPlatinum.append['X']
        EntGold=int(input *(Gold))
        listaGold.append['X']
        EntSilver=int(input *(Silver))
        listaSilver.append['X']

        input("Ingrese su RUN")
        len(8)
        break
    
    except:
        print("Numero ingresado fuera de rango")

    
while opc==2:
    try:
        int(input(opc))
        if opc==2:
            print("-----Ubicaciones Disponibles-----")
            print(listaEntDisp)
            break
    except:
        ("No quedan ubicaciones disponibles")
while opc==3:
    print("-----Listado de Asistentes-----")

    listaAsist=['193117437','149978252','212014631','162948402','199342444']
    listaAsist.sort
    print(listaAsist)
    break

while opc==4:
    print("Ganancias totales")

    print("Ganancias recaudadas de las entradas:   ")

    print(Platinum+Gold+Silver)
    break
while opc==5:
    print("Salir")
    break
input("Enter para terminar")
