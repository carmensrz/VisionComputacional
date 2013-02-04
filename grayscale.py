from PIL import Image
from sys import argv
from math import floor

imagen = argv[1]
img = Image.open('/home/carmensrz/'+ imagen)
img.show()
width, height = img.size

def grayscale():

    for i in range(width):
        for j in range(height):
            r,g,b = img.getpixel((i,j))
            average = int(floor((r+g+b)/3))
            #print r,g,b, average
            img.putpixel((i,j),(average,average,average))

    img.show()
    img.save('graysc_'+imagen)

def main():
    grises()
    
if __name__ == '__main__':
    main()
