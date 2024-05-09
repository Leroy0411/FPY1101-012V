import os
import time
time.sleep(2)

limpiarpantalla="cls"
pik_rll=4500
ang_roll=4800
otk_rll=5000
plpv_rll=5200
valortotal=0
totalproductos=0
aplicardescuento=False
z=True
pk=0
an=0
ot=0
pl=0

x=True
y=True
z=True

while x==True:

    
    while y==True:
        print("¡Okaerinasai mase!╰(*°▽°*)╯ ¡Bienvenido a Otaku Rolls!")
        print("Menu:")
        print(f"1 Pikachu Roll: {pik_rll}")
        print(f"2 Anguila Electrica Roll: {ang_roll}")
        print(f"3 Otaku Roll: {otk_rll}")
        print(f"4 Pulpo venenoso Roll: {plpv_rll}")
        print("5 nada mas")
        print("6 Cancelar compra")
        

        try:

            compra=int(input("Que deseas llevar? (ingrese un valor del 1-4)"))

            if compra==1:
                print("Pikachu roll agregado a su carrito")
                valortotal +=pik_rll
                pk +=1
                totalproductos +=1
                os.system(limpiarpantalla)
            elif compra==2:
                print("Anguila Electrica Roll Agregado a su carrito")
                valortotal +=ang_roll
                an +=1
                totalproductos +=1
                os.system(limpiarpantalla)
            elif compra==3:
                print("Otaku Roll Agregado a su carrito")
                valortotal +=otk_rll
                ot +=1
                totalproductos +=1
                os.system(limpiarpantalla)
            elif compra==4:
                print("Pulpo venenoso Roll Agregado a su carrito")
                valortotal +=plpv_rll
                pl +=1
                totalproductos +=1
                os.system(limpiarpantalla)
            elif compra==5:
                print("Procediendo con tu pedido （づ￣3￣）づ╭❤～")
                y=False
                time.sleep
                os.system(limpiarpantalla)
            elif compra==6:
                print("Sayonara (ノへ￣、)")
                valortotal=0
                x=False
                y=False
                z=False
            else:
                print("Ingresa un valor del 1-4")
        except ValueError:
                print("error, ingrese un valor del 1-4")

    while z==True:
        try:
            codigo_descuento=input("Ingresa codigo de descuento si no aplicas ninguno escribe x")
            if codigo_descuento=="soyotaku":
                print("Descuento aplicado con exito ╰(*°▽°*)╯")
                time.sleep
                os.system(limpiarpantalla)
                aplicardescuento=True
                z=False
            elif codigo_descuento=="x" or codigo_descuento=="X":
                print("Siguenos en Instagram para conseguir codgigos de descuento ^_^")
                z=False
                time.sleep
                os.system(limpiarpantalla)
            else:
                print("codigo erroneo intodruce un codigo valido (los codigos van en minusculas!!)")
        except ValueError:
            print ("introduce caracteres validos (solo letras)")
    valorcondescuento=valortotal*0.1
    valordescuento=valortotal*0.9
    if aplicardescuento==True:
        print("*************************************")
        print(f"Total de productos: {totalproductos}")
        print("*************************************")
        print(f"Pikachu Rolls: {pk}\nAnguila Electrica Rolls: {an}\nOtaku Rolls: {ot}\nPulpo Venenoso Rolls: {pl}")
        print("*************************************")
        print(f"Valor total a pagar:{valortotal}\nDescuento por codigo: {valordescuento}\nValor a pagar:{valorcondescuento}")
    elif aplicardescuento==False:
        print("*************************************")
        print(f"Total de productos: {totalproductos}")
        print("*************************************")
        print(f"Pikachu Rolls: {pk}\nAnguila Electrica Rolls: {an}\nOtaku Rolls: {ot}\nPulpo Venenoso Rolls: {pl}")
        print("*************************************")
        print(f"Valor total a pagar:{valortotal}\nDescuento por codigo: No aplica\nValor a pagar:{valortotal}")
    try:
        nuevopedido=int(input("¿Desea realizar un nuevo pedido? 1-Si 2-No"))
        if nuevopedido==1:
            z=True
            pk=0
            an=0
            ot=0
            pl=0
            x=True
            y=True
            z=True
            os.system(limpiarpantalla)
        elif nuevopedido==2:
            print("\(￣︶￣*\))")
            x=False
        else:
            print("ingresa 1 o 2")
    except ValueError:
        print("error introduce un valor correcto")