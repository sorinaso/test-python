import unittest, random
from ejercicio_2 import *

RUEDAS = random.randint(1,16)
COLOR = 'rojo'
VELOCIDAD = 100
CILINDRADA = 330
CARGA = 2800
RUEDAS_INVALIDO = random.choice((3.2, "3.2", "abc"))
TIPO_INVALIDO = 'tipoinvalido'
VELOCIDAD_INVALIDO = random.choice((3.2, "3.2", "abc"))
CILINDRADA_INVALIDO = random.choice((3.2, "3.2", "abc"))
CARGA_INVALIDO = random.choice((3.2, "3.2", "abc"))

class TestVehiculo(unittest.TestCase):
    def test_constructor(self):
        test_object = Vehiculo(color=COLOR, ruedas=RUEDAS)

        self.assertEqual(test_object.color, COLOR)
        self.assertEqual(test_object.ruedas, RUEDAS)

        self.assertRaises(AttributeError, lambda: Vehiculo(color=COLOR, ruedas=RUEDAS_INVALIDO))

class TestCoche(unittest.TestCase):
    def test_constructor(self):
        test_object = Coche(color=COLOR, velocidad=VELOCIDAD, cilindrada=CILINDRADA)

        self.assertEqual(test_object.color, COLOR)
        self.assertEqual(test_object.cilindrada, CILINDRADA)
        self.assertEqual(test_object.velocidad, VELOCIDAD)

        self.assertRaises(AttributeError, lambda: Coche(color=COLOR, velocidad=VELOCIDAD_INVALIDO, cilindrada=CILINDRADA))
        self.assertRaises(AttributeError, lambda: Coche(color=COLOR, velocidad=VELOCIDAD, cilindrada=CILINDRADA_INVALIDO))

class TestCamioneta(unittest.TestCase):
    def test_constructor(self):
        test_object = Camioneta(color=COLOR, velocidad=VELOCIDAD, cilindrada=CILINDRADA, carga=CARGA)

        self.assertEqual(test_object.color, COLOR)
        self.assertEqual(test_object.cilindrada, CILINDRADA)
        self.assertEqual(test_object.velocidad, VELOCIDAD)
        self.assertEqual(test_object.carga, CARGA)

        self.assertRaises(AttributeError, lambda: Camioneta(color=COLOR, velocidad=VELOCIDAD_INVALIDO, cilindrada=CILINDRADA, carga=CARGA))
        self.assertRaises(AttributeError, lambda: Camioneta(color=COLOR, velocidad=VELOCIDAD, cilindrada=CILINDRADA_INVALIDO, carga=CARGA))
        self.assertRaises(AttributeError, lambda: Camioneta(color=COLOR, velocidad=VELOCIDAD, cilindrada=CILINDRADA, carga=CARGA_INVALIDO))

class TestBicicleta(unittest.TestCase):
    def test_constructor(self):
        test_object = Bicicleta(color=COLOR, tipo=Bicicleta.Tipo.URBANA)

        self.assertEqual(test_object.color, COLOR)
        self.assertEqual(test_object.ruedas, 2)
        self.assertEqual(test_object.tipo, Bicicleta.Tipo.URBANA)

        self.assertRaises(AttributeError, lambda: Bicicleta(color=COLOR, tipo=TIPO_INVALIDO))

class TestMotocicleta(unittest.TestCase):
    def test_constructor(self):
        test_object = Motocicleta(color=COLOR, tipo=Bicicleta.Tipo.URBANA, velocidad=VELOCIDAD, cilindrada=CILINDRADA)

        self.assertEqual(test_object.color, COLOR)
        self.assertEqual(test_object.ruedas, 2)
        self.assertEqual(test_object.tipo, Motocicleta.Tipo.URBANA)
        self.assertEqual(test_object.cilindrada, CILINDRADA)
        self.assertEqual(test_object.velocidad, VELOCIDAD)

        self.assertRaises(AttributeError, lambda: Motocicleta(color=COLOR, velocidad=VELOCIDAD_INVALIDO, cilindrada=CILINDRADA, tipo=Motocicleta.Tipo.URBANA))
        self.assertRaises(AttributeError, lambda: Motocicleta(color=COLOR, velocidad=VELOCIDAD, cilindrada=CILINDRADA_INVALIDO, tipo=Motocicleta.Tipo.URBANA))
        self.assertRaises(AttributeError, lambda: Motocicleta(color=COLOR, velocidad=VELOCIDAD, cilindrada=CILINDRADA, tipo=TIPO_INVALIDO))


        self.assertRaises(AttributeError, lambda: Motocicleta(
            color=COLOR, 
            velocidad=VELOCIDAD, 
            cilindrada=CILINDRADA, 
            tipo=TIPO_INVALIDO)
        )

if __name__ == '__main__':
    unittest.main()