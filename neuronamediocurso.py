#!/usr/bin/python 
                                                                                                                                            
import random

x=[]
w=[] 	#pesos
wn=[] 	#pesos nuevos
wi=[]     	#pesos nuevos insertados
alpha = 0.05
umbral = 0.5
t = 0
p = 0
res = 0
res2 = 0
suma = 0
mult = 0
i = 1
countErr=0

def inicio():

    global n
    n = input("Dame el numero de entradas ")
    for i in range(n):
        x.insert(i,random.uniform(0,2))	#generar cadena de entradas binarias aleatorias 
        w.insert(i,random.uniform(-1.0,1.0))	#generar cadenas de pesos random

    x.append(-1)			#agregar al vector de entradas un -1 al final
    print '\nVector de elementos de entrada generado \n', x[:]
                                                                                                       
    w.append(umbral)			#agregar al vector de pesos el umbral al final
    print '\nVector de elementos de pesos generado \n', w[:]
    
    sumatoria()   			#brincar a la funcion sumatoria

    return n

def sumatoria():
    
    global suma
    suma=0
    res=0
    
    res = x[i] * w[i]			#sumatoria del producto de elementos de entrada por elmentos del peso
    suma = suma + res			#actualizar sumatoria
                                                                                                          
    #t = raw_input("\nSalida Esperada (0 o 1): ")	#pedir al usuario salida esperada
    t = random.randint(0,1)		#generar solucion esperada aleatoria entre 0 y 1
    #t = int(t)
    print '\nLa salida aleatoria deseada es \n', t
                                                                                                  
    print '\nLa sumatoria de productos de entradas por pesos es:', suma	#imprimir la sumatoria total del producto de entradas por pesos
    
    comparacion(t,n)			#brincar a la funcion comparacion
    
    return t

def comparacion(t,n):
    global countErr
    if(suma>=umbral):	#comparar suma con el umbral
        
        p=1		#suma mayor o igual a 1, salida obtenida = 1
        print '\nLa salida obtenida = 1'
    
    else:
                                                                   
        p=0		#de lo contrario, salida obtenida = 0 
        print '\nLa salida obtenida = 0'
        
    i=1
    if(t!=p):		#si la salida esperada difiere de la salida producida, se realiza un cambio en el vector de pesos

        countErr +=1         
        wn[:]=[]
        for i in range(n+1):
            mult = alpha*(t-p)*x[i]	#agregamos la tasa de aprendizaje alpha para modificar los pesos
            wi.insert(i,w[i] + mult)
            wn.insert(i,wi[i])		#agregamos a un vector nuevo los nuevos pesos
        wn.append(umbral)		#agregamos el umbral al final del vector de pesos nuevo
        w[:]=[]
        for i in range(n+1):
            w.insert(i,wn[i])
        
        print '\nVector de elementos de pesos nuevos generado es \n', wn[:]	#imprimimos el vector nuevo de pesos
        
        sumatoria()	#brincamos a la funcion sumatoria para volver a hacer calculas

        
    else:
        
        print 'La salida esperada fue diferente que la obtenida', countErr, 'veces'             

    return countErr, w[:]

def main():
    global x,n,w,wn,wi,umbral
    inicio()




main()    
