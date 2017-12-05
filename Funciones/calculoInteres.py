#‐*‐coding:utf‐8‐*‐
'''
Created on 16/11/2017
Escribir un programa que le pregunte al usuario una cantidad de dinero, 
una tasa de interés y un número de años y muestre como resultado el monto final a 
obtener. La fórmula a utilizar es: Cn = C * (1 + x/100) ^ n
Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular

@author: Cristobal
'''





def calculoInteres():
    capitalInicial = input("Ingresa la cantidad de dinero: \n")
    tasa = input("Ingresa la tasa de interés: \n")
    anyos = input("Ingresa numero de años: \n")
    calculo = capitalInicial *(1 + tasa/100.0)**anyos
    return calculo;

total = calculoInteres()
print total