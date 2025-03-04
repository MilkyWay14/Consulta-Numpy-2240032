# 2240032 - Daniver Franchesco Hernandez Acero

#Se crea una matriz con código, nombre, promedio y carrera
import numpy as np

# Generar el vector de códigos aleatorios, suponiendo que los códigos son iguales desde el 1948, cuando se fundó
# Los códigos del 1948 empiezan con 148 y los del 2025 con 225
codigo_aleatorio = np.random.randint(1480000, 2260000, size=6500)

# Definir los arrays de nombres y apellidos, se pueden generar 10 mil nombres
nombres1 = np.array(['Octavio','Victorino', 'Nicolae', 'Jonatan', 'Alexis', 'Nabil', 'Maria', 'Susana', 'Mia', 'Benita'])
nombres2 = np.array(['Fernanda', 'Luz', 'Yasmin', 'Antonia', 'Davinia', 'Delfina', 'Diana', 'Minerva', 'Angel', 'Ferran'])
apellidos1 = np.array(['Velazquez', 'Galan', 'Redondo', 'Zafra', 'Correa', 'Chavez', 'Saura', 'Rios', 'Hernandez', 'Lopez','Espinoza'])
apellidos2 = np.array(['Montesino', 'Cantos', 'Zambrano', 'Pelaez', 'Mayoral', 'Espejo', 'Seco', 'Marco', 'Castellanos','Tejados'])

# Inicializar una lista para almacenar los nombres completos
nombres_completos = []

# Generar 6500 nombres aleatorios
for _ in range(6500):
    # Seleccionar aleatoriamente un elemento de cada array
    nombre1 = np.random.choice(nombres1)
    nombre2 = np.random.choice(nombres2)
    apellido1 = np.random.choice(apellidos1)
    apellido2 = np.random.choice(apellidos2)
    
    # Combinar los elementos seleccionados en un nombre completo
    nombre_completo = f"{nombre1} {nombre2} {apellido1} {apellido2}"
    
    # Agregar el nombre completo a la lista
    nombres_completos.append(nombre_completo)

# Convertir la lista a un array de NumPy
nombres_completos = np.array(nombres_completos)

# Lista de promedios ponderados aleatorios de 0 a 5
promedios = np.random.uniform(0, 5, size=6500)
# Con 2 cifras decimales
promedios = np.round(promedios, decimals=2)

# Lista de carreras aleatorias de 1 a 72
carreras = np.random.randint( 1 , 72 , size=6500 )

#Unir columnas (listas) a una matriz, matriz de columnas: código, nombre, promedio, carrera
matriz = np.column_stack((codigo_aleatorio, nombres_completos, promedios, carreras))

# Leer la carrera usada en el filtro
carrera = int(input('Ingrese la carrera de los estudiantes a filtrar: '))

# Crear matriz con filtro de promedio mayor que 4 y carrera leída
estudiantes_filtrados = matriz[(matriz[:, 2].astype(float) >= 4) & (matriz[:, 3].astype(int) == carrera)]

# Imprimir solo código y nombre de los filtrados
print(f"\nEstudiantes con promedio mayor o igual a 4 en la carrera : {carrera} \n")
for estudiante in estudiantes_filtrados:
    print(f"Código: {estudiante[0]}, Nombre: {estudiante[1]}")
print(f"\nEstudiantes con promedio mayor o igual a 4 de carrera {carrera} encontrados: {len(estudiantes_filtrados)}")

# Crear matriz con filtro de estudiantes condicionales e ingresados antes del 1990
condicionales_1990 = matriz[(matriz[:, 0].astype(int) < 1900000) & (matriz[:, 2].astype(float) >= 2.7) & (matriz[:, 2].astype(float) < 3.2)]

# Imprimir solo código y nombre de los filtrados
print(f"\nEstudiantes condicionales")
for estudiante in condicionales_1990:
    print(f"Código: {estudiante[0]}, Nombre: {estudiante[1]}")
print("\nEstudiantes condicionales encontrados antes del 1990: ", len(condicionales_1990))