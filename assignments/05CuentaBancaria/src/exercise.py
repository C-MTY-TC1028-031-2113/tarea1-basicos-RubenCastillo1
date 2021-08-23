def main():
    #escribe tu código abajo de esta línea
    mesA = float(input("Dame el saldo del mes anterior: "))
    ing = float(input("Dame tus ingresos: "))
    eg = float(input("Dame tus egresos: "))
    che = float(input("Dame el número de cheques expedidos: "))
    mesB = (mesA+ing-eg-(che*13))*.925
    print("El saldo final de la cuenta es: "+str(mesB))




if __name__ == '__main__':
    main()
