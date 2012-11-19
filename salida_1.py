#!/usr/bin/env python
 
#Importamos las librerias necesarias
import Image, sys

#Variables
x = 1
y = 1
igual = 0
igual2 = 0
cadena = {}
cadena2 = {}

#Abrimos la huella que ocupamos que es la que ingresa la persona
im = Image.open("ingresa.png") 

#Hacemos un recorrido en largo y ancho de la imagen por pixeles
for y in range(0,400): #Largo
	for x in range(0,276): #Ancho
		pix = im.load()             
		pix[x, y]                          #Tomamos pixel por pixel de la imagen
                if pix[x,y] == (255,255,255):  #Si se encuentra un punto blanco se guarda 1
	       	        cadena[x,y] = 1
		else:
			cadena[x,y] = 0                               #Si no es blanco entonces se guarda 0
		
#Abrimos la huella que esta en nuestros archivos almacenados
im = Image.open("comprueba2.png") 

#Hacemos un recorrido en largo y ancho de la imagen por pixeles
for y in range(0,400): #Largo
	for x in range(0,276): #Ancho
		pix = im.load()                      #Tomamos pixel por pixel de la imagen
		pix[x, y]
                if pix[x,y] == (255,255,255):  #Si se encuentra un punto blanco se guarda 1
	       	        cadena2[x,y] = 1
		else:
			cadena2[x,y] = 0                               #Si no es blanco entonces se guarda 0
	
#Se crea una comprobacion entre la imagen recivida y la del registro	
for y in range(0,400):
	for x in range(0,276):
		if cadena[x,y] == cadena2[x,y]:
			igual = 1
		else:
			igual2 = 1

#Si son iguales el usuario accede al sistema y es identificado, de lo contrario se niega al acceso
if igual2 == 1:
	print "El usuario no esta identificado no puede acceder al sistema"
else:
	print "Si hay coincidencia, acceso al sistema"

