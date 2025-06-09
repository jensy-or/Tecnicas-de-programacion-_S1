from abc import ABC, abstractmethod

## ABSTRACCIÓN - Clase abstracta que define el concepto general de insecto
class Insecto(ABC):
    def __init__(self, nombre, patas):
        # ENCAPSULACIÓN - Atributos protegidos
        self._nombre = nombre
        self._patas = patas
        self._esta_vivo = True
    
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def alimentarse(self):
        pass
    
    # Método concreto que comparten todos los insectos
    def describir(self):
        return f"Soy un {self._nombre} con {self._patas} patas."
    
    # ENCAPSULACIÓN - Getter y setter para atributo protegido
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre

## HERENCIA - Clase base para insectos voladores
class InsectoVolador(Insecto):
    def __init__(self, nombre, patas, num_alas):
        super().__init__(nombre, patas)
        self.__num_alas = num_alas  # ENCAPSULACIÓN - Atributo privado
    
    # POLIMORFISMO - Implementación específica del método mover
    def mover(self):
        return f"{self._nombre} está volando con sus {self.__num_alas} alas."
    
    # Método específico de insectos voladores
    def aterrizar(self):
        return f"{self._nombre} ha aterrizado suavemente."

## HERENCIA - Clase concreta para mariposas
class Mariposa(InsectoVolador):
    def __init__(self, nombre, color_alas):
        super().__init__(nombre, 6, 4)  # Todas las mariposas tienen 6 patas y 4 alas
        self.color_alas = color_alas
    
    # POLIMORFISMO - Implementación específica del método alimentarse
    def alimentarse(self):
        return f"{self._nombre} se alimenta de néctar con su espiritrompa."
    
    def describir(self):  # Sobrescritura de método
        return f"{super().describir()} Mis alas son de color {self.color_alas}."

## HERENCIA - Clase para insectos no voladores
class InsectoNoVolador(Insecto):
    def __init__(self, nombre, patas):
        super().__init__(nombre, patas)
    
    # POLIMORFISMO - Implementación específica del método mover
    def mover(self):
        return f"{self._nombre} está caminando con sus {self._patas} patas."

## HERENCIA - Clase concreta para hormigas
class Hormiga(InsectoNoVolador):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, 6)  # Todas las hormigas tienen 6 patas
        self.__tipo = tipo  # ENCAPSULACIÓN - Atributo privado
    
    # POLIMORFISMO - Implementación específica del método alimentarse
    def alimentarse(self):
        return f"{self._nombre} (hormiga {self.__tipo}) recolecta comida para la colonia."
    
    # Método específico de hormigas
    def trabajar(self):
        return f"{self._nombre} está trabajando duramente como {self.__tipo}."
    
    # ENCAPSULACIÓN - Getter para atributo privado
    @property
    def tipo(self):
        return self.__tipo

# Función que demuestra POLIMORFISMO
def accion_insecto(insecto):
    print(insecto.describir())
    print(insecto.mover())
    print(insecto.alimentarse())
    if isinstance(insecto, Hormiga):
        print(insecto.trabajar())
    if isinstance(insecto, InsectoVolador):
        print(insecto.aterrizar())
    print("------")

# Demostración
if __name__ == "__main__":
    # Crear instancias
    monarca = Mariposa("Mariposa Monarca", "naranja y negro")
    reina = Hormiga("Hormiga Reina", "reina")
    saltamontes = InsectoVolador("Saltamontes", 6, 4)
    
    # Usar métodos específicos
    monarca.nombre = "Mariposa Monarca Real"  # Usando setter
    
    # Demostración de POLIMORFISMO
    print("=== COMPORTAMIENTO DE DIFERENTES INSECTOS ===")
    for insecto in [monarca, reina, saltamontes]:
        accion_insecto(insecto)
    
    # ENCAPSULACIÓN - Intentar acceder a atributo privado
    try:
        print(reina.__tipo)  # Esto fallará
    except AttributeError as e:
        print(f"\nError de encapsulación: {e}")
        print(f"Acceso correcto mediante getter: {reina.tipo}")