rol_ingresado = input("Por favor, ingresa el rol (sin guión ni dígito): ")

rol_invertido = ""
for caracter in rol_ingresado:
    rol_invertido = caracter + rol_invertido

suma_total = 0
multiplicador = 2

for digito in rol_invertido:
    numero = int(digito)
    producto = numero * multiplicador
    suma_total = suma_total + producto

    multiplicador = multiplicador + 1
    if multiplicador == 8:
        multiplicador = 2

resto = suma_total % 11
resta = 11 - resto

if resta == 11:
    digito_verificador = "0"
elif resta == 10:
    digito_verificador = "K"
else:
    digito_verificador = str(resta)
    
print("----------------------------------------")
print("Resultado final:", rol_ingresado + "-" + digito_verificador)
print("----------------------------------------")