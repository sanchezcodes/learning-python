from datetime import date
from enum import Enum
from random import randint


class Sexo(Enum):
    MASCULINO = 1
    FEMENINO = 2

class Carnet(Enum):
    A = 1
    A1 = 2
    A2 = 3
    B = 4
    B1 = 5
    C = 6
    C1 = 7
    D = 8
    D1 = 9
    E = 10


class Persona:
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.fecha_nacimiento = date.today()
        self.sexo = Sexo(randint(1, 2))
        self.dni = ""

    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellidos}"

    def edad(self) -> int:
        return date.today() - self.fecha_nacimiento

    def presentarme(self) -> str:
        return f"Hola, me llamo {self.nombre} y tengo {self.edad()} años"



class Alumno(Persona):
    def __init__(self):
        super().__init__()
        self.fecha_matriculacion = None
        self.carnets = []

    def matricularse(self, carnet:Carnet):
        self.carnets.append(carnet)
        self.fecha_matriculacion = date.today()

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.fecha_antiguedad = None
        self.cargo = None
        self.sueldo_base = 0


    def contratar(self, cargo:str, sueldo_base:int):
        self.cargo = cargo
        self.sueldo_base = sueldo_base
        self.fecha_antiguedad = date.today()

    def despedir(self):
        return "adeu"
        
