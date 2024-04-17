def main():
    numeros = 0
    total_numero = 0
    total_pares = 0 
    total_impares = 0
    suma_pares = 0 
    suma_impares = 0
    menores_de_10 = 0
    entre_20_y_50 = 0
    mayores_que_100 = 0

    while True:
        num = int(input('ingrese el numero entero pasitivo (ingrese un número negativo para terminar):'))

        if num < 0:
            break

        numeros.append(num)
        total_numero += 1

        if num % 2 == 0:
            total_pares += 1
            suma_pares += num
        else:
            total_impares += 1
            suma_impares += num
        if num < 10:
            menores_de_10 += 1
        elif 20 <= num <= 50:
            entre_20_y_50 += 1
        elif num >  100:
            mayores_que_100 += 1
    if total_pares > 0:
        promedio_pares = suma_pares / total_pares
    else:
        promedio_impares = 0
    if total_impares > 0:
        promedio_impares = suma_impares / total_impares
    else:
        promedio_impares = 0
    
    print('\nreporte:')

    print('A. total de numeros ingresasados:', total_numero)
    print('B total de numeros  pares ingresados:',total_pares)
    print('C promedio de los numero pares:', promedio_pares)
    print('D promedio de los numero impares:', promedio_impares)
    print('E cuantos numeros son menores que 10:',menores_de_10)
    print('F cuantos numeros estan entre 20 y 50:',entre_20_y_50)
    print('G cuantos numeros son mayores que 100:',mayores_que_100)
if __name__ == "__main__":
    main()




    