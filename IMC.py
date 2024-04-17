# CALCULAR LOS IMC DE LOs ESTUDIANTES 

import os 
os.system('cls')
def calcular_imc():
    nombre = input('ingrese el nombre del estudiante')
    edad =  int(input('ingrese la edad de los estudiante'))
    peso = float(input('ingrese el peso de los estdiantes'))
    altura = float(input('ingrese la altuta de los estudiantes'))
    imc = (peso // (altura**2))
    print('imc calcula:',imc)

    print('nombre del estudiante:',nombre)
    print('ingrese la edad del estudiante:',edad)
    print('imc del estudiante:',imc)

    if 18.5 <= imc < 25:
        print('categoria normal') 
    elif 25 <= imc < 30:
        print('categoria peso normal')
    elif 30 <= imc < 35:
        print('categoria sobre peso grado I')
    elif 35 <= imc < 40:
        print('categoria sobre peso gradp II')
    else:
        print('categoria obesidad grado III')

# calcular la funcion
calcular_imc()
    
 

