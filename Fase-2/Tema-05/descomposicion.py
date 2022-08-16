import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print("Error-numero es incorrecto")
        print("Ejemplo: descomposicion.py[0-999]")
    else:
        # aqui va la logica
        cadena=str(numero)
        longitud=len(cadena)

        for i in range(longitud):
         print("{:04d}".format(int(cadena[i])))