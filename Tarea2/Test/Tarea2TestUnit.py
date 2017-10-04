import unittest
from Tarea2.Tarea2 import *

#Clase TestTarea, esta se encargara de realizar las pruebas sobre las funciones de
#nuestro script.
#Heredamos de unittest, esto nos dara una serie de capacidades de prueba.
class TestTarea(unittest.TestCase):
    
    #Tests de funcionamiento
    #Tests funcipn Tiempo de Trabajo

    def test_TiempoDeTrabajo(self):
        # Se calcularan 20 horas de trabajo
        InicioServicio = datetime(2017, 5, 31, hour=3, minute=20, second=0)
        FinalServicio = datetime(2017, 6, 3, hour=23, minute=0, second=0) #Notese los 20 minutos faltantes
        
        result = tiempoDeTrabajo(InicioServicio, FinalServicio)
        
        p = str(result)
        
        self.assertEqual(result, [69, 23], msg=p)

if __name__ == "__main__":
    unittest.main() 