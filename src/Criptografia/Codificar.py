import numpy as np
import math

# Generar matriz codigo aleatorio
def generarMatrizCodigo(n):
    # Generar una matriz aleatoria con números enteros entre -10 y 10
    matriz = np.random.randint(-10, 11, size=(n, n))
    
    # Verificar si la matriz es invertible y su inversa contiene números enteros
    try:
        inversa = np.linalg.inv(matriz)
        if np.all(inversa.astype(int) == inversa):  # Verificar si todos los elementos de la inversa son enteros
            return matriz
        else:
            return generarMatrizCodigo(n)  # Si la inversa no tiene números enteros, generar otra matriz
    except np.linalg.LinAlgError:  # Si la matriz no es invertible, generar otra matriz
        return generarMatrizCodigo(n)

dicc = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                    'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27, '0': 28, 
                    '1': 29, '2': 30, '3': 31, '4': 32, '5': 33, '6': 34, '7': 35, '8': 36, '9': 37}

dicc_inverso = {valor: clave for clave, valor in dicc.items()}

# Ingreso del mensaje y transformación
def ingresarMsg():
    print('Ingresar la frase a encriptar')
    frase = input()
    fraseEnNum = list(dicc[letra] for letra in frase.upper())
    return fraseEnNum

# Convertir frase en una matriz
def generarMatrizMsg(mensaje):
    n = math.ceil(math.sqrt(len(mensaje)))
    # Calcular la cantidad de elementos que faltan para que la matriz sea cuadrada
    faltantes = n**2 - len(mensaje)

    # Agregar espacios adicionales si es necesario
    mensaje.extend([27] * faltantes)

    matriz = np.array(mensaje).reshape(n, n)
    print('Matriz mensaje:')
    print(matriz)
    return matriz

# Conseguir el valor de nXn
def conseguirN(mensaje):
    n = math.ceil(math.sqrt(len(mensaje)))
    return n

# Codificar el mensaje
def codificar(mMensaje, mCodigo):
    mCodificado = np.dot(mMensaje, mCodigo)
    print('Matriz codificada')
    print(mCodificado)
    return mCodificado

# Generar la matriz para descifrar
def invertirMatriz(mCodigo):
    mCodigoDescifrar = np.linalg.inv(mCodigo)
    print('Matriz descifrado')
    print(mCodigoDescifrar)
    return mCodigoDescifrar

# Insertar la matriz para descifrar
def ingresarCodigoInverso():
    print('Ingresa la matriz inversa separando los valores con espacios')
    mCodigo = list(map(int, input().split(' ')))
    n = math.ceil(math.sqrt(len(mCodigo)))
    codigoInverso = np.array(mCodigo).reshape(n, n)
    return codigoInverso

# Descifrar el mensaje
def descifrarMensaje(mCodificado, cInverso):
    mDescifrado = np.dot(mCodificado, cInverso)
    print('Matriz decodificada')
    print(mDescifrado)
    return mDescifrado

# Convertir los números descifrados a letras
def convertirMensajeDescifrado(mDescifrado):
    fraseTransformada = [dicc_inverso[round(letra)] for fila in mDescifrado for letra in fila]
    cadena = ''.join(fraseTransformada)
    print('Mensaje descodificado:')
    print(cadena)
    return cadena

def ingresarMensajeEncriptado(n1, n2):
    print('Ingresa el mensaje a decodificar')
    m1 = list(map(int, input().split(' ')))
    msgEncriptado = np.array(m1).reshape(n1, n2)
    return msgEncriptado