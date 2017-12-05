#‐*‐coding:utf‐8‐*‐
'''
Created on 16/11/2017
Escribir un programa que tome una cantidad m de valores ingresados por el 
usuario, a cada uno le calcule el factorial e imprima el resultado junto con el 
número de orden correspondiente
Realizar una función para calcular el factorial
@author: Cristobal
'''

def factorial():
    cantidadNumeros = input("Introduce la cantidad de números: ")
    for i in range(cantidadNumeros):
        aux = 1
        numero = input("Introduce número: ")
        for x in range(numero, 0, -1):
            aux = aux * x
        print "Resultado ",i + 1    
        print aux   

factorial()        