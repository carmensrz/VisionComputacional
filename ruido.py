#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
from PIL import Image
from sys import argv
from math import floor
import numpy 
import Image
import time
import random

umbral = 80
n_img = argv[1]

img = Image.open('/home/carmensrz/'+ n_img)
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

def ruido(image):
    prob = 0.015
    sal_pim_img = Image.new("RGB",(width,height))
    for i in range(width):
        for j in range(height):
            r,g,b = image.getpixel((i,j))
            if random.random() < prob:
                sal_p = random.randint(0,1)
                if sal_p == 0:
                    sal_p = 0
                else:
                    sal_p = 255
                sal_pim_img.putpixel((i,j),(sal_p, sal_p, sal_p))
            else:
                sal_pim_img.putpixel((i,j),(r, g, b))
            
    return sal_pim_img

#def eliminar_ruido():
def eliminar_ruido(imagen):
    sinruido_img = Image.new("RGB",(width,height))
    vecinos = [] 
 #   num = 0
    for i in range(width):
        for j in range(height):
            color = imagen.getpixel((i,j))[0]
            #print color
            if (color == 255 or color == 0):
                    
                if(i==0):
                    vecino = imagen.getpixel((i+1,j))[0]
                    sinruido_img.putpixel((i,j),(vecino,vecino,vecino))
#                print vecino
                elif(j==0):
                    vecino = imagen.getpixel((i,j+1))[0]
                    sinruido_img.putpixel((i,j),(vecino,vecino,vecino))
#                print vecino
                elif(j==height):
                    vecino = imagen.getpixel((i-1,j))[0]
                    sinruido_img.putpixel((i,j),(vecino,vecino,vecino))
#                print vecino
                elif(i==width):
                    vecino = imagen.getpixel((i,j-1))[0]
                    sinruido_img.putpixel((i,j),(vecino,vecino,vecino))
#                print vecino
                else:            
                    try:
                        vecinos=[]
                #pixeles = list(img.getdata())
                        vecinos.append(imagen.getpixel((i,j-1))[0])
                        vecinos.append(imagen.getpixel((i,j+1))[0])
                        vecinos.append(imagen.getpixel((i-1,j))[0])
                        vecinos.append(imagen.getpixel((i+1,j))[0])
                        sort_vecinos = sorted(vecinos)
                    #print num, sort_vecinos
                    #print vecinos
                        num1,num2 = sort_vecinos[2:4]
                        print sort_vecinos[2:4]
                        mediana = int((num1+num2)/2)
                        sinruido_img.putpixel((i,j),(mediana,mediana,mediana))
                    except:
                        pass
            else:
                sinruido_img.putpixel((i,j),(color,color,color))
    return sinruido_img

def diferencia(grises, media):
    dif_img = Image.new("RGB",(width,height))
    for i in range(width):
        for j in range(height):
            diff = grises.getpixel((i,j))[0] - media.getpixel((i,j))[0]
            dif_img.putpixel((i,j),(diff,diff,diff))
#    nueva_img = b_w(dif_img)
            #print diff
    new_img = prom(dif_img)            
    nueva_imagen = normalizar(new_img)
    dif_new = b_w(nueva_imagen)
    return dif_img,dif_new
    


def prom(imagen):
    prom_img = Image.new("RGB",(width,height))
    pix = []
    vecinos = []
    for i in range(width):
        for j in range(height):
            pixeles = imagen.getpixel((i,j))[0]
            if j>0 and j<(height-1) and i>0 and i<(width-1):
                vecinos.append(imagen.getpixel((i,j-1))[0])
                vecinos.append(imagen.getpixel((i,j+1))[0])
                vecinos.append(imagen.getpixel((i-1,j))[0])
                vecinos.append(imagen.getpixel((i+1,j))[0])
            else:
                try:
                    vecinos.append(imagen.getpixel((i+1,j))[0])
                except:
                    pass
                try:
                    vecinos.append(imagen.getpixel((i,j+1))[0])
                except:
                    pass
                try:
                    vecinos.append(imagen.getpixel((i-1,j))[0])
                except: 
                    pass
                try:
                    vecinos.append(imagen.getpixel((i,j-1))[0])
                except:
                    pass
          
            
            vecinos.append(pixeles)
            promedio = (sum(vecinos)/len(vecinos))
            vecinos = []
            prom_img.putpixel((i,j),(promedio,promedio,promedio))
    return prom_img

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
    pix = []
    for i in range(width):
        for j in range(height):
            pix.append(imagen.getpixel((i,j))[0])
    mayor_px = max(pix)
    menor_px = min(pix)
    
    print mayor_px, menor_px

#    print 
    
    prop = 256.0/(mayor_px-menor_px)
            
    for i in range(width):
        for j in range(height):
            r,g,b = imagen.getpixel((i,j))
            new_px = int(floor((g-menor_px)*prop))
            imagen_norm.putpixel((i,j),(new_px,new_px,new_px))

    #img.save("norm_" + imagen)
    return imagen_norm

def main():

    start = time.time()
    grises = grayscale(img)
    grises.save("Imagen1.jpg")

    ruido_img = ruido(grises)
    ruido_img.save("SalPimienta.jpg")

    limpia_img = eliminar_ruido(ruido_img)
    limpia_img.save("SinSalPimienta.jpg")

    blur_img = prom(grises)
    blur_img.save("Promedio.jpg")

    norm_img = normalizar(grises)
    norm_img.save("Normalizada.jpg")

    dif_img, bordes_img  = diferencia(grises,blur_img)
    dif_img.save("Diferencia.jpg")
    bordes_img.save("Bordes.jpg")

if __name__ == '__main__':
    main()
