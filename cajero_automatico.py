
saldo = 500000
opciones = int(input("1.consultar saldo,2.Retirar dinero,3.Depositar dinero,4.salir: "))
opcion = ["Consultar_saldo","Retirar_dinero","Depositar_dinero","salir"]

print(opcion[opciones - 1])


if opciones == 1:
    print("1. Consultar saldo \nSaldo disponible: " + str(saldo))
elif opciones == 2:
    print("2. Retirar dinero: ") 
    cantidad = int(input("¿Cuánto dinero desea retirar?: "))
    saldo_disponible = (saldo - cantidad)
    print("Retiro exitoso.\n saldo disponible: " + str(saldo_disponible))
    
elif opciones == 3:
    print("3. Depositar dinero")
    cantidad = int(input("¿Cuánto dinero desea depositar?: "))
    nuevo_saldo_disponible = (saldo + cantidad)                  
    print("Depósito exitoso.\n Saldo disponible: " + str(nuevo_saldo_disponible))
elif opciones == 4:
    print("4. Salir Gracias por utilizar el cajero.")