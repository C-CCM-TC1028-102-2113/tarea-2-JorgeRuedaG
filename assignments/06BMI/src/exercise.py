def main():
    #escribe tu código abajo de esta línea
      peso = float(input("Tu peso en kg: "))
    alt = float(input("Tu altura en m: "))
    
    if peso <= 0 or alt <= 0:
        print("Revisa tus datos, alguno es erroneo")
    else:
        indice = peso/alt**2
    if indice < 20:
        print ("peso bajo")
    elif 20 <= indice < 25:
        print ("peso normal")
    elif 25 <= indice < 30:
        print ("sobrepeso")
    elif 30 <= indice < 40:
        print ("obesidad")
    elif indice >= 40:
        print ("obesidad morbida")
    pass
if __name__=='__main__':
    main()
