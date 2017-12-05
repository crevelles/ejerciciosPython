'''
Created on 4 dic. 2017

@author: cristobal
'''

seguir = True
while seguir:    
    mayus = False
    minus = False
    espacio = True
    alfanum = False
    signos = False
    longitud = False    
    password = raw_input("Intro cadena: \n")
    if(password.__len__() >= 8):
        longitud = True
    for letra in password:
        if (letra.isspace()):
            espacio = False
        if (letra.isupper()):
            mayus = True
        if (letra.islower()):
            minus = True
        if (letra.isalnum()):
            alfanum = True
        if (letra.isalnum() ==  False):
            signos = True
    if(espacio and mayus and minus and alfanum and signos and longitud):
        seguir = False
        print "Contrasena valida"
    else:
        print "La contrasena no es segura"  
