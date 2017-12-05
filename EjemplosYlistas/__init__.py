#‐*‐coding:utf‐8‐*‐
precio = 5785
descuento = 38

descuentoBicileta = (precio * descuento) / 100

precioBiciclesConDescuento = precio - descuentoBicileta

print "El Precio de la bicilceta es", precioBiciclesConDescuento
print '--------------------------------'
print 'tupla:'
mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)
print mi_tupla [2]
print mi_tupla [0:3]
print mi_tupla [-1]

mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
print '---------------------------------'
print 'lista:'
print mi_lista [0:3]
print mi_lista [-1]
print mi_lista [2]
mi_lista[2] = 3.8
print mi_lista [2]

print '--------------------------------------'
print 'diccionario:'
mi_diccionariio =  {'clave_1' : 'valor_1', 'clave_2' : 'valor_2', 'clave_3' : 'valor_3'}
print mi_diccionariio ['clave_2']
del(mi_diccionariio['clave_2']) #elimina una entrada en el diccionario.
print mi_diccionariio['clave_1']
mi_diccionariio['clave_1'] = 'Nuevo Valor'
print mi_diccionariio['clave_1']
mi_diccionariio['clave_4'] = 'Pepe'
print mi_diccionariio['clave_4']

print '---------------------------------------'
semaforo = 'verde'

if semaforo == 'verde':
    print "Cruzar la calle"
else:
    print 'Esperar'

compra = 150

if compra <= 100:
    print "Pago en efectivo"
elif compra> 100 and compra< 300:
    print "Pago con tarjeta de débito"
else:
    print "Pago con tarjeta de crédito"
print '---------------------------------'
i=1
while i <= 3:
    print i
    i += 1
print 'Programa terminado'

print '---------------------------------'
print "Comienzo"
for i in [3, 4, 5]:
    print "Hola. Ahora i vale " + str(i) + " y su cuadrado " + str(i ** 2)
print "Final"

print '----------------------------------'
mi_lista = ['Juan', 'Antonio', 'Pedro', 'Luis']
for nombre in mi_lista:
    print nombre
for i in "AMIGO":
    print i
print "¡AMIGO!"
for i in range(1, 10):
    print i*5

print '------------------------------------'
for i in range(2, 11, 2):
    print i
print '------------------------------------'
for i in range(2, 11, 3):
    print i
print '------------------------------------'
for i in range(10, 4, -1):
    print i
print '------------------------------------'
for i in range(3, -1, -1):
    print i
print '------------------------------------'
t = 1
for i in range(1, 21, 1):
    t = i * t
    print t
