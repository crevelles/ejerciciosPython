'''
Created on 4 dic. 2017
Escribe un programa que muestre por pantalla los numeros multiplos de 7 entre 
el 1 y el 500. Utiliza range(501) en un bucle for con los if necesarios. Despues haz 
lo mismo empleando un range con tres parametros
@author: cristobal
'''

for i in range(501):
    if(i % 7 == 0):
        print i, " es multiplo de 7"
print "Otra forma con 3 parametros en el range"

for i in range(0,501,7):
    print i, " es multiplo de 7"