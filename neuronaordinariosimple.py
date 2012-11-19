#!/usr/bin/python 
                                                                                                                                            
from random import *
from numpy import *
from numpy.random import *
from sys import argv


#Tasa de entrenamiento
alpha = 0.05

#Umbral agregado al final del vector de pesos
umbral = 0.5

#Clase de la neurona
class Neurona(object):
	
	#Constructor, genera el vector de pesos de tamanio n y agrega el umbral
	#al final para comparar con 0.

	def __init__(self, n):
    		self.w = uniform(low=-1, high=1, size=(1, n))
		self.w = append(self.w, umbral )
	
	#Funcion de activacion. 
	def activacion(self, x):
		x = append(x, -1)
		act = self.w * x
		act = act.sum()
		#print self.w
		if act > 0:
			return 1
		else:
			return 0

	#Funcion de aprendizaje 
	def aprendizaje(self, y, t, x):
		for i in range(self.w.size-1):
      			self.w[i] += alpha*(t - y)*x

#Numero de pruebas que queremos que haga la red
ITER = int(argv[1])

#Objeto de la neurona
neurona = Neurona(1)

#Contador veces que la neurona acerto
bien = 0
#Contador veces que la neurona fallo
mal = 0

#Contador que corre el numero de pruebas introducidas por el usuario
for i in range(ITER):
	y = ""
	t = 0
	#Obtener una muestra aleatoria (x), un numero entre 0 y 2
	muestra = uniform(0, 2)
	
	#Aqui se define lo que entrena la neurona
	#Si la muestra es mayor a 1, el valor esperado es 1
	if muestra > 1:
		t = 1
	
	#Si la muestra es menor a 1, el valor esperado es 0
	else:
		t = 0
	
	#Corremos la neurona con la muestra generada
	y = neurona.activacion(muestra)
	
	#Imprimimos lo obtenido
	print "Muestra: %s Salida de la Neurona: %s Salida Correcta: %s"%(muestra, y, t)
