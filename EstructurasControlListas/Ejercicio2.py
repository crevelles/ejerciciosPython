'''
Created on 4 dic. 2017
 Escribe  un programa en Python que cree una lista con los cuadrados de todos 
los numeros enteros del 0 al 10
@author: cristobal
'''

lista = []
for i in range(0,11):
    aux = i * i 
    print i,"elevado al cuadrado es", aux
    print ""
    lista.append(aux)
