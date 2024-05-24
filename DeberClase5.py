#ingreso de datos 
a = True    
b = True
print(" ******** BIENVENIDO AL BURGER KING ******")
print("")
print("Ingrese los datos para la factura electrónica")
print("")
print("")

nombre = input("Por favor ingrese su nombre: ")
cedula = int(input("Ingrese su número de cedula: "))
correoE = input("Ingrese su correo: ")
numH = int(input("Ingrese el número de hamburgesas a adquirir: "))


#proceso de datos 
print("Ingrese uno de los siguientes tipos de hamburgesas: ")
print("1) Sencilla")
print("2) Doble")
print("3) Triple")
opc1 =int(input("Ingrese la opción:"))

match opc1:
    case 1:
        cos = float(1.50)
    case 2:       
        cos = float(2.50)
    case 3:
        cos = float(3.25)
    case _:
        a = False


if a == True :
    precio = float(cos*numH)
    print("")
    print("Ingrese su forma de pago : ")
    print("1) Tarjeta de credito")
    print("2) Efectivo")
    opc2 =int(input("Ingrese la opción:"))

    match opc2:
        case 1:
            aume = float(precio*0.05)
        case 2:       
            aume = float(0)
        case _:
            b = False
else:
    print("")
    print("Este tipo de hamburgesa no existe")
    print("Muchas gracias")
    breakpoint



#Salida de datos 

if a == True and b == True:
    preciof = round(float(precio+aume),2)
    print("")
    print(f"Genial, {nombre} el precio final a pagar es ${preciof}")
    print(f"La factura se enviará a su correo {correoE}")
elif a==True and b==False:
    print("")
    print("No existe este tipo de pago")
    print("Muchas gracias ")