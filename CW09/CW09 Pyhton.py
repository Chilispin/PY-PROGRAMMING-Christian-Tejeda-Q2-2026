# INPUT
verbo = input("Ingrese verbo: ")

# PROCESS
# List of pronouns (required structure)
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

# Dictionary of endings by verb type (required structure)
terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# Get stem (verb minus last 2 letters) and ending (last 2 letters)
stem = verbo[:-2]
ending = verbo[-2:]

# Look up the matching endings list in the dictionary
endings_list = terminaciones[ending]

# OUTPUT
for index, pronombre in enumerate(pronombres):
    terminacion = endings_list[index]
    print(f"{pronombre} {stem}{terminacion}")