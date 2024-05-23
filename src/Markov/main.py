import numpy as np

# Definir la matriz estocástica
matriz_transicion = np.array([[0.40, 0.30, 0.30],
                               [0.50, 0.20, 0.30],
                               [0.30, 0.40, 0.30]])

# Definir el vector de estado inicial
estado_inicial = np.array([1, 0, 0])  # Por ejemplo, suponiendo que el clima inicialmente es bueno

# Función para aplicar la matriz de transición de forma recursiva
def aplicar_matriz(matriz, vector, iteraciones):
    if iteraciones == 0:
        return vector
    else:
        nuevo_vector = np.dot(vector, matriz)
        return aplicar_matriz(matriz, nuevo_vector, iteraciones - 1)

# Definir el número de veces que se aplicará la matriz
num_iteraciones = 10

# Aplicar la matriz de transición de forma recursiva
resultado_python = aplicar_matriz(matriz_transicion, estado_inicial, num_iteraciones)

print("Resultado obtenido mediante Python después de", num_iteraciones, "iteraciones:")
print(resultado_python)
