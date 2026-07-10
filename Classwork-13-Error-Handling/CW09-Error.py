# INPUT
verbo = input("Ingrese verbo: ").strip().lower()

# PROCESS
try:
    if len(verbo) < 3:
        raise ValueError("El texto ingresado es demasiado corto para ser un verbo válido.")

    pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

   
    terminaciones = {
        'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
        'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
        'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
    }


    stem = verbo[:-2]
    ending = verbo[-2:]

    endings_list = terminaciones[ending]

    # OUTPUT (Se ejecuta dentro del bloque try protegido)
    for index, pronombre in enumerate(pronombres):
        terminacion = endings_list[index]
        print(f"{pronombre} {stem}{terminacion}")

except ValueError as e:
    print(f"Error de validación: {e}")
except KeyError:
    print(f"Error: La terminación '{verbo[-2:]}' no corresponde a un verbo regular ('ar', 'er', 'ir').")
except IndexError as e:
    print(f"Error de índice: No se pudo segmentar el verbo correctamente. Detalles: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")