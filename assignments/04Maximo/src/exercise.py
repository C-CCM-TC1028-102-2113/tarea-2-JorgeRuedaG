def main():
    #escribe tu código abajo de esta línea
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if x > y > z:
        print(x)
    elif y > x > z:
        print(y)
    elif x > z > y:
        print(x)
    elif z > x > y:
        print(z)
    elif z > y > x:
        print(z)
    elif y > z > x:
        print(y)
    pass


if __name__=='__main__':
    main()
