#!/usr/bin/env python
# -*- coding: latin-1 -*-
from PIL import Image
from sys import argv
from math import floor
import math
import numpy 
import Image
import time

umbral = 100
n_img = argv[1]
img = Image.open('/home/carmensrz/'+ n_img)

matrix = []
comb = {}
angulos = []

#tamaño de la imagen
width, height = img.size

#funcion para realizar el efecto de escala de grises
def grayscale(img):
    imagen = img.convert("RGB")
    new_image = Image.new("RGB",(width,height))
    for i in range(width):
        for j in range(height):
            r,g,b = imagen.getpixel((i,j))
            average = int(floor((r+g+b)/3))
            #print r,g,b, average                                              
            new_image.putpixel((i,j),(average,average,average))
    return new_image

#funcion para filtro de convolucion, deteccion de bordes
def convolucion(new_image, h):
    pix = new_image.load()
    F = Image.new("RGB",(width,height))
    k = len(h[0]) 
    for x in range(width):
        for y in range(height):
            suma = 0
            for i in range(k):
                #centrar la mascara
                z1 = (i - (k/2))
                for j in range(k):
                    #centrar la mascara en la imagen
                    z2 = (j - (k/2))
                    #sin centrar z1=i z2=j
                    try:
                        suma += pix[x+z1,y+z2][0] * h[i][j]
                    except:
                        pass
            suma = int(floor(suma))
            F.putpixel((x,y),(suma,suma,suma))
    return F

def lines(img_gx, img_gy, imagen, umbral):					#Mascara vertical
    w,h = img_gx.size
    comb = {}
    for i in range(w):
        datos = []
        for j in range(h):
            #se saca el promedio de los pixeles
            pix_x = float(sum(img_gx.getpixel((i,j)))/3.0)
            pix_y = float(sum(img_gy.getpixel((i,j)))/3.0)
            #Si este promedio es mayor a 0 usamos la funcion arc para definir el angulo
            if abs(pix_x) > 0:
                angulo = math.atan(pix_y/pix_x)                
            #m_gx = img_gx.getpixel((i,j))[0]				
            #m_gy = img_gy.getpixel((i,j))[0]
            else:
                angulo = None
            if angulo is not None:
                angulo = int(math.degrees(angulo))
                #damos valor a rho con funciones de seno y coseno
                rho = int((j - h/2) * math.sin(angulo) + (w/2 - i) * math.cos(angulo))
                angulos.append(angulo)
                if i > 0 and i < w-1 and j > 0 and j < h - 1: 			
                    if (rho, angulo) in comb:					
                        comb[(rho, angulo)] += 1				
                    else:
                        comb[(rho, angulo)] = 1
                datos.append((rho, angulo))
            else:
                datos.append((None, None))
        matrix.append(datos)

    comb = sorted(comb.items(), key=lambda k: k[1], reverse = True)
    freq = {}
    n = int(math.ceil(len(comb) * umbral))

    for i in range(n):							       
        (rho, angulo) = comb[i][0]					       
        freq[(rho, angulo)] = comb[1]
    pixeles = imagen.load()

    for i in range(w):
        for j in range(h):						       
            if i > 0 and j > 0 and i < w and j < h:
                rho, angulo = matrix[i][j]
		print rho, angulo
                if (rho, angulo) in freq:
                    #dependiendo del angulo ponemos un color diferente, si es vertical, horizontar o diagonal
		    print angulo
                    if angulo == 0:
                        imagen.putpixel((i,j),(255,0,0))
                    elif angulo == 90:
                        imagen.putpixel((i,j),(0,255,0))
                    else:
                        imagen.putpixel((i,j),(0,0,255))

    return imagen

def b_w(imagen):
    new_image = Image.new("RGB",(width,height))
    for i in range(width):
        for j in range(height):
            r,g,b = imagen.getpixel((i,j))
            mayor = max(r,g,b)
            if(mayor<umbral):
                color = 0
            else: 
                color = 255
            new_image.putpixel((i,j),(color,color,color))

    #img.save('byn_'+imagen)
    return new_image
            
def normalizar(imagen):
    pix = imagen.load()
    imagen_norm = Image.new("RGB",(width,height))
    max = 0
    min = 0
    for i in range(width):
        for j in range(height):
            px = pix[i,j]
            mayor = max
            menor = min
            n_max = px[0]
            n_men = px[0]
            if n_max >= mayor:
                max = n_max
            if n_men <= menor:
                min = n_men

    print min, max
    prop = 256/(max-min)
    print prop
        
    for i in range(width):
        for j in range(height):
            r,g,b = imagen.getpixel((i,j))
            new_px = int(floor((g-min)*prop))
            imagen_norm.putpixel((i,j),(new_px,new_px,new_px))

    #img.save("norm_" + imagen)
    return imagen_norm

def bfs(img, origen, color):
    pixeles = img.load()
    
    #fila, columna = origen
   
    width, height = img.size
    
    cola = []
    cola.append(origen)
    original = pixeles[origen]
    m = []
    n=0
    while len(cola)>0:
        fila,columna = cola.pop(0)
        actual = pixeles[fila,columna]
        if actual == original or actual == color:
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    candidato = (fila + dy, columna + dx)
                    pixel_dy = candidato[0]
                    pixel_dx = candidato[1]
                    if pixel_dy >= 0 and pixel_dy < width and pixel_dx >= 0 and pixel_dx < height:
                        contenido = pixeles[pixel_dy,pixel_dx]
                        if contenido == original:
                            pixeles[pixel_dy,pixel_dx]=color
                            img.putpixel((pixel_dy,pixel_dx),color)
                            cola.append(candidato)
                            m.append((pixel_dy,pixel_dx))
                            n+=1
    return img


def main():
    start = time.time()
    binarizar = b_w(img)
    binarizar.save("Imagen1.jpg")

#    gx = [[-1,0,1],[-2,0,2],[-1,0,1]] #Sobel horizontal
#    gy = [[1,2,1],[0,0,0],[-1,-2,-1]] #Sobel vertical
    gy = [[-1,-1,-1],[2,2,2],[-1,-1,-1]] 
    gx = [[-1,2,-1],[-1,2,-1],[-1,2,-1]] 
    img_gx = convolucion(binarizar, gx)						
    img_gy = convolucion(binarizar, gy)	
    
    img_lineas = lines(img_gx, img_gy , binarizar, float(argv[2]))
    img_lineas.save("Lineas.png")

#    i_norm = normalizar(conv_gx)
#    i_norm.save("Imagen4.jpg")
    
#    imagen_f = b_w(conv_gx)
#    imagen_f.save("Imagen5.jpg")
    fin = time.time()
    tiempo = fin - start
    print "Tiempo total: "+ str(tiempo)
    
#    image_bfs = bfs(imagen_f,(200,150),(0,255,255))
#    image_bfs.save("bfs.jpg")

if __name__ == '__main__':
    main()
