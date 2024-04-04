import numpy as np
import math

# Generar matriz codigo aleatorio
def generar_matriz_enteros(n):
    # Generar una matriz aleatoria con números enteros entre -10 y 10
    matriz = np.random.randint(-10, 11, size=(n, n))
    
    # Verificar si la matriz es invertible y su inversa contiene números enteros
    try:
        inversa = np.linalg.inv(matriz)
        if np.all(inversa.astype(int) == inversa):  # Verificar si todos los elementos de la inversa son enteros
            return matriz
        else:
            return generar_matriz_enteros(n)  # Si la inversa no tiene números enteros, generar otra matriz
    except np.linalg.LinAlgError:  # Si la matriz no es invertible, generar otra matriz
        return generar_matriz_enteros(n)

dicc = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                    'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27}

dicc_inverso = {valor: clave for clave, valor in dicc.items()}

# Ingreso del mensaje y transformación
def ingresarFrase():
    frase = input()
    fraseEnNum = list(dicc[letra] for letra in frase.upper())
    return fraseEnNum

# Convertir frase en una matriz
def matrizMensaje(m1):
    n = math.ceil(math.sqrt(len(m1)))
    # Calcular la cantidad de elementos que faltan para que la matriz sea cuadrada
    faltantes = n**2 - len(m1)

    # Agregar espacios adicionales si es necesario
    m1.extend([27] * faltantes)

    mensaje = np.array(m1).reshape(n, n)
    print('Matriz mensaje:')
    print(mensaje)
    return mensaje

# Conseguir el valor de nXn
def conseguirN(m1):
    n = math.ceil(math.sqrt(len(m1)))
    return n

# Codificar el mensaje
def codificar(mensaje, mCodigo):
    mCodificado = np.dot(mensaje, mCodigo)
    print('Matriz codificada')
    print(mCodificado)
    return mCodificado

# Generar la matriz para descifrar
def matrizDescifrar(mCodigo):
    mCodigoDescifrar = np.linalg.inv(mCodigo)
    print('Matriz descifrado')
    print(mCodigoDescifrar)
    return mCodigoDescifrar

# Insertar la matriz para descifrar
def ingresarMatrizCodigoInverso():
    m1 = list(input().split(' '))
    n = math.ceil(math.sqrt(len(m1)))
    codigoInverso = np.array(m1).reshape(n, n)
    return codigoInverso

# Descifrar el mensaje
def descifrarMensaje(mCDescifrar, mCodificado):
    mDescifrado = np.dot(mCodificado, mCDescifrar)
    print('Matriz decodificada')
    print(mDescifrado)
    return mDescifrado

# Convertir los números descifrados a letras
def convertirMensajeDescifrado(mDescifrado):
    fraseTransformada = [dicc_inverso[int(letra)] for fila in mDescifrado for letra in fila]
    cadena = ''.join(fraseTransformada)
    print('Mensaje descodificado:')
    print(cadena)
    return cadena
