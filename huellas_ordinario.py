#!/usr/bin/env python

c1 = open("Comp1.txt", "r")
c2 = open("Comp2.txt", "r")
archivoUno = c1.readlines()
archivoDos = c2.readlines()
c1.close()
c2.close()
result = open("resultado.txt", "w")

x = 0
for i in archivoUno:
   if i != archivoDos[x]:
      result.write(i+"El otro archivo contiene >> "+archivoDos[x])
   x += 1

	
result.close()