'''
Created on 30 sept. 2017

@author: aabv
'''

from datetime import datetime, date, time, timedelta

print("Introduzca la fecha y hora de inicio del Servicio dd-mm--aaaa-hh-mm-ss: ")
diaI = int(input("dia: "))
mesI = int(input("mes : "))
anyoI = int(input("anyo: "))
segI = int(input("segundos: "))
minI = int(input("minutos: "))
horI = int(input("horas: "))
iServicio = datetime(anyoI, mesI, diaI, hour=horI, minute=minI, second=segI)
print(iServicio)

print("Introduzca la fecha y hora de fin del Servicio dd-mm--aaaa-hh-mm-ss: ")
diaF = int(input("dia: "))
mesF = int(input("mes : "))
anyoF = int(input("anyo: "))
segF = int(input("segundos: "))
minF = int(input("minutos: "))
horF = int(input("horas: "))
fServicio = datetime(anyoF, mesF, diaF, hour=horF, minute=minF, second=segF)
print(fServicio)

# Funcion que determina las horas trabajadas dependiendo de si fue un dia de la semana o fin de semana

def tiempoDeTrabajo(inicioDeServicio, finDeServicio):
    
    serv = finDeServicio - inicioDeServicio
    serv = serv.total_seconds()
    horasTrabajadasSemanales = 0
    horasTrabajadasFinSemanales = 0 
    es_trabajo = False
    
    while not es_trabajo:
        
        dia = inicioDeServicio.weekday()
        
        if 0 <= dia <= 4:
    
            if serv > 60:
                horasTrabajadasSemanales += 1
                serv = serv -3600
            
            else:
                es_trabajo = True
                
        elif 5 <= dia <= 6:
            
            if serv > 60:            
                horasTrabajadasFinSemanales += 1
                serv = serv -3600
        
        inicioDeServicio = inicioDeServicio + timedelta(hours=1)
        
    horasTrabajadas = [horasTrabajadasSemanales, horasTrabajadasFinSemanales]    
    
    return horasTrabajadas

# Clase que permite hacer una taza del precio a pagar dependiendo del dia y horas trabajadas


class tarifa:
    
    def __init__(self, tarifaSemanales, tarifaFinSemanales):
        
        self.tarifaSemanales = tarifaSemanales
        self.tarifaFinSemanales = tarifaFinSemanales
    
    def tarifaFinDeSemana(self, numeroHorasFinSemanales):    
        return self.tarifaFinSemanales*numeroHorasFinSemanales
    
    def tarifaSemana(self, numeroHorasSemanales):   
        return self.tarifaSemanales*numeroHorasSemanales 
    
def calcularPrecio(tarifa, tiempoDeServicio):
    
    precio = 0
    
    precio = tarifa.tarifaFinDeSemana(tiempoDeServicio[0])
    precio = precio + tarifa.tarifaFinDeSemana(tiempoDeServicio[1])
    
    return precio         
    
#######################
###Programa
#######################

#300 hora semanal
#500 hora fin de semana

tf = tarifa(300, 500)
minimo = timedelta(minutes= 15)
maximo = timedelta(weeks=1)
servicio = fServicio - iServicio
   
if minimo <= servicio and servicio <= maximo:
    tiempoDeServicio = tiempoDeTrabajo(iServicio, fServicio)
    print("Hora Semanales: " +str(tiempoDeServicio[0]) + "Hora Fin Semanales: " +str(tiempoDeServicio[1]))
    precio = calcularPrecio(tf, tiempoDeServicio)
    print("Usted debe pagar: "+str(precio)+ " bsf")
    
else:
    print("No es un servicio")
    
     
    
    
                

