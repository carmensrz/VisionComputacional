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
