# Definición de la matriz 3D de temperaturas para ciudades de Ecuador
# Estructura: Ciudad, semana, dia
temperaturas = [
    # Quito
    [
        [15, 16, 15, 14, 15, 15, 16],  # Semana 1: Temperaturas diarias
        [16, 15, 14, 15, 16, 16, 15]   # Semana 2: Temperaturas diarias
    ],
    # Guayaquil
    [
        [25, 26, 27, 26, 25, 26, 27],  # Semana 1: Temperaturas diarias
        [26, 27, 28, 27, 26, 27, 28]   # Semana 2: Temperaturas diarias
    ],
    # Cuenca
    [
        [19, 18, 17, 18, 19, 18, 19],  # Semana 1: Temperaturas diarias
        [18, 17, 18, 19, 20, 19, 18]   # Semana 2: Temperaturas diarias
    ]
]

# Mostrar las ciudades de Ecuador para mostrar en los resultados
nombres_ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Índice de ciudad inicial para el bucle while
i = 0

#bucles while anidados
while i < len(temperaturas):
    # Imprime el nombre de la ciudad
    print(nombres_ciudades[i] + ":")
    # Inicializa el índice de semana
    j = 0
    while j < len(temperaturas[i]):
        # Inicializa el índice de día y la suma de temperaturas
        k = 0
        suma_temperaturas = 0
        while k < len(temperaturas[i][j]):
            # Suma las temperaturas de la semana
            suma_temperaturas += temperaturas[i][j][k]
            k += 1
        # Calcula el promedio de temperatura de la semana
        promedio = suma_temperaturas / len(temperaturas[i][j])
        # Imprime el promedio de temperatura de la semana
        print(f"  Semana {j + 1}: Promedio de temperatura = {promedio:.2f}°C")
        j += 1
    print()  # espacio
    i += 1