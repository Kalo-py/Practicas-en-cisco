#Vamos a acceder a la función funI() del módulo iota del paquete extra. Nos obliga a usar nombres de paquetes calificados (asocia esto al nombramiento de carpetas y subcarpetas).

from sys import path

path.append('C:\\Users\\Carlos\\Documents\\programacion\\python\\cursos de cisco\\usando modulos invocando otros programas\\multiples import en uno solo')

from extra.iota import funI

print(funI())
#La siguiente variante también es válida:
#from sys import path
#path.append('..\\packages')
#from extra.iota import funI
#print(funI())

#Ahora vamos hasta el final del árbol: así es como se obtiene acceso a los módulos sigma y tau.
import extra.good.best.sigma
from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())
#Puedes hacer tu vida más fácil usando un alias:
import extra.good.alpha as alp
print(alp.funA())
