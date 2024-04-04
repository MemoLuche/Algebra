import numpy as np
import math

dicc = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                    'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27}

#Ingreso del mensaje y transformacion
frase = input()
fraseEnNum = list(dicc[letra] for letra in frase.upper())
n = math.ceil(math.sqrt(len(fraseEnNum)))

# Calcular la cantidad de elementos que faltan para que la matriz sea cuadrada
faltantes = n**2 - len(fraseEnNum)

# Agregar espacios adicionales si es necesario
fraseEnNum.extend([27] * faltantes)

mensaje = np.array(fraseEnNum).reshape(n, n)
print('Matriz mensaje:')
print(mensaje)

mCodigo = generar_matriz_enteros(n)
print("Matriz codigo:")
print(mCodigo)

mCodificado = np.dot(mensaje, mCodigo)
print('Matriz codificada')
print(mCodificado)