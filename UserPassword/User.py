'''
Created on 4 dic. 2017

@author: cristobal
'''
ok = True

while ok:
    usuario = raw_input("Introduce nombre de usuario: ")
    if(usuario.isalnum() == False):
        print "El usuario solo puede contener letras y numeros"
    elif(usuario.__len__() < 6):
        print "Longitud invalida, minimo 6 caracteres"
    elif(usuario.__len__() > 12):
        print "Maximo 12 caracteres"
    else:
        print "Usuario correcta"
        ok=False;        