import math

# INPUT (Manejo de entrada de datos)
try:
    a_input = input("Write the left endpoint of the interval: ")
    if "pi" in a_input:
        a = eval(a_input.replace("pi", str(math.pi)))
    else:
        a = float(a_input)
except (ValueError, SyntaxError, NameError) as e:
    print(f"Error: The left endpoint '{a_input}' is invalid. Details: {e}")
    exit(1)

try:
    b_input = input("Write the right endpoint of the interval: ")
    if "pi" in b_input:
        b = eval(b_input.replace("pi", str(math.pi)))
    else:
        b = float(b_input)
except (ValueError, SyntaxError, NameError) as e:
    print(f"Error: The right endpoint '{b_input}' is invalid. Details: {e}")
    exit(1)

f_x = input("Write the function to integrate (use 'x' as variable): ")
method = input("Write the integration method (LRM/RRM/MRM/TRAP): ").upper().strip()

# PROCESS
try:
    valid_methods = ["LRM", "RRM", "MRM", "TRAP"]
    if method not in valid_methods:
        raise ValueError(f"Method '{method}' is not recognized. Choose from {valid_methods}.")

    n = 1000
    h = (b - a) / n
    area = 0.0
    shift = 0
    constant = 0
    variable = 0

    if method == "RRM":
        shift = 1
        
    elif method == "MRM":
        constant = h / 2
        
    elif method == "TRAP":
        variable = 1
        f_0 = f_x.replace("x", f"({str(a)})")
        area += (h / 2) * eval(f_0)
        
        for i in range(variable, n):
            xi = a + i * h
            f_xi = f_x.replace("x", f"({str(xi)})")
            area += (h / 2) * 2 * eval(f_xi)
            
        f_xn = f_x.replace("x", f"({str(b)})")
        area += (h / 2) * eval(f_xn)
        
    else: 
        for i in range(shift, n + shift):
            xi = a + i * h
            height = f_x.replace("x", f"({str(xi + constant)})")
            area += h * eval(height)

    # OUTPUT (Solo se ejecuta si todo el bloque try corre exitosamente)
    print(f"The integration of {f_x} using {method} is {area}")

except ValueError as e:
    print(f"Validation Error: {e}") [cite: 19]
except (SyntaxError, NameError) as e:
    print(f"Mathematical Error: Could not evaluate the function '{f_x}'. Please check its syntax. Details: {e}") [cite: 14]
except ZeroDivisionError as e:
    print(f"Calculation Error: Division by zero encountered during execution. Details: {e}") [cite: 8, 19]
except Exception as e:
    print(f"An unexpected error occurred: {e}") [cite: 23]