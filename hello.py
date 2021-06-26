#Módulo introductorio a las pruebas básicas de Python.
def pruebas1():
    numero = int(input('degame un numero:'))
    numero2 = numero + 55
    print('su número es:',numero2)
    if (numero >= 100000):
        print("debe pagar impuestos")
        impuestos = float(numero+numero * 12/100)
        print("debe pagar:", impuestos)
    else:
        print("esta pobreton , no puede pagar")


def pelotica():
    for i in range(1,10):
        for j in range(i,i*i):
            print(" ",end='')
        print ("*")

    for i in range(10,1,-1):
        for j in range(i,i*i):
            print(' ',end='')
        print("*")        

#Inicio del programa principal 

msg = "Programa Principal"
print(msg+" otra cosa")
pelotica()
