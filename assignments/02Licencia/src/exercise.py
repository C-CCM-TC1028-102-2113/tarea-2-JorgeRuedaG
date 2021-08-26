
def main():
    #Escribe tu código debajo de esta línea
     edad=int(input("ingresa tu edad:"))
    if edad >= 18:
        R = (input("Tienes identificación oficial? (s/n):"))
    elif edad < 18 and edad >= 1:
        print("No cumples los requisitos")
    else:
        print("Respuesta incorrecta")
    if str(R)=="s":
        print("Tramite de licencia concedido")
    elif R =="n":
        print("No cumples los requisitos")
    else:
        print("Respuesta incorrecta")
    pass


if __name__ == '__main__':
    main()
