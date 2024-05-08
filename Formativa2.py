import os
import time

pik_rll=4500
ang_roll=4800
otk_rll=5000
plpv_rll=5200


x=True
y=1

while x==True:
    valortotal=0
    valorcondescuento=(valortotal*0.1)
    valordescuento=(valortotal*0.9)
    z=True
    pk=0
    an=0
    ot=0
    pl=0
    
    while y==1:
        print("¡Okaerinasaimase!╰(*°▽°*)╯ ¡Bienvenido a Otaku Rolls!")
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
            elif compra==2:
                print("Anguila Electrica Roll Agregado a su carrito")
                valortotal +=ang_roll
                an +=1
            elif compra==3:
                print("Otaku Roll Agregado a su carrito")
                valortotal +=otk_rll
                ot +=1
            elif compra==4:
                print("Pulpo venenoso Roll Agregado a su carrito")
                valortotal +=plpv_rll
                pl +=1
            elif compra==5:
                print("Procediendo con tu pedido （づ￣3￣）づ╭❤～")
                break
            elif compra==6:
                print("Sayonara (ノへ￣、)")
                valortotal=0
                y=2
            else:
                print("Ingresa un valor del 1-4")

        except ValueError:
                print("error, ingrese un valor del 1-4")
    

       

        
