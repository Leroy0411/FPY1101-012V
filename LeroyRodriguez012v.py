import os
import csv
import random
pedidos=[]
mainmenu=1 
def clean():
    os.system("cls")

def ingreso():
    npedido=random.randint(1, 1000)
    print(f"su numero de pedido es: {npedido}")
    nombre = input("Ingrese su nombre: ")
    direccion=input("ingrese su direccion")
    try:
        sector=int(input("Ingrese su sector:\n1-san bernardo\n2-Calera de tango\n3-Buin"))
    except ValueError:
        print("ingrese un numero entero del 1 al 3")
    try:
        sacos5kg=int(input("Ingrese la cantidad de sacos de 5kg que desea"))
    except ValueError:
        print("ingrese un valor correcto")
    try:
        sacos10kg=int(input("Ingrese la cantidad de sacos de 10kg que desea"))
    except ValueError:
        print("ingrese un valor correcto")
    try:
        sacos15kg=int(input("Ingrese la cantidad de sacos de 15kg que desea"))
    except ValueError:
        print("ingrese un valor correcto")
    cliente = {
        "Nº de pedido": npedido,
        "Nombre": nombre,
        "direccion": direccion,
        "sector": sector,
        "sacos 5kg": sacos5kg,
        "sacos 10kg": sacos10kg,
        "sacos 15kg": sacos15kg,
    }
    pedidos.append(cliente)
    print("pedido agregado exitosamente")

def cargar():
    if os.path.exists("pedidos.csv"):
        with open("pedidos.csv", mode="r", newline="") as archivo:
            reader = csv.DictReader(archivo)
            for i in reader:
                cargar = {
                    "Numero pedido": int(i["Numero pedido"]),
                    "Nombre": i["Nombre"],
                    "direccion": i["direccion"],
                    "sector": int(i["Sector"]),
                    "Saco 5kg": int(i["Saco 5kg"]),
                    "Saco 10kg": int(i["Saco 10kg"]),
                    "Saco 10kg": int(i["Saco 15kg"])
                }
                pedidos.append(cargar)
                print("pedido agregado")
                

def guardar():
    with open("pedidos.csv", mode="w", newline="") as archivo:
        campos = ["Nº de pedido", "Nombre", "direccion", "sector", "sacos 5kg", "sacos 10kg", "sacos 15kg"]
        escribir = csv.DictWriter(archivo, fieldnames=campos)
        escribir.writeheader()
        for pedido in pedidos:
            escribir.writerow({
                "Nº de pedido": pedido["Nº de pedido"],
                "Nombre": pedido["Nombre"],
                "direccion": pedido["direccion"],
                "sector": pedido["sector"],
                "sacos 5kg": pedido["sacos 5kg"],
                "sacos 10kg": pedido["sacos 10kg"],
                "sacos 15kg": pedido["sacos 15kg"]
            })

def listar():
    for pedido in pedidos:
        print(pedido)




while mainmenu==1:

    print("bienvenido a CatPremium ¿que desea hacer?")
    print("1- realizar un pedido")
    print("2- ver todos los pedidos")
    print("3- imprimir hoja de ruta")
    print("4- salir del programa")

    try:
        opc=int(input("seleccione una opcion con numeros del 1 al 4"))

        if opc==1:        
            ingreso()
            cargar()
            clean()
        elif opc==2:
            listar()
        elif opc==3:
            clean()
        elif opc==4:
            guardar()
            mainmenu=0
    except ValueError:
        print("Error introduce un numero entero del 1 al 4")
        continue





