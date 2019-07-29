from enum import Enum

class Vehiculo(object):
    def __init__(self, color, ruedas):
        if not isinstance(ruedas, int):
            raise AttributeError('La cantidad de ruedas {ruedas} no es un entero valido.'.format(ruedas=ruedas))

        self.color = color
        self.ruedas = ruedas

    @classmethod
    def catalogar_1(cls, vehiculos):
        for vehiculo in vehiculos:
            print(vehiculo.__class__.__name__)

            for key, value in vehiculo.__dict__.items():
                print("\t" + key + ": " + str(value)) 

    @classmethod
    def catalogar_2(cls, vehiculos, ruedas=None):
        vehiculos_filtrados = []

        if ruedas is None:
            vehiculos_filtrados = vehiculos
        else:
            vehiculos_filtrados = [vehiculo for vehiculo in vehiculos if vehiculo.ruedas == ruedas]

            print("Se han encontrado {count} vehículos con {ruedas} ruedas.\n".format(count=len(vehiculos_filtrados), ruedas=ruedas))

        Vehiculo.catalogar_1(vehiculos_filtrados)

class Coche(Vehiculo):
    def __init__(self, color, velocidad, cilindrada):
        # Asumimos que todos los descendientes de coches tienen 4 ruedas
        super(Coche, self).__init__(color=color, ruedas=4)

        # Asumiendo que la velocidad y cilindrada son numeros enteros.
        if not isinstance(velocidad, int):
            raise AttributeError('La velocidad {velocidad} no es un entero valido.'.format(velocidad=velocidad))

        if not isinstance(cilindrada, int):
            raise AttributeError('La cilindrada {cilindrada} no es un entero valido.'.format(cilindrada=cilindrada))

        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Camioneta(Coche):
    def __init__(self, color, velocidad, cilindrada, carga):
        super(Camioneta, self).__init__(
            color=color,
            velocidad=velocidad,
            cilindrada=cilindrada,
        )

        if not isinstance(carga, int):
            raise AttributeError('La carga {carga} no es un entero valido.'.format(carga=carga))

        self.carga = carga

class Bicicleta(Vehiculo):
    Tipo = Enum('Tipo', "URBANA DEPORTIVA")

    def __init__(self, color, tipo):
        # Asumimos que todos los descendientes de bicicleta tienen 2 ruedas
        super(Bicicleta, self).__init__(color=color, ruedas=2)

        if tipo not in Bicicleta.Tipo:
            raise AttributeError('El tipo de bicicleta no valido {tipo} no es valido.'.format(tipo=tipo))
        
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, color, velocidad, cilindrada, tipo):
        super(Motocicleta, self).__init__(color=color, tipo=tipo)

        # Asumiendo que la velocidad y cilindrada son numeros enteros.
        if not isinstance(velocidad, int):
            raise AttributeError('La velocidad {velocidad} no es un entero valido.'.format(velocidad=velocidad))

        if not isinstance(cilindrada, int):
            raise AttributeError('La cilindrada {cilindrada} no es un entero valido.'.format(cilindrada=cilindrada))

        self.velocidad = velocidad
        self.cilindrada = cilindrada

if __name__ == '__main__':
    vehiculo_1 = Vehiculo(color='rojo', ruedas=3)
    coche_1 = Coche(color='rojo', velocidad=160, cilindrada=1330)
    camioneta_1 = Camioneta(color='rojo', velocidad=160, cilindrada=1330, carga=2500)
    bicicleta_1 = Bicicleta(color='rojo', tipo=Bicicleta.Tipo.URBANA)
    motocicleta_1 = Motocicleta(color='rojo', tipo=Motocicleta.Tipo.URBANA, velocidad=180, cilindrada=330)

    vehiculos = [vehiculo_1, coche_1, camioneta_1, bicicleta_1, motocicleta_1]
    
    print("Prueba catalogar_1:\n")

    Vehiculo.catalogar_1(vehiculos=vehiculos)

    print("Prueba catalogar_2 sin argumento de ruedas:\n")

    Vehiculo.catalogar_2(vehiculos=vehiculos)

    print("Prueba catalogar_2 con argumentos de ruedas(0,2,4):\n")

    for valor_ruedas in (0,2,4):
        Vehiculo.catalogar_2(vehiculos=vehiculos, ruedas=valor_ruedas)
