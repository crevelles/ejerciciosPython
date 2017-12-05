'''
Created on 23 nov. 2017

@author: cristobal
'''

opccion = 10;
alumnos = {};
notaOK = False;


print "Gestion de notas"
while(opccion!=0):
    print ""
    print "1 - anadir alumno"
    print "2 - eliminar alumno"
    print "3 - mostrar alumnos"
    print "4 - mostrar notas"
    print "5 - introducir notas"
    print "0 - SALIR" 
    opccion = input("Selecciona opcion: ")
    if(opccion == 1):
        print "Introducir alumno: "
        nombre = raw_input("nombre: ")
        alumnos[nombre]=-1
    elif(opccion == 2):
        print "Eliminacion de alumno" 
        nombre = raw_input("nombre:")  
        alumnos.pop(nombre)
    elif(opccion == 3):
        print "alumnos registrados"
        for x in alumnos:
            print "Alumno ", x
    elif(opccion == 4):
        print "Mostrar notas"
        for x in alumnos:
            if(alumnos[x] != -1):
                print "El alumno ", x, " tiene la nota: ", alumnos[x]
    elif(opccion == 5):
        print "Introducion de notas"
        nombre = raw_input("nombre:")
        nota = input("Introduce nota: ")
        alumnos[nombre] =  nota;
    elif(opccion == 0):
        print "Adios"    
   