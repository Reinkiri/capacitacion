Entn=5500
Entj=7000
Enta=9000
Totaln=0
Totalj=0
Totala=0
sw=1
total1=0
total2=0
total3=0
while sw==1:
    try:
        vOp=int(input("¿Que tipo de entrada quiere?: \n1.- Niño (1 a 13 años)\n2.- Jóven (14 a 21 años)\n3.- Adulto (Mayor a 22)\n4.- Salir\nDigite: "))
        if vOp==1:
            total=Entn
            cantent=int(input(f"El precio de su entrada es de ${Entn} pesos, ¿Cuántas entradas desea?\nDigite: "))
            total*=cantent
            Totaln+=cantent
            print(f"======BOLETA======\nCategoría: Niño\nCantidad de entradas: {cantent}\nTotal a pagar: ${total} pesos")
            total1=total
            print("Gracias por su compra, disfrute la función.")

        if vOp==2:
            total=Entj
            cantent=int(input(f"El precio de su entrada es de ${Entj} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total*=cantent
            Totalj+=cantent
            print(f"======BOLETA======\nCategoría: Jóven\nCantidad de entradas: {cantent}\nTotal a pagar: ${total} pesos")
            total2=total
            print("Gracias por comprar en nuestro cine , disfrute la función.")
            
        if vOp==3:
            total=Enta
            cantent=int(input(f"El precio de su entrada es de ${Enta} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total*=cantent
            Totala+=cantent
            print(f"======BOLETA======\nCategoría: Adulto\nCantidad de entradas: {cantent}\nTotal a pagar: ${total} pesos")
            total3=total
            print("Gracias por su compra, disfrute la función.")

        if vOp==4:
            sw=0
        
            

        
        
        
        totalent=(Totaln+Totalj+Totala)
        totaltodo= total1+total2+total3
        print(f"La cantidad de entradas para \"Niño\" vendidas es: {Totaln} ({((Totaln*1.00)//totalent)}% de las entradas totales.)")
        print(f"La cantidad de entradas para\"Jóven\" vendidas es: {Totalj} ({((Totalj*100)//totalent)}% de las entradas totales.)")
        print(f"La cantidad de entradas para \"Adulto\" vendidas es: {Totala} ({((Totala*100)//totalent)}% de las entradas totales.)")
        print(f"Total de ganancias del día: ${totaltodo} pesos")
    except ValueError:
        print("no valido")
        
       
        

    
    