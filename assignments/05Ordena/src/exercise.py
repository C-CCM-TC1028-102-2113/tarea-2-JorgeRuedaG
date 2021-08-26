def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if x > y > z:
        print(z)
        print(y)
        print(x)
    elif y > x > z:
        print(z)
        print(x)
        print(y)
    elif x > z > y:
        print(y)
        print(z)
        print(x)
    elif z > x > y:
        print(y)
        print(x)
        print(z)
    elif z > y > x:
        print(x)
        print(y)
        print(z)
    elif y > z > x:
        print(x)
        print(z)
        print(y)
    pass


if __name__=='__main__':
    main()
