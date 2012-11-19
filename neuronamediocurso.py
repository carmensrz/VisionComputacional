#!/usr/bin/python 
                                                                                                                                            
import random

def main(): 	
                                                                                                                                     
    x=[] 	#entradas
                                                                                                                                           
    w=[] 	#pesos
                                                                                                                                               
    wn=[] 	#pesos nuevos

    wi=[]     	#pesos nuevos insertados
    

    alpha = 0.05
    umbral = 0.5
    t = 0	#salida esperada
    res = 0
    suma = 0
    mult = 0

    print "Ingresa 10 entradas decimales entre 0 y 1"

    for i in range(10):			#recibir entradas binarias de 10 elementos 
                                                                                                               
        x.insert(i, input())		#almacenar elementos de entrada tecleados por el usuario
                                                                                                                             
        w.insert(i,random.uniform(-1.0,1.0))	#generar pesos random
                                                                                                                     
        res = x[i] * w[i]		#sumatoria del producto de elementos de entrada por elmentos del peso

        suma = suma + res		#actualizar sumatoria

                                                                                                         
    x.append(-1)	#agregar al vector de entradas un -1 al final
    print '\nVector de elementos de entrada introducido \n', x[:]
                                                                                                        
    w.append(umbral)	#agregar al vector de pesos el umbral al final
    print '\nVector de elementos de pesos generado \n', w[:]

                                                                                                          
    t = raw_input("\nSalida Esperada (0 o 1): ")	#pedir al usuario salida esperada 
    t = int(t)
                                                                                                  
    print '\nLa sumatoria de productos de entradas por pesos es:', suma	#imprimir la sumatoria total del producto de entradas por pesos

                                                                                                                      
    if(suma>=umbral):	#comparar suma con el umbral
                                                                                   
        p=1		#suma mayor o igual a 1, salida obtenida = 1
        print '\nLa salida obtenida = 1'
   
    else:
                                                                              
        p=0		#de lo contrario, salida obtenida = 0 
        print '\nLa salida esperada = 0'

    
    if(t!=p):		#si la salida esperada difiere de la salida producida, se realiza un cambio en el vector de pesos
        for i in range(11):
            
            mult = alpha*(t-p)*x[i]	#agregamos la tasa de aprendizaje alpha para modificar los pesos 
            wi.insert(i,w[i] + mult)
            wn.insert(i,wi[i])		#agregamos a un vector nuevo los nuevos pesos
        
        print '\nVector de elementos de pesos nuevos generado es \n', wn[:]	#imprimimos el vector nuevo de pesos

main()
