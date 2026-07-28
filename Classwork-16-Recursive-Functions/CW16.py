
def recursiva(n):
    if not isinstance(n, int) or isinstance(n, bool):
        return "Error: Input must be an integer."
    if n < 0:
        return "Error: Input must be a non-negative integer."
    
    if n == 0:
        return "Done!"
    else:
        print(n)
        return recursiva(n - 1)


def fibonacci(n):
    if not isinstance(n, int) or isinstance(n, bool):
        return "Error: Input must be an integer."
    if n < 0:
        return "Error: Input must be a non-negative integer."
    
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if not isinstance(n, int) or isinstance(n, bool):
        return "Error: Input must be an integer."
    if n < 0:
        return "Error: Input must be a non-negative integer."
    
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n - 1) * n


def multiplicacion_recursiva(n, m):
    if not (isinstance(n, (int, float)) and isinstance(m, int)) or isinstance(n, bool) or isinstance(m, bool):
        return "Error: Invalid data types."
    if m < 0:
        return "Error: Multiplier (m) must be a non-negative integer."
    
    if m == 0:
        return 0
    else:
        return multiplicacion_recursiva(n, m - 1) + n


def division_entera_recursiva(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)) or isinstance(dividendo, bool) or isinstance(divisor, bool):
        return "Error: Inputs must be integers."
    if divisor <= 0:
        return "Error: Divisor must be greater than 0."
    if dividendo < 0:
        return "Error: Dividend must be a non-negative integer."
    
    if dividendo - divisor < 0:
        return 0
    else:
        return division_entera_recursiva(dividendo - divisor, divisor) + 1


def potencia_recursiva(base, exponente):
    if not (isinstance(base, (int, float)) and isinstance(exponente, int)) or isinstance(base, bool) or isinstance(exponente, bool):
        return "Error: Invalid data types."
    
    if exponente < 0:
        return 1 / potencia_recursiva(base, -exponente)
    if exponente == 0:
        return 1
    else:
        return potencia_recursiva(base, exponente - 1) * base

def serie_collatz(n):
    if not isinstance(n, int) or isinstance(n, bool):
        return "Error: Input must be an integer."
    if n <= 0:
        return "Error: Input must be a positive integer strictly greater than 0."
    
    if n == 1:
        print("END!")
        return 0
    else:
        if n % 2 == 0:
            print(n // 2)
            return serie_collatz(n // 2)
        else:
            print(3 * n + 1)
            return serie_collatz(3 * n + 1)

def aplanar_json(diccionario, clave_padre='', separador='.'):
    if not isinstance(diccionario, dict):
        return "Error: Input must be a dictionary."
    
    elementos = []
    try:
        for key, value in diccionario.items():
            nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else str(key)
            
            if isinstance(value, dict):
                sub_aplanado = aplanar_json(value, nueva_llave, separador)
                if isinstance(sub_aplanado, dict):
                    elementos.extend(sub_aplanado.items())
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    llave_lista = f"{nueva_llave}{separador}{i}"
                    if isinstance(item, (dict, list)):
                        sub_aplanado = aplanar_json(item if isinstance(item, dict) else dict(enumerate(item)), llave_lista, separador)
                        if isinstance(sub_aplanado, dict):
                            elementos.extend(sub_aplanado.items())
                    else:
                        elementos.append((llave_lista, item))
            else:
                elementos.append((nueva_llave, value))
        return dict(elementos)
    except Exception as e:
        return f"Error processing dictionary: {str(e)}"