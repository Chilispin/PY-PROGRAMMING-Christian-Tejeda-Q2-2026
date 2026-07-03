from PIL import Image

config = {}

archivo = open("config.txt", 'r')

for linea in archivo:
    clave, valor = linea.strip().split('=')
    config[clave] = float(valor) if "." in valor else int(valor)
archivo.close()


with open("clase.csv", 'r') as data:
    datos = data.readlines()

datos.pop(0)

alto, ancho, max_iter = config["alto"], config["ancho"], config["max_iter"]

img = Image.new('HSV', (alto, ancho))


for dato in datos:
    fila, columna, iteraciones = dato.strip().split(",")
    fila, columna, iteraciones = map(int, dato.strip().split(","))
    brillo = 40 if (iteraciones == max_iter) else int((iteraciones / max_iter) * 255)
    img.putpixel((columna, fila), (brillo, 255, 255))
    
img_rgb = img.convert('RGB')
img_rgb.save("mandelbrot-clase.png")

print("DONE") 