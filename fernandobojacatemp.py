temps =[]
tempmax = int(input())
tempmin = int(input())
tempsdia=[]
dias=0
diaError=0
diaErrormin=0
diaErrormax=0
diaErrormaxmin=0
suma=0
a=0
sumamin= 0
sumamax= 0
porcentajeError=0
media_mayor=0
media_menor=0

while (tempmin !=0 or tempmax !=0):
    if(tempmin < 5 or tempmax > 35 ):
        diaError = diaError + 1
        if(tempmin < 5 and tempmax > 35 ):
            diaErrormaxmin= diaErrormaxmin + 1
        elif(tempmin < 5 and tempmax <= 35 ):
            diaErrormin=diaErrormin + 1
        elif(tempmin >= 5 and tempmax > 35 ):
            diaErrormax= diaErrormax + 1
    elif(tempmin >= 5 and tempmax <= 35 ):
        suma=suma+ tempmin + tempmax
        a= a +1
        sumamin= sumamin + tempmin
        sumamax= sumamax + tempmax

        media_mayor= sumamax/a
        media_menor= sumamin/a
        
    temps.append(tempmax)
    temps.append(tempmin)
    tempsdia.append(temps)
    temps =[]
    tempmax = int(input())
    tempmin = int(input())
    dias=dias+1
    tempromedio= suma/((dias-diaError)*2)
    porcentajeError = (diaError*100)/dias 
  
print(dias)
print(diaError)
print(diaErrormin)
print(diaErrormax)
print(diaErrormaxmin)
print(media_mayor)
print(media_menor)
print(porcentajeError)


