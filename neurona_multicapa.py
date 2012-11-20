#!/usr/bin/python 
# -*- coding: latin-1 -*-                                                    

import matplotlib
import matplotlib.pyplot as plt
from random import *
from numpy import *
from numpy.random import *
from sys import argv
import numpy as np
import pickle 

#Clase de la neurona
class Neurona(object):

	def __init__(self, ne, no, ns):
		#Nodos de la capa de entrada, oculta y salida
		self.ne = ne+1
		self.no = no
		self.ns = ns
		
		#Activaciones de los nodos, se crean arreglos para la activacion de 
		#los nodos de las capas de entrada, oculta y salida
		self.ae = ones((self.ne),float)
		self.ao = ones((self.no),float)
		self.ay = ones((self.ns),float)
	
		#Se generan las matrices de pesos aleatorios de entrada y de salida 
		#en un rango de -1.0 a 1.0
		self.we = uniform(-1.00, 1.00,(self.ne, self.no))
		self.ws = uniform(-1.00, 1.00,(self.no, self.ns))

		#Se generan matrices para tener el ultimo cambio en los pesos para 
		#el momentum el cual hace que la convergencia sea estable y mas rapida
		self.ce = zeros((self.ne, self.no), float)
		self.cs = zeros((self.no, self.ns), float)

	#Guardar los pesos en un archivo	
	def guardar(self, outfile):
		self.lw = [self.we,self.ws]
		pickle.dump(self.lw,open(outfile,'w'))
		#self.reset()
		
	#Cargar el archivo de pesos
	def cargar(self, outfile):
		self.lw = pickle.load(open(outfile,'r'))
		self.we=self.lw[0]
		self.ws=self.lw[1]

	#Funcion de sigmoidal. Esta funcion te devuelve el sigmoidal que es igual a la
	#tangente hiperbolica de s
	def sigmoidal(self, s):
		return np.tanh(s)

	#Funcion derivada sigmoida. La derivada de la sigmoidal esta dada por x(s)(1-x(s))
	def derivada_sigm(self, x):
		return 1.0-x**2

	#Funcion actualizar. Actualiza las activaciones de los nodos de salida, oculta y 
	#entrada
	def actualizar(self, entradas):
		#Activaciones de entradas
		self.ae[0:self.ne-1] = entradas

                #Activaciones ocultas. Hace la suma del producto de la matriz
		#transpuesta de pesos de entrada y la matriz de activacion de entrada,
		#la matriz de activacion de los nodos ocultos es igual la sigmoidal
		#de la suma anterior.
		sum = np.dot(np.transpose(self.we),self.ae) 
		self.ao = self.sigmoidal(sum)

                #Activaciones de salidas. Hace la suma del producto de la matriz
		#transpuesta de pesos de salida y la matriz de activacion de salida,
		#la matriz de activacion de la capa de salida es igual a la sigmoidal de
		#la suma anterior.	       
		sum = np.dot(np.transpose(self.ws),self.ao)
		self.ay = self.sigmoidal(sum)
		
#		print self.ay
		return self.ay
	
	def back_propagation(self,esperado, alpha, m):
		#Calcula terminos de error para la salida utilizando la regla delta
		#la cual se define por el producto de la derivada sigmoidal del arreglo
		#de activacion de salida y la diferencia del valor esperado menos
		#el vector de activacion de nodos ocultos
		delta_salida = self.derivada_sigm(self.ay) * (esperado-self.ao)

		#Calcular terminos de error para capa oculta. El error esta dado por
		#el producto de la matriz traspuesta de pesos de salida y la funcion
		#delta obtenida anteriormente. Y la funcion delta para esta capa
		#esta definida por la derivada sigmoidal de la activacion oculta por
		#el error obtenido.
#		print self.ws 
#		print delta_salida
		error = np.dot(np.transpose(self.ws),(delta_salida))
		delta_oculta = self.derivada_sigm(self.ao)*error

		#Actualiza pesos de salida utilizando la tasa de aprendizaje y el
		#momentum
		cambios = delta_salida * reshape(self.ao,(self.ao.shape[0],1))
		self.ws = self.ws + (alpha* cambios) + (m*self.cs)
		self.cs = cambios
		
		#Actualizar pesos de entrada
		cambios = delta_oculta * reshape(self.ae,(self.ae.shape[0],1))
		self.we = self.we + (alpha*cambios) + (m*self.ce)
		self.ce = cambios

		#Calcular los errores de salida utilizando metodo del gradiente
		errores = esperado-self.ay**2
		
		return(error/2).sum()

	#Realizar pruebas e imprimir
#	def pruebas(self, patron):
		#for i in range (patron.size):
		#	x = back_propagation(patron['input'][i])

		#	print i, '>>', self.actualizar(i)

	def entrenamiento_simple(self, entradas, esperado):
		self.actualizar(entradas)
		return self.back_propagation(esperado,0.5,0.1)

	#Funcion de entrenamiento. Toma como parametro los patrones, epoch (iterativo),
	#alpha que es la tasa de aprendizaje, m es el momentum
	def entrenamiento(self, patron, epoch=3000, alpha=0.1, m=0.1):
		for i in range(epoch):
			error = 0.0
			for p in patron:
				entradas = p[0]
				esperado = p[1]
				self.actualizar(entradas)
				error = error + self.back_propagation(esperado, alpha, m)
		for i in range(len(patron)):
			o = self.actualizar(patron['input'][i])
			print i, patron['input'][i], '%.2f' % o[0],
			print '(valor esperado %.2f)' % patron['output'][i]
			
		print 'Error', error


def main():


	#Definir un patron, de tamanio 4, con 2 entradas y 1 salida
	neurona = Neurona(2,2,1)
	print "Aprendiendo funcion logica OR"
	patron = np.zeros(4, dtype=[('input', float, 2), ('output', float, 1)])
	patron[0] = (0,0) , 0
	patron[1] = (1,0) , 1
	patron[2] = (0,1) , 1
	patron[3] = (1,1) , 0
	
#	patron = [
 #       [[0,0], [-1]],
  #      [[0,1], [1]],
   #     [[1,0], [1]],
    #    [[1,1], [-1]]
    #]
	#Crear una neurona con 2 nodos de entrada, dos ocultos y uno de salida

	#Entrenarla la neurona con patrones
	neurona.entrenamiento(patron,1000)
	#Probarla
#	neurona.pruebas(patron)
	neurona.guardar("weights.dat")
	del neurona
	neurona = Neurona(2,2,1)
	neurona.cargar("weights.dat")
#	neurona.pruebas(patron)
	del neurona
	neurona = Neurona(2,2,1)
	for i in xrange(1000):
		error=0.0
		for p in patron:
			entradas = p[0]
			esperado = p[1]
			error = error + neurona.entrenamiento_simple(entradas,esperado)
	print 'Error', error
#	neurona.pruebas(patron)
	neurona.guardar("weights.dat")
	del neurona
	neurona = Neurona(2,2,1)
	neurona.cargar("weights.dat")


	print "Aprendiendo funcion sen(x)"
	patron = np.zeros(500, dtype=[('x',  float, 1), ('y', float, 1)])
	patron['x'] = np.linspace(0,1,500)
	patron['y'] = np.sin(patron['x']*np.pi)
	
	for i in range(10000):
		n = np.random.randint(patron.size)
		neurona.actualizar(patron['x'][n])
		neurona.back_propagation(patron['y'][n],0.1,0.1)
		
		plt.figure(figsize=(10,5))
		#Dibujo de la funcion real de sen(x)
		x,y = patron['x'],patron['y']
		plt.plot(x,y,color='b',lw=1)
		#Dibujo de la funcion aproximada con la red neuronal
		for i in range(patron.shape[0]):
			y[i] = neurona.actualizar(x[i])
			plt.plot(x,y,color='r',lw=3)
			plt.axis([0,1,0,1])
			plt.show()
#	neurona.pruebas(patron)
	del neurona


if __name__ == '__main__':
	main()
