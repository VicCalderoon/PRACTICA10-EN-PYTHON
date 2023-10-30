def sumaIterativa(n):
    suma = 0

    while n > 9:
        suma += n % 10
        n //= 10

    return suma + n

def main():
    numero = 12345
    resultado = sumaIterativa(numero)
    print(f"La suma de los dígitos de {numero} es {resultado}")

if _name_ == "_main_":
    main()
