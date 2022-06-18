from ast import Num

def numeroDeCelular (num):
    if len(num) == 10:
        print("Ya puede navegar")
    else:
        print("El numero de celular debe tener 10 digitos") 
    return int(num)

def menuFn():
    menu = """
Compra de paquete de datos 
1 - 1GB + 200 mins + redes sociales  
2 - 3GB + 500 mins + redes sociales
3 - 5GB + 1000 mins + redes sociales
Elige una opcion: """

    opcion = int(input(menu))

    if opcion == 1:
        numero_de_celular = input("""Paquete 1 valor $20000 \nIngrese numero de celular:""")
        numeroDeCelular (numero_de_celular)  
        
    elif opcion == 2:
        numero_de_celular = input("""Paquete 2 valor $30000 \nIngrese numero de celular:""")
        numeroDeCelular (numero_de_celular) 
        
    elif opcion == 3:
        numero_de_celular = input("""Paquete 3 valor $50000 \nIngrese numero de celular:""")
        numeroDeCelular (numero_de_celular)

    else:
        print("Ingrese una opcion correcta")

while True: 
    menuFn()




