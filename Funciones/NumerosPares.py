#‐*‐coding:utf‐8‐*‐
'''
Created on 16/11/2017
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario
Realizar una función para comprobar que un número es par
@author: Cristobal
'''

def imprimePares():
    numero1 = input("Introduce el primer numero: ")
    numero2 = input("Introduce el segundo numero: ")
    if(numero1 < numero2):
        for i in range(numero1, numero2+1):
            if(i%2 == 0):
                print i
    else:
         for i in range(numero2, numero1+1):
            if(i%2 == 0):
                print i
imprimePares()   