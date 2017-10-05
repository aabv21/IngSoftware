'''
Created on 30 sept. 2017

@author: aabv
'''
#
from datetime import datetime, timedelta

# Funcion que determina las horas trabajadas dependiendo de si fue un dia de la semana o fin de semana
# tuple(datetime, datetime) -> int
def tiempoDeTrabajo(inicioDeServicio, finDeServicio):
    
    minimo = timedelta(minutes= 15)
    maximo = timedelta(weeks=1)
    servicio = finDeServicio - inicioDeServicio
    horasTrabajadas = [0, 0]
    
    if minimo <= servicio and servicio <= maximo:
    
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
                
                else:
                    es_trabajo = True
            
            inicioDeServicio = inicioDeServicio + timedelta(hours=1)
                 
        horasTrabajadas = [horasTrabajadasSemanales, horasTrabajadasFinSemanales]    
        
    else:
        pass
        
    return horasTrabajadas    

# Clase que permite hacer una taza del precio a pagar dependiendo del dia y horas trabajadas
    
class tarifa:
    
    def __init__(self, tarifaSemanales, tarifaFinSemanales):
        
        self.tarifaSemanales = 0
        self.tarifaFinSemanales = 1
        
        if tarifaSemanales >= 0 and tarifaFinSemanales >= 0:
            if tarifaSemanales != tarifaFinSemanales:
                self.tarifaSemanales = round(tarifaSemanales, 2)
                self.tarifaFinSemanales = round(tarifaFinSemanales, 2)
            else:
                self.tarifaSemanales = round(tarifaSemanales, 2)
                self.tarifaFinSemanales = self.tarifaSemanales+1
        else:
            self.tarifaFinSemanales = 0

    
    def tarifaFinDeSemana(self, numeroHorasFinSemanales):    
        return float(int(self.tarifaFinSemanales*numeroHorasFinSemanales*100))/100
    
    def tarifaSemana(self, numeroHorasSemanales):   
        return float(int(self.tarifaSemanales*numeroHorasSemanales*100))/100


# Funcion calcularPrecio
# tuple(float, int) -> float

def calcularPrecio(tarifa, tiempoDeServicio):
    
    precio = 0
    
    if(tiempoDeServicio[0] == 0 and tiempoDeServicio[1] == 0):
        pass
    
    else:
    	
        precio = tarifa.tarifaSemana(tiempoDeServicio[0])
        precio = precio + tarifa.tarifaFinDeSemana(tiempoDeServicio[1])
        
    return precio         
    




    
     
    
    
                

