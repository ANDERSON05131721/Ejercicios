def ordenes(rutinaContable):
    from functools import reduce

    ordenMinima = 600000
    ordenTotal = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])),
     rutinaContable))
    ordenTotal = list(map(lambda x: [x[0]] + [reduce(lambda a,b: round(a+b,2), x[1:])],
     ordenTotal)) 
    ordenTotal = list(map(lambda x : x if x [1] >= ordenMinima else (x[0], x[1]+25000),
     ordenTotal))
    
    print('------------------------ Inicio Registro diario ---------------------------------')
    for x in range(len(ordenTotal)):
        print(f"La factura {ordenTotal[x][0]} tiene un total en pesos de{ordenTotal[x][1]: ,.2f}")
    print('-------------------------- Fin Registro diario ----------------------------------')

rutinaContable =[
    [6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],
    [6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],
    [6591, ("7812", 2, 11.99), ("9652",11,18.99)],
  
    
    ]


      
ordenes(rutinaContable)