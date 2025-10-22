"""
NOTACION DE CORTE DE PYTHON

Cuando se tiene un arreglo de datos, se puede utilizar la notacion de corte al momento de obtener los datos de ese arreglo.
Su sintaxis es: arreglo[inicio:final]; donde inicio y final son valores enteros
- inicio: Indice donde se inicia la obtencion de datos del arreglo
- final: Indice donde se deja de obtener datos (se detiene en el indice final-1)
Se puede dejar tanto el inicio como final vacios
- [inicio:] Regresa todos los valores desde 'inicio' hasta donde termine el arreglo
- [:final] Regresa todos los valores desde el comienzo del arreglo hasta 'final'
- [:] Regresa TODOS los valores del arreglo
"""

arr = [0,1,2,3,4,5]
print("Arreglo:",arr[:])
print("Arreglo cortado:",arr[1:3])
# Al igual, se pueden modificar valores dentro del arreglo en un rango definido
arr[1:3] = ['x','y']
print("Arreglo modificado con corte:",arr,"\n")

# Esta notacion tambien puede ser usada para asignar valores a otro arreglo
arr2 = arr[1:3]
print("Segundo arreglo:",arr2)