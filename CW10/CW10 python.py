# ==========================================
# DATA INICIALIZADA (6 Alumnos, 1 Maestro, 1 Coordinator)
# ==========================================
usuarios = {
    'jperez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno', 'nombre': 'Ana Martín'},
    'gsolis': {'password': '1234', 'rol': 'alumno', 'nombre': 'Gerardo Solís'},
    'lcanche': {'password': '1234', 'rol': 'alumno', 'nombre': 'Lizbeth Canché'},
    'mpech': {'password': '1234', 'rol': 'alumno', 'nombre': 'Manuel Pech'},
    'ucahuich': {'password': '1234', 'rol': 'alumno', 'nombre': 'Uriel Cahuich'},
    'Chilispin': {'password': '1234', 'rol': 'maestro', 'nombre': 'Christian Tejeda'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}

# Tupla fija e inmutable de materias
materias = ('Matemáticas', 'Programación', 'Inglés')

# Historial de calificaciones correspondientes a las llaves de usuarios
calificaciones = {
    'jperez': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'amartin': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'gsolis': {'Matemáticas': 7.0, 'Programación': 8.5, 'Inglés': 6.0},
    'lcanche': {'Matemáticas': 9.5, 'Programación': 10.0, 'Inglés': 9.0},
    'mpech': {'Matemáticas': 6.5, 'Programación': 7.5, 'Inglés': 8.0},
    'ucahuich': {'Matemáticas': 8.0, 'Programación': 9.0, 'Inglés': 8.5}
}

usuario_actual = ""
login_exitoso = False

while not login_exitoso:
    print("\n--- LOGIN SISTEMA UPY ---")
    username = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()
    
    if username in usuarios and usuarios[username]['password'] == password:
        login_exitoso = True
        usuario_actual = username
        rol = usuarios[username]['rol']
        nombre = usuarios[username]['nombre']
        print(f"\nBienvenido, {nombre} ({rol})")
    else:
        print("Credenciales incorrectas. Intente de nuevo.")

# 2. Ramificación por Roles mediante condicionales
if rol == 'alumno':
    print(f"\nBoleta de {nombre}")
    aprobadas = set()
    
    # Iteración usando la tupla de materias
    for materia in materias:
        nota = calificaciones[usuario_actual][materia]
        print(f"{materia}: {nota}")
        
        # Guardar en conjunto si es aprobatoria
        if nota >= 8.0:
            aprobadas.add(materia)
            
    # El conjunto de materias pendientes se obtiene por diferencia de conjuntos
    pendientes = set(materias) - aprobadas
    
    print(f"Materias aprobadas: {aprobadas}")
    print(f"Materias pendientes: {pendientes}")

elif rol == 'maestro':
    print("\n--- Lista de Alumnos de la sección ---")
    for usr, info in usuarios.items():
        if info['rol'] == 'alumno':
            print(f"- {info['nombre']} (Username: {usr})")
            
    print("\n--- Modificación de Notas ---")
    alumno_target = input("Alumno (escribe el username): ").strip()
    
    if alumno_target in calificaciones:
        materia_target = input("Materia: ").strip()
        
        # Validar la materia usando la tupla global
        if materia_target in materias:
            try:
                nueva_calif = float(input("Nueva calificación: "))
                calificaciones[alumno_target][materia_target] = nueva_calif
                print("Calificación actualizada con éxito.")
            except ValueError:
                print("Error: Ingresa un valor numérico válido.")
        else:
            print("Error: La materia especificada no forma parte del plan de estudios.")
    else:
        print("Error: El alumno ingresado no existe.")

elif rol == 'coordinador':
    print("\n==============================================")
    print("REPORTE ACADÉMICO GLOBAL (MODO LECTURA)")
    print("==============================================")
    
    print("\n1. Docentes Activos:")
    for usr, info in usuarios.items():
        if info['rol'] == 'maestro':
            print(f"   • {info['nombre']}")
            
    print("\n2. Plan de Asignaturas:")
    for materia in materias:
        print(f"   • {materia}")
        
    print("\n3. Concentrado de Calificaciones de Alumnos:")
    for estudiante, mapeo_notas in calificaciones.items():
        nombre_estudiante = usuarios[estudiante]['nombre']
        print(f"   Estudiante: {nombre_estudiante}")
        for materia in materias:
            print(f"      - {materia}: {mapeo_notas[materia]}")