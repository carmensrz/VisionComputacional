#!/usr/bin/python 
                                                                                                                                          import random

<<<<<<< HEAD
=======
#!/usr/bin/python 
                                                                                                                                            
import random

>>>>>>> 92df799b1c1a96417544e30f8470d860951e5b0c
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
cont = 0
i = 1
<<<<<<< HEAD


def main(): 	
                                                                                                                                     
    global x,w,wn,wi,umbral

def inicio():

    for i in range(10):

        x.insert(i,random.uniform(0,1))	#generar cadena de entradas binarias aleatorias 
=======

def main(): 	
                                                                                                                                     
    global x,w,wn,wi,umbral

def inicio():
    
    global x

    for i in range(10):

        x.insert(i,random.uniform(0.0,1.0))	#generar cadena de entradas binarias aleatorias 
>>>>>>> 92df799b1c1a96417544e30f8470d860951e5b0c
                                                                                                                           
        w.insert(i,random.uniform(-1.0,1.0))	#generar cadenas de pesos random
                                                                                                                                                                                                                            
    x.append(-1)			#agregar al vector de entradas un -1 al final
<<<<<<< HEAD
    print '\nVector de elementos de entrada generado \n', x[:]
=======
    print '\nVector de elementos de entrada introducido \n', x[:]
>>>>>>> 92df799b1c1a96417544e30f8470d860951e5b0c
                                                                                                       
    w.append(umbral)			#agregar al vector de pesos el umbral al final
    print '\nVector de elementos de pesos generado \n', w[:]
    
    sumatoria()   			#brincar a la funcion sumatoria

def sumatoria():
<<<<<<< HEAD
    
=======
    global x
>>>>>>> 92df799b1c1a96417544e30f8470d860951e5b0c
    global suma
    suma=0
    res=0
    
    res = x[i] * w[i]			#sumatoria del producto de elementos de entrada por elmentos del peso
                                                                                                        
    suma = suma + res			#actualizar sumatoria
                                                                                                          
<<<<<<< HEAD
    #t = raw_input("\nSalida Esperada (0 o 1): ")	#pedir al usuario salida esperada
    t = random.randint(0,1)		#generar solucion esperada aleatoria entre 0 y 1
    #t = int(t)
    print '\nLa salida aleatoria deseada es ', t
                                                                                                  
    print '\nLa sumatoria de productos de entradas por pesos es:', suma	#imprimir la sumatoria total del producto de entradas por pesos
    print '\nEl umbral es igual a: ', umbral
=======
    t = raw_input("\nSalida Esperada (0 o 1): ")	#pedir al usuario salida esperada
    t = int(t)
                                                                                                  
    print '\nLa sumatoria de productos de entradas por pesos es:', suma	#imprimir la sumatoria total del producto de entradas por pesos
>>>>>>> 92df799b1c1a96417544e30f8470d860951e5b0c
    
    comparacion(t)			#brincar a la funcion comparacion
    
    return t

def comparacion(t):
    
    global cont
                                                                                                                       
    if(suma>=umbral):	#comparar suma con el umbral
                                                                                    
        p=1		#suma mayor o igual a 1, salida obtenida = 1
        print '\nLa salida obtenida = 1'
    
    else:
                                                                   
        p=0		#de lo contrario, salida obtenida = 0 
        print '\nLa salida obtenida = 0'

    
    
    i=1
    if(t!=p):		#si la salida esperada difiere de la salida producida, se realiza un cambio en el vector de pesos
        wn[:]=[]

        for i in range(11):
            
            mult = alpha*(t-p)*x[i]	#agregamos la tasa de aprendizaje alpha para modificar los pesos
            wi.insert(i,w[i] + mult)
            wn.insert(i,wi[i])		#agregamos a un vector nuevo los nuevos pesos
        wn.append(umbral)		#agregamos el umbral al final del vector de pesos nuevo
        w[:]=[]
        for i in range(11):
            w.insert(i,wn[i])
         
        print '\nVector de elementos de pesos nuevos generado es \n', wn[:]	#imprimimos el vector nuevo de pesos
        sumatoria()	#brincamos a la funcion sumatoria para volver a hacer calculas
         
    return w[:]
        
      
<<<<<<< HEAD
def main():
    #for n in range (10):        
    	inicio()	
=======
def main():        
    inicio()	

main()    
>>>>>>> 92df799b1c1a96417544e30f8470d860951e5b0c

