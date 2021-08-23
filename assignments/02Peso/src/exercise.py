def main():
    #escribe tu código abajo de esta línea
    pesoI = float(input("¿Cuánto pesas? "))
    pesoF = float(input("¿Cuánto quieres pesar? "))
    meses = float(input("¿En cuántos meses quieres bajar de peso? "))
    pesoMes = (pesoI-pesoF)/meses
    print("Debes bajar "+str(pesoMes)+" kilos cada mes")



if __name__ == '__main__':
    main()
