import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 3 numeros
2+4+6 = 12
"""

# start-->
def suma(num1, num2, num3):
    return num1+num2+num3

"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros impares del 1 al 1000
"""

# start-->
def sumaImpares():
    result = 0
    i = 0

    while i<=1000:
        if i%2!=0:
            result = result + i
        i +=1

    return result

"""
***************************************************************
@@ ejercicio 3 @@
encontrar el perimetro, area y el volumen de un esfera
radio = 12 m

perimetro: 2*pi*r
area: 4*pi*r^2
volumen: (4/3)*pi*r^3
"""

# start-->
def definicionEsfera():
    perimetro = obtenerPerimetro()
    area= obtenerArea()
    volumen= obtenerVolumen()
    esferaDict= {
        "perimetro": perimetro,
        "area": area,
        "volumen": volumen
    }
    return esferaDict

def obtenerPerimetro():
    radio = 12
    result = 0
    perimetro = 2*math.pi*radio
    return perimetro

def obtenerArea():
    radio = 12
    result = 0
    area=4*math.pi*(radio**2)
    return area

def obtenerVolumen():
    result = 0
    radio = 12
    volumen = (4/3)*math.pi*(radio**3)
    return volumen

"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Esfera:
    def definicionEsfera(self):
        perimetro = self.obtenerPerimetro()
        area= self.obtenerArea()
        volumen= self.obtenerVolumen()
        esferaDict= {
            "perimetro": perimetro,
            "area": area,
            "volumen": volumen
        }
        return esferaDict
    
    def obtenerPerimetro(self):
        radio = 12
        perimetro = 2*math.pi*radio
        return perimetro

    def obtenerArea(self):
        radio = 12
        area=4*math.pi*(radio**2)
        return area

    def obtenerVolumen(self):
        radio = 12
        volumen = (4/3)*math.pi*(radio**3)
        return volumen

"""
***************************************************************
@@ ejercicio 5 @@
Banco
Cliente
    nombre
    lugar
    numero de cuenta
    transaccion - retiro o abono
    monto
"""


class Banco:
    def procesar(self):
        return 0

    def abonosSanSalvador(self):
        return 0

    def abonosBalYRod(self):
        return 0


class Cliente:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/alexia-avelar/Alexia-Avelar_Parcial_ClaveB.git"