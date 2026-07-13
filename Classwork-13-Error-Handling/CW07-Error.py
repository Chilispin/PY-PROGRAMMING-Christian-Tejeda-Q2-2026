class DigitoVerificadorError(Exception):
    pass

check = True
while check:
    rol = input("Ingrese el rol: ")
    
    # CASO 1 y CASO 2: Validar que tenga exactamente un guion
    if rol.count("-") != 1:
        print("Rol inválido: No tiene el formato XXXXXXXXX-X")
        continue # Reinicia el bucle para pedir el rol de nuevo
        
    rol_sin_digito, digito = rol.split("-")
    
    # CASO 3: Validar que la parte del rol sea numérica
    if not rol_sin_digito.isnumeric():
        print("Los digitos del rol deben ser numéricos")
        continue

    # CASO 4: Validar que el dígito verificador sea numérico
    if not digito.isnumeric():
        print("El digito verificador debe ser numérico")
        continue
        
    # Si pasa todas las validaciones de formato, salimos del bucle
    check = False
        
# Invertimos la cadena para el algoritmo del módulo 11
invertido = rol_sin_digito[::-1]

secuencia = [2, 3, 4, 5, 6, 7]
suma = 0

for index in range(len(invertido)):
    multiplicando = secuencia[index % 6]
    numero = int(invertido[index])
    suma += numero * multiplicando
    
total = suma % 11
verificador = 11 - total


try:
    # CASO 5: El dígito no coincide
    if verificador != int(digito):
        raise DigitoVerificadorError(f"Error: El dígito verificador no conicide, se esperaba {verificador}")
except DigitoVerificadorError as e:
    print(e)
else:
    # CASO 6 y CASO 7: El dígito SÍ coincide y el rol es válido
    print(f"{rol_sin_digito}-{verificador}")
