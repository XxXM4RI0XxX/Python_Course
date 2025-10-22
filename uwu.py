print('phyton')

# Linea de comentario

""" DOCUMENTATION
Nombre del programa
Que hace el programa (resumido en una linea corta)
Nombre del creador, y fecha
"""

asd ,dsa = "XD", 1

var = True

cali1 = 0
cal2 = 1
res = cali1 + cal2

# Por defecto, depues de cada print, el interprete aplica un salto de linea :o

if res >= 70:
    print("Pasao :D")
else:
    print("Pasao'nt :(")

for x in range(0,5):
    print(x)

for x in "Uwu's":
    print(x)

for x in [12,"123",'c',12.3]:
    print(x)

lista = [123]
lista.pop()
print(lista)

tupla = (1,"ola") #Este valor no se puede modificar de ninguna manera :o

# Tienda simple de articulos
list_1 = []
size = 0

while True:
    print("-------------------------\n")

    print("1) Agregar articulos\n2) Ticket\n3) Salir")

    opt = int(input("Elija opcion: "))
    print("-------------------------")

    if opt == 1:
        name = input("Nombre: ")
        price = float(input("Precio: "))
        list_1.append(name)
        list_1.append(price)
        size = size + 2
    elif opt == 2:
        art_name = input("Que articulo desea?: ")
        art_no = 0
        for x, item in enumerate(list_1):
            if item == art_name:
                art_no = x
                break
        price = list_1[art_no+1]
        quantity = int(input("Cuantos?: "))
        print("----------\nVenta ####\nArticulo: ",art_name,"\nCantidad: ",quantity,"\nTotal: ",quantity*price)
    else: break