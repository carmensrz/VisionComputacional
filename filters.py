from PIL import Image
from sys import argv
from math import floor
import numpy 


umbral = 100
imagen = argv[1]
img = Image.open('/home/carmensrz/'+ imagen)
#img.show()
width, height = img.size

def grayscale():

    for i in range(width):
        for j in range(height):
            r,g,b = img.getpixel((i,j))
            average = int(floor((r+g+b)/3))
            #print r,g,b, average
            img.putpixel((i,j),(average,average,average))

    #img.show()
    img.save('graysc_'+imagen)
        
def b_w():
    for i in range(width):
        for j in range(height):
            r,g,b = img.getpixel((i,j))
            mayor = max(r,g,b)
            if(mayor<umbral):
                color = 0
            else: 
                color = 255
            img.putpixel((i,j),(color,color,color))

    img.save('byn_'+imagen)

def blur():
    #vecinos = [] 
    num = 0
    for i in range(width):
        for j in range(height):
            if(i==0):
                vecino = min(img.getpixel((i+1,j)))
                img.putpixel((i,j),(vecino,vecino,vecino))
#                print vecino
            elif(j==0):
                vecino = min(img.getpixel((i,j+1)))
                img.putpixel((i,j),(vecino,vecino,vecino))
#                print vecino
            elif(i==height):
                vecino = min(img.getpixel((i-1,j)))
                img_.putpixel((i,j),(vecino,vecino,vecino))
#                print vecino
            elif(j==width):
                vecino = min(img.getpixel((i,j-1)))
                img.putpixel((i,j),(vecino,vecino,vecino))
#                print vecino
            else:
                try:
                    vecinos=[]
                #pixeles = list(img.getdata())
                    vecinos.append(min(img.getpixel((i,j-1))))
                    vecinos.append(min(img.getpixel((i,j+1))))
                    vecinos.append(min(img.getpixel((i-1,j))))
                    vecinos.append(min(img.getpixel((i+1,j))))
                    vecinos.append(min(img.getpixel((i-1,j-1))))
                    vecinos.append(min(img.getpixel((i+1,j+1))))
                    vecinos.append(min(img.getpixel((i-1,j+1))))
                    vecinos.append(min(img.getpixel((i+1,j-1))))
                    num += 1
                    #print num, vecinos
                    sort_vecinos = sorted(vecinos)
#                    print num, sort_vecinos
                    #print vecinos
                    num1,num2 = vecinos[4:6]
                    mediana = int((num1+num2)/2)
                    img.putpixel((i,j),(mediana,mediana,mediana))

                except:
                    pass
    
    img.save('blur_'+imagen)

def main():
    grayscale()
    b_w()
    blur()
if __name__ == '__main__':
    main()
