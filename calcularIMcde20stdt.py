# calcualr los IMC  de 10}
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
peso_ideal =0
obesidad_1 = 0
obesidad_2 = 0
obesidad_3 = 0
sobrepeso = 0

for _ in range(15):
    nombre = input('ingrese la nombre del estudiante:')
    edad = int(input('ingrese la edad de  {}:'.format(nombre)))
    peso = float(input('ingrese el peso de {}:'.format(nombre)))
    altura = float(input('ingrese la altura de  {}:'.format(nombre)))


    imc = calcular_imc(peso, altura)
    if imc < 18.5:
        categoria = "bajo peso"
    elif imc < 24.9:
        categoria =  'peso normal (peso ideal)'
        peso_ideal += 1
    elif imc < 29.9:
        categoria = 'sobrepeso'
        sobrepeso += 1
    elif imc < 34.9:
        categoria = 'obesidad grado I'
        obesidad_1 +=1
    elif imc < 39.9:
        categoria = 'obesidad grado II'
        obesidad_2 += 1
    else:
        categoria = 'obesisdad grado III (Obesidad morbida)'
        obesidad_3 += 1

    print('nombre: {}, edad: {}, IMC: {:.2f}, categoria IMC: {}'.format(nombre, edad, imc, categoria))
    
    print('\nreporte:')
    print('estiantes en peso ideal: {}'.format(peso_ideal))
    print('estudiante en obesidad grado I: {}'.format(obesidad_1))
    print('estudiante en obesidad grado II: {}'.format(obesidad_2))
    print('estudantes en obesidad grado III: {}'.format(obesidad_3))
    print('estudiante sobre peso: {}'.format(sobrepeso))
    