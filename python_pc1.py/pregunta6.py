edad=int(input("¿Que edad tienes?"))
if 0< edad <4 :
    print("Entra gratis")
elif 4 <= edad <= 18 :
    print("Debe pagar 5$")
elif edad > 18 :
    print("Debe pagar 10$")