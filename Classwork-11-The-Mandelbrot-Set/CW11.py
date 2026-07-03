import random
#CREAR CSV
archivo = open("archivo.csv", "w")
#ESCRIBIR ENCABEZADOS
archivo.write("X,Y,COLOR\n")

for _ in range(100_000):
    x = random.uniform(-10,10)
    y = random.uniform(-10,10)
    
    distancia = (x * x + y * y) ** 0.5
    iteraciones = 0
    color = 0
    
    while (distancia < 1) and (iteraciones < 100):
        distancia = distancia ** 2
        iteraciones += 1
        
    
    if distancia > 1: color = 255  
    
    archivo.write(f"{x},{y},{color}\n")
    
archivo.close()

print("Done")
                  
            