import unittest, math
from tareaSoft2 import *

#Clase TestTarea, esta se encargara de realizar las pruebas sobre las funciones de
#nuestro script.
#Heredamos de unittest, esto nos dara una serie de capacidades de prueba.
class TestTarea(unittest.TestCase):

    #Inicializacion del metodo SetUp
    def setUp(self):
	
	self.tf0 = tarifa(-1,-1)
	self.tf1 = tarifa(399.99, 425)
	self.tf2 = tarifa(150.50, 150.50)
	self.tf3 = tarifa(399.99999, 400.3102568)
	self.tf4 = tarifa(-8, -5)
    
    #Tests de funcionamiento
    #Tests funcion Tiempo de Trabajo

    def test_TiempoDeTrabajo(self):
        ###PRUEBAS DE FUNCIONAMIENTO###
        #Miercoles a las 3 hasta sabado a las 23.
        InicioServicio = datetime(2017, 5, 31, hour=3, minute=20, second=0)
        FinalServicio = datetime(2017, 6, 3, hour=23, minute=0, second=0)
        
        result = tiempoDeTrabajo(InicioServicio, FinalServicio)
        
        #69 horas semana + 23 fin de semana
        self.assertEqual(result, [69, 23])
        
        ###PRUEBAS DE FRONTERA###
        # Viernes a las 23:59:59 hasta Sabado a las 0:00:00 (menor a 15 minutos)
        InicioServicio3 = datetime(2017, 10, 6, hour=23, minute=59, second=59)
        FinalServicio3 = datetime(2017, 10, 7, hour=0, minute=0, second=0)
        
        result3 = tiempoDeTrabajo(InicioServicio3, FinalServicio3)
        
        #0 horas, no hay servicio
        self.assertEqual(result3, [0, 0])
        
        
        #Viernes a las 23:00:00 hasta Viernes a las 23:15:00 (exactamente 15 minutos)
        InicioServicio4 = datetime(2017, 10, 6, hour=23, minute=0, second=0)
        FinalServicio4 = datetime(2017, 10, 6, hour=23, minute=15, second=0)
        
        result4 = tiempoDeTrabajo(InicioServicio4, FinalServicio4)
        
        self.assertEqual(result4, [1, 0])
        
        #Viernes 6 a las 23:00:00 hasta Viernes 13 a las 23:00:01 (mas de 1 semana)
        InicioServicio5 = datetime(2017, 10, 6, hour=23, minute=0, second=0)
        FinalServicio5 = datetime(2017, 10, 13, hour=23, minute=0, second=1)
        
        result5 = tiempoDeTrabajo(InicioServicio5, FinalServicio5)
        
        self.assertEqual(result5, [0, 0])
        
        #Viernes 6 a las 23:00:00 hasta Viernes 13 a las 23:00:00 (exactamente 1 semana)
        InicioServicio6 = datetime(2017, 10, 6, hour=23, minute=0, second=0)
        FinalServicio6 = datetime(2017, 10, 13, hour=23, minute=0, second=0)
        
        result6 = tiempoDeTrabajo(InicioServicio6, FinalServicio6)
                
        self.assertEqual(result6, [120, 48])
        
        ##OTRAS PRUEBAS###
        
        #Viernes a las 23:59:59 hasta Sabado a las 0:59:59
        InicioServicio2 = datetime(2017, 10, 6, hour=23, minute=59, second=59)
        FinalServicio2 = datetime(2017, 10, 7, hour=0, minute=59, second=59)
        
        result2 = tiempoDeTrabajo(InicioServicio2, FinalServicio2)
        
        #1 hora de semana, a pesar de que solo se tomo 1 segundo del dia de semana y 59 minutos del fin de semana
        self.assertEqual(result2, [1, 0])

        #Domingo a las 11:59:59 hasta Lunes a las 0:14:59 (15 minutos y caso de fin de semana mas corto)
        InicioServicio7 = datetime(2017, 10, 8, hour=23, minute=59, second=59)
        FinalServicio7 = datetime(2017, 10, 9, hour=0, minute=14, second=59)

        result7 = tiempoDeTrabajo(InicioServicio7, FinalServicio7)

        self.assertEqual(result7, [0, 1])
        
    def test_Tarifa(self):
        ###PRUEBAS DE FUNCIONAMIENTO###
        
        # Tarifa de Bs399 con 99 centimos en dia de semana y Bs425 en fin de semana 
        
        #tf1 = tarifa(399.99, 425)
        
        # Se trabajan 5 horas el dia de semana y 8 el fin de semana
        
        self.assertEqual(self.tf1.tarifaSemana(5), 1999.95)
        self.assertEqual(self.tf1.tarifaFinDeSemana(8), 3400)

        ###PRUEBAS DE FRONTERA###
        # Tarifa de dia de semana igual a fin de semana
        #tf1 = tarifa(150.50, 150.50)

        #Es necesario que las tarifas de los dias de semanas siempre sean distintas a las del fin de semana
        self.assertTrue(self.tf2.tarifaSemanales < self.tf2.tarifaFinSemanales)

        #La manera en la que se resuelve este error es cambiando la tarifa del fin de semana al mismo valor de la tarifa
        # del dia de semana + 1
        self.assertEqual(self.tf2.tarifaSemanales, self.tf2.tarifaFinSemanales - 1)


        # Tarifa con valores de decimas de centimo
        #tf1 = tarifa(399.99999, 400.3102568)

        #El numero es multiplicado por 100, redondeado HACIA ARRIBA, y dividido entre 00
        ValorSemana = math.ceil(self.tf3.tarifaSemanales * 100)/100
        ValorFindeSemana = math.ceil(self.tf3.tarifaFinSemanales * 100)/100

        #Si la igualdad se mantiene, tiene 2 o menos digitos
        self.assertEqual(self.tf3.tarifaSemanales, ValorSemana)
        self.assertEqual(self.tf3.tarifaFinSemanales, ValorFindeSemana)

        # Tarifa con valores negativos
        #tf1 = tarifa(-8, -5)

        # Al encontrar tarifas negativas se pondran en 0 por defecto, esto asegurara que el programa responda con un no hay servicio
        self.assertTrue(self.tf4.tarifaSemanales == 0 and self.tf4.tarifaFinSemanales == 0, msg = self.tf4.tarifaFinSemanales)

    def test_calcularPrecio(self):
        ###PRUEBAS DE FUNCIONAMIENTO###
        # Miercoles a las 3 hasta sabado a las 23.
        # Tarifa de Bs399 con 99 centimos en dia de semana y Bs425 en fin de semana 
        InicioServicio = datetime(2017, 5, 31, hour=3, minute=20, second=0)
        FinalServicio = datetime(2017, 6, 3, hour=23, minute=0, second=0)
        tiempo = tiempoDeTrabajo(InicioServicio, FinalServicio)
        #tf1 = tarifa(399.99, 425)

        result = calcularPrecio(self.tf1, tiempo)

        self.assertEqual(37374.31, result)

        ###PRUEBAS DE FRONTERA###

        #Errores de entrada en el tiempo de trabajo o en las tarifas daran como valores por defecto
        #0 en tiempo y 0 en tarifa de dia de semana y 0 en tarifa de fin de semana respectivamente 
        InicioServicio0 = datetime(2017, 5, 31, hour=0, minute=0, second=0)
        FinalServicio0 = datetime(2017, 5, 3, hour=0, minute=0, second=0)
        tiempo0 = tiempoDeTrabajo(InicioServicio0, FinalServicio0)
        #tf0 = tarifa(-1,-1)

        result1 = calcularPrecio(self.tf1, tiempo0)
        self.assertEqual(0, result1)
        result2 = calcularPrecio(self.tf0, tiempo)
        self.assertEqual(0, result2)
        result3 = calcularPrecio(self.tf0, tiempo0)
        self.assertEqual(0, result3)

if __name__ == "__main__":
    unittest.main() 
