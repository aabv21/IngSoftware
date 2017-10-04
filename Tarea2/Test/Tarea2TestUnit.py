import unittest
from Tarea2.Tarea2 import *

#Clase TestTarea, esta se encargara de realizar las pruebas sobre las funciones de
#nuestro script.
#Heredamos de unittest, esto nos dara una serie de capacidades de prueba.
class TestTarea(unittest.TestCase):
    
    #Tests de funcionamiento
    #Tests funcion Tiempo de Trabajo

    def test_TiempoDeTrabajo(self):
        ###PRUEBAS DE FUNCIONAMIENTO###
        #Miercoles a las 3 hasta sabado a las 23.
        InicioServicio = datetime(2017, 5, 31, hour=3, minute=20, second=0)
        FinalServicio = datetime(2017, 6, 3, hour=23, minute=0, second=0)
        
        result = tiempoDeTrabajo(InicioServicio, FinalServicio)
        
        #69 horas semana + 23 fin de semana
        self.assertEqual(result, [69, 23], msg="La prueba no fue satisfactoria")
        
        ###PRUEBAS DE FRONTERA###
        # Viernes a las 23:59:59 hasta Sabado a las 0:00:00 (menor a 15 minutos)
        InicioServicio3 = datetime(2017, 10, 6, hour=23, minute=59, second=59)
        FinalServicio3 = datetime(2017, 10, 7, hour=0, minute=0, second=0)
        
        result3 = tiempoDeTrabajo(InicioServicio3, FinalServicio3)
        
        #0 horas, no hay servicio
        self.assertEqual(result3, [0, 0], msg="La prueba no fue satisfactoria")
        
        
        #Viernes a las 23:00:00 hasta Viernes a las 23:15:00 (exactamente 15 minutos)
        InicioServicio4 = datetime(2017, 10, 6, hour=23, minute=0, second=0)
        FinalServicio4 = datetime(2017, 10, 6, hour=23, minute=15, second=0)
        
        result4 = tiempoDeTrabajo(InicioServicio4, FinalServicio4)
        
        #1 hora de semana
        self.assertEqual(result4, [1, 0], msg="La prueba no fue satisfactoria")
        
        #Viernes 6 a las 23:00:00 hasta Viernes 13 a las 23:00:01 (mas de 1 semana)
        InicioServicio5 = datetime(2017, 10, 6, hour=23, minute=0, second=0)
        FinalServicio5 = datetime(2017, 10, 13, hour=23, minute=0, second=1)
        
        result5 = tiempoDeTrabajo(InicioServicio5, FinalServicio5)
        
        #1 hora de semana
        self.assertEqual(result5, [0, 0], msg="La prueba no fue satisfactoria")
        
        #Viernes 6 a las 23:00:00 hasta Viernes 13 a las 23:00:00 (exactamente 1 semana)
        InicioServicio6 = datetime(2017, 10, 6, hour=23, minute=0, second=0)
        FinalServicio6 = datetime(2017, 10, 13, hour=23, minute=0, second=0)
        
        result6 = tiempoDeTrabajo(InicioServicio6, FinalServicio6)
        
        p=str(result6)
        
        #1 hora de semana
        self.assertEqual(result6, [120, 48], msg="La prueba no fue satisfactoria")
        
        ##OTRAS PRUEBAS###
        
        #Viernes a las 23:59:59 hasta Sabado a las 0:59:59
        InicioServicio2 = datetime(2017, 10, 6, hour=23, minute=59, second=59)
        FinalServicio2 = datetime(2017, 10, 7, hour=0, minute=59, second=59)
        
        result2 = tiempoDeTrabajo(InicioServicio2, FinalServicio2)
        
        #1 hora de semana, a pesar de que solo se tomo 1 segundo del dia de semana
        self.assertEqual(result2, [1, 0], msg="La prueba no fue satisfactoria")
        
    
    

if __name__ == "__main__":
    unittest.main() 