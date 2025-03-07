#creando una clase

class Cultivo:

#atributos de clase
    familia= "FABACEAE"

#atributos de  instancia
    def __init__ (self, cultivo, especie, duracion):
        self.cultivo = cultivo
        self.especie = especie
        self.duracion = duracion
#metodos
    def tipo_de_siembra (self):
        print ("Instalacion 3x3 colgado a una distacia de 40cm")
    def tiempo_de_siembra (self):
        print ("inicios de marzo o inicios de las lluvias ")
# Creando un objeeto para la clase cultivo

Habichuela = Cultivo("Habichuela", "Phaseolus vulgaris", "90 dias")
#impirmiendo infomracion del cultivo
print(Habichuela.cultivo)
print (Habichuela.familia)
#LLamando metodos 
Habichuela.tipo_de_siembra ()
Habichuela.tiempo_de_siembra ()