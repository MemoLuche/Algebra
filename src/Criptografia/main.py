from Codificar import *

dicc = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                    'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27}

dicc_inverso = {valor: clave for clave, valor in dicc.items()}

opcion = None
while opcion != 0:
    while True:
        print('Selecciona la opcion deseada:')
        print('1. Codificar mensaje')
        print('2. Decodificar mensaje')
        print('0. Salir')
        try:
            opcion = int(input())
            break
        except:
            print('Ingresa una opcion valida')
    if opcion == 1:
        frase = ingresarMsg() # Solicitamos la frase y convertimos a una lista de numeros
        n = conseguirN(frase) # Conseguimos el valor de nXn
        matrizMsg = generarMatrizMsg(frase) # Convertimos la frase en matriz
        while True:
            print('Selecciona un opcion')
            print('1. Generar matriz codigo aleatorio')
            print('2. Ingresar una matriz codigo')
            opcion2 = int(input())
            if opcion2 == 1:
                matrizCodigo = generarMatrizCodigo(n) # Generamos la matriz codigo
                print('La matriz codigo generada es:')
                print(matrizCodigo)
                break
            elif opcion2 == 2:
                matrizCodigo = ingresarCodigoInverso()
                print('La matriz codigo es:')
                print(matrizCodigo)
                break
            else:
                print('Elige una opcion valida')
                continue
        matrizCodificada = codificar(matrizMsg, matrizCodigo)
        print('El mensaje codificado es:')
        print(matrizCodificada)
    
    elif opcion == 2:
        print('Cuanto mide tu matriz mensaje:')
        print('Ingrese la medida de n1:')
        n1 = int(input())
        print('Ingrese la medida de n2:')
        n2 = int(input())
        msg = ingresarMensajeEncriptado(n1, n2)
        print(msg)
        mCodigo = ingresarCodigoInverso()
        print(mCodigo)
        codigoInverso = invertirMatriz(mCodigo)
        msgDescifrado = descifrarMensaje(msg, codigoInverso)
        print(msgDescifrado)
        mMensaje = convertirMensajeDescifrado(msgDescifrado)
        print(mMensaje)
    
    elif opcion == 0:
        print('Adios!')

    else:
        print('Elige una opcion correcta')