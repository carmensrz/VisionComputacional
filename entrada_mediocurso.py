#!/usr/bin/env python
 
#Importamos las librerias necesarias
import Image, sys

#Creamos un nuevo archivo para guardas los datos binarios 
f = open("huella1.txt", "w")

#Variables
x = 1
y = 1

#Abrimos la huella que ocupamos
im = Image.open("img1.png") 

#Hacemos un recorrido en largo y ancho de la imagen por pixeles
for y in range(0,209): #Largo
	for x in range(0,180): #Ancho
		pix = im.load()             
		pix[x, y]
                if pix[x,y] == (255,255,255):  #Si se encuentra un punto blanco se guarda 1
	       	        c= 1
		else:
			c= 0                   #Si no es blanco entonces se guarda 0
		f.write(str(c))            #Escribimos en el archivo
	f.write('\n')
f.close()					       #Cerramos el archivo

print "Huella grabada con exito"

