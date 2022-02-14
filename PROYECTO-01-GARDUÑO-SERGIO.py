"""
Se importan las los archivos desde el archivo lifestore_file para tener las siguientes listas

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from copy import deepcopy

#Variable acceso para determinar el estado del login, F = no acceso T = acceso. Intentos es para contar el numero de intenos para acceder, el maximo sera de 3 intentos
acceso = False
intentos = 0
#Mensaje bienvenida
print("Hola bienvenido\nIngresa tus credenciales para acceder")

#while loop para hacer login
#not acceso cambia el estado a true hasta hacer el login correcto
while not acceso:
  usuario = input('Usuario: ')
  contras = input('Contraseña del usuario: ')
  
  if (contras != 'admin') or (usuario != 'admin'):
    intentos += 1
    restantes = 3 - intentos
    print(f'Credenciales incorrectas\nTienes "{restantes}" intentos restantes' ) 
    if restantes == 0:
      print('Error, intentos excedidos')
      exit()
  else:
    acceso = True
    
  

#Se personalizara la lista products para incluir informacion de las ventas como de las busquedas

lista_vgeneral = []
lista_vgeneral = deepcopy(lifestore_products)

#Se elimina en la nueva lista informacion como el precio y el stock del producto
for elemento in lista_vgeneral:
    elemento.pop(4)
    elemento.pop(2)

#Se agregan dos nuevas columnas para empezar a sumar las ventas como las busquedas. La lista_vgeneral = [id_product, name, category, sales, searches]
for x in lista_vgeneral:
    x.append(0)
    x.append(0)

#Se revisa cada elemento de la lista general creada contra la lista de ventas para acumular las ventas de cada producto si su id registrado en las ventas es el mismo y el producto no fue devuelto
for elemento in lista_vgeneral:
    for product in lifestore_sales:
        if product[1] == elemento[0] and product[4] == 0:
            elemento[3] += 1

#Se realiza la misma comparacion pero ahora con las busquedas y se agrega al indice de la lista de cada producto dentro del indice 4
for elemento in lista_vgeneral:
    for search in lifestore_searches:
        if search[1] == elemento[0]:
            elemento[4] += 1


#Definicion de funciones que nos permitiran acceder al elemento de cada producto para obtener las ventas o las busquedas. Todo esto para utilizar el metodo .sort de python
def sales(elemento):
    return elemento[3]


def search(elemento):
    return elemento[4]


#Se realiza una copia de la lista general por medio de slicing, y despues se utiliza el metodo sort para ordernar las listas de mayor a menor utilizando las funciones antes mencionadas.

lista_topsales = lista_vgeneral[:]
lista_topsales.sort(reverse=True, key=sales)

lista_topsearches = lista_vgeneral[:]
lista_topsearches.sort(reverse=True, key=search)

#Impresion de los 5 elementos mas vendidos, como de los 5 elementos mas buscados
print('Top 5 productos mas vendidos: \n')

for x in range(5):
    print(lista_topsales[x], '\t')

print('\nTop 5 productos mas buscados: \n')

for x in range(5):
    print(lista_topsearches[x], '\t')

#Se procedera ahora a hacerlo por categoria
#Se copian los elementos de las categorias de todos los productos por listas por compresion. Los elementos repetidos se eliminan al ponerse como llaves de un diccionario, una vez teniendo todas las diferentes categorias, se regresan a una lista.

categorias = [elemento[2] for elemento in lista_vgeneral]
categorias = list(dict.fromkeys(categorias))

print("\n", categorias, "\n")

procesadores = []
discosduros = []
tarjetamadre = []
tarjetavideo = []
bocinas = []
audifonos = []
pantallas = []
usb = []


#Se añade los productos a una lista determinada de su categoria
for producto in lista_vgeneral:
    if categorias[0] in producto:
        procesadores.append(producto)
    elif categorias[1] in producto:
        tarjetavideo.append(producto)
    elif categorias[2] in producto:
        tarjetamadre.append(producto)
    elif categorias[3] in producto:
        discosduros.append(producto)
    elif categorias[4] in producto:
        usb.append(producto)
    elif categorias[5] in producto:
        pantallas.append(producto)
    elif categorias[6] in producto:
        bocinas.append(producto)
    elif categorias[7] in producto:
        audifonos.append(producto)

#Funcion que recibe una lista para ordenarla en determinada manera e imprime de cierta manera los mensajes recien ordenados
def imprimir_sort(lista, mensaje, veces, posicion_lista, key, reverse):
    lista.sort(key=key, reverse=reverse)
    print(mensaje + " :")
    for x in range(veces):
        print(
            f"iD: {lista[x][0]} Name: {lista[x][1]}   Number : {lista[x][posicion_lista]}"
        )
    print("\n")

#Se hace uso de la funcion para ordenar e imprimir los productos menos vendidos por categoria
#Cabe mencionar que para la cateogria 'memorias usb' unicamente hay 2 productos
print('\nLos productos por categoria menos vendidos son:\n')

imprimir_sort(procesadores, categorias[0], 5, 3, sales, False)
imprimir_sort(tarjetavideo, categorias[1], 5, 3, sales, False)
imprimir_sort(tarjetamadre, categorias[2], 5, 3, sales, False)
imprimir_sort(discosduros, categorias[3], 5, 3, sales, False)
imprimir_sort(usb, categorias[4], 2, 3, sales, False)
imprimir_sort(pantallas, categorias[5], 5, 3, sales, False)
imprimir_sort(bocinas, categorias[6], 5, 3, sales, False)
imprimir_sort(audifonos, categorias[7], 5, 3, sales, False)

#Articulos menos buscados haciendo uso de la funcion que ordena e imprime
print("\nLos 10 articulos menos buscados por categoria son: \n")

imprimir_sort(procesadores, categorias[0], 9, 4, search, False)
imprimir_sort(tarjetavideo, categorias[1], 10, 4, search, False)
imprimir_sort(tarjetamadre, categorias[2], 10, 4, search, False)
imprimir_sort(discosduros, categorias[3], 10, 4, search, False)
imprimir_sort(usb, categorias[4], 2, 4, search, False)
imprimir_sort(pantallas, categorias[5], 10, 4, search, False)
imprimir_sort(bocinas, categorias[6], 10, 4, search, False)
imprimir_sort(audifonos, categorias[7], 10, 4, search, False)








#Empezar a segmentar por las reseñas obtenidos
resenas = lista_vgeneral[:]
#Lista resenas = [id_product, Product_name, sales, promedio_resena]
for product in resenas:
    contador = 0
    suma_r = 0
    product.pop(2)
    product.pop()

    #Si la venta coincide con el id de un producto especifico en resenas y este no fue devuelto, se suma a la variable suma_r y el contador que indicara el numero de ventas suma 1.
    for sale in lifestore_sales:
        if sale[1] == product[0] and sale[2] != 0:
            suma_r += sale[2]
            contador += 1
    #Si hubo ventas, calcular el promedio y agregarlo al producto en resenas. Sino, agregar un 0 en resenas
    if contador >= 1:
        promedio = round(suma_r / contador,2)
        product.append(promedio)
    else:
        product.append(0)

#Se hacen 2 listas, una que imprima las mejores reseñas y otro las peores
r_top = []
r_bottom = []

#Hubieron muchos productos con 5.0 de promedio en reseñas, mas de los 10 requeridos, por lo que la lista r_top solo contendra estos productos
for resena in resenas:
    if resena[-1] == 5:
        r_top.append(resena)
#Ordena e imprime la lista con la funcion imprimir_sort
imprimir_sort(r_top, "Los top 10 productos con mejores reseñas: ", 10, 3, lambda e: e[2], True)

#Si tuvieron resenas y las restantes menores a 5.0 de promedio, las agrega a la lista r_bottom
for resena in resenas:
    if resena[-1] > 0 and resena[-1] < 5:
        r_bottom.append(resena)
#Ordena e imprime la lista con la funcion imprimir_sort
imprimir_sort(r_bottom, "Los 10 productos con peores reseñas: ", 10, 3, lambda e: e[3], False)





#Se hace una lista id_no_refund = [id_sale, id_product, fecha] si el producto no es devuelto
id_no_refund = [[sale[0], sale[1], sale[3]] for sale in lifestore_sales if sale[4] == 0]

categoria_meses = {}
for sale in id_no_refund:
    id = sale[0]
    _, mes, _ = sale[2].split('/')
    #Despues de obtener el id y el mes de la venta, se añade como llave el mes si no ha sido registrado antes. Despues se anexa el id como value a la llave con el mes correspondiente
    if mes not in categoria_meses.keys():
        categoria_meses[mes] = []
    categoria_meses[mes].append(id)


#Se hace una lista resumen_meses donde se tiene una lista anidada con el valor del mes transformado a entero
resumen_meses = []
for x in list(categoria_meses.keys()):
  resumen_meses.append([int(x)])

#Contador servira para acudir a cada mes de la lista resumen_meses a continuacion
contador = 0
#Por cada llave, se revisa la lista de sus valores para obtener de ahi el id_product y consultar su precio en la lista lifestore_product para sumarlo en la variable suma_ventas
for key in categoria_meses.keys():
    suma_ventas = 0
    for id_venta in categoria_meses[key]:
        indice = id_venta - 1
        info_venta = lifestore_sales[indice]
        id_product = info_venta[1]
        precio = lifestore_products[id_product - 1][2]
        suma_ventas += precio
    #Se obtienen el numero total de ventas al mes con la longitud de la lista de los valores del diccionario, se calcula el promedio por ticket de compra al mes. Se añaden a la lista resumen_meses a su correspondiente mes esta informacion junto con la suma de los ingresos mensuales
    num_ventas = len(categoria_meses[key])
    promedio = round(suma_ventas/num_ventas,2)
    resumen_meses[contador].append(num_ventas)
    resumen_meses[contador].append(suma_ventas)
    resumen_meses[contador].append(promedio)
    contador += 1

#Se ordena la lista resumen_meses conforme el mes y se imprime
resumen_meses.sort(key = lambda e:e[0], reverse = False)
print('Los ingresos acumuladas por mes y el ticket promedio mensual\n')
for mes in resumen_meses:
  print(f"Num Mes: {mes[0]}   Ventas: {mes[2]}   Ticket promedio: {mes[3]}")

#Se ordena nuevamente la lista resumen_meses conforme al numero de ventas por mes y se imprime
print("\nLa informacion con los meses con mayores ventas son: \n")
resumen_meses.sort(key = lambda e:e[2], reverse = True)
for mes in resumen_meses:
  print(f"Num Mes: {mes[0]}   Ventas: {mes[2]}   Num ventas: {mes[1]}")
