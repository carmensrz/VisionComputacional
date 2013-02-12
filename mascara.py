from PIL import Image
from sys import argv
from math import floor
import numpy 
import Image
import time

umbral = 100
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

def main():
    start = time.time()
    grises = grayscale(img)
    grises.save("Imagen1.jpg")
    #Aplicar mascara 
    sx = [[-1,0,1],[-2,0,2],[-1,0,1]] #Sobel horizontal
    sy = [[1,2,1],[0,0,0],[-1,-2,-1]] #Sobel vertical
    #h = [[-1,1,1],[-1,-1,1],[-1,1,1]] #Prewit
    
    conv_gx = convolucion(grises,sx)
    conv_gx.save("Imagen2.jpg")
    conv_gy = convolucion(conv_gx,sy)
    conv_gy.save("Imagen3.jpg")

    i_norm = normalizar(conv_gy)
    i_norm.save("Imagen4.jpg")
    
    imagen_f = b_w(i_norm)
    imagen_f.save("Imagen5.jpg")
    fin = time.time()
    tiempo = fin - start
    print "Tiempo total: "+ str(tiempo)
    
if __name__ == '__main__':
    main()
