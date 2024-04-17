class sismo:
    def __init__(self,magnitud):
        self,magnitud = magnitud
    
class ciudad:
    def __init__(self,nombre):
        self.nombre = nombre
        self.sismo = []
    def agregar_sismo(seff, magnitud):
        seff.sismo.append(sismo(magnitud))

    def obtener_promedio_de_sismos(self):
        suma_sismos = sum([sismo.magnitud for sismo in self.sismos])
        return suma_sismos / len(self.sismo) if self.sismos else 0
def registrar_ciudad(ciudades):
    nombre_ciudad = input('ingrese el nombre de la ciudad:')
    ciudades.append(ciudad(nombre_ciudad))
    print('ciudades registrada exitosamente.')
def registar_sismos(ciudades):
    nombre_ciudad = input('ingrese el nombre de la ciudad:')
    magnitud_sismo = float(input('ingrese la magnitud del sismo:'))
    for ciudad in ciudades:
        if ciudades.nombre == nombre_ciudad:
            ciudad.agregar_sismo(magnitud_sismo)
            print('sismo registrado exitosamente en', nombre_ciudad)
            return
    print('ciudad no encontrada.')

def buscar_sismo(ciudades):
    nombre_ciudad = input('ingrese el nombre de la ciudad: ')
    for ciudad in ciudades:
        if ciudad.nombre == nombre_ciudad:
            print('sisimos en', nombre_ciudad + ':')
            for sismo in ciudad.sismos:
                print('- magnitud:',sismo.magnitud)
            return
    print('ciudad no encontrada.')

def informe_riesgo(ciudades):
    nombre_ciudad = input('ingrese el nombre de la ciudad:')
    for ciudad in ciudades:
        if ciudad.nombre == nombre_ciudad:
            promedio_sismo = ciudad.obtener_promedio_sismos()
            if promedio_sismo < 2.5:
                print('informe de riesgo para',nombre_ciudad + ':','amarillo (sin riesgo)')
            elif 2.5 <= promedio_sismo <= 4.5:
                print('informe de riesgo para', nombre_ciudad + ':', 'naranja (riesgo miego)')
            else:
                print('informe de riesgo para', nombre_ciudad + ':', 'rojo (riesgo alto)')
            return
    print('ciudad no encontrada.')

def main():
    ciudades = []
    while True:
        print(""")
              menu:
              1. registrar ciudad
              2. regidtrar sismo
              3. buscar sismo por ciudad
              4. informe de riesgo
              5. salir
              """)
        opcion = input('seleccione una opcion:')
        if opcion == '1':
               registrar_ciudad(ciudades)
        elif opcion == '2':
               registar_sismos(ciudades)
        elif opcion == '3':
               buscar_sismo(ciudades)
        elif opcion == '4':
               informe_riesgo(ciudades)
        elif opcion == '5':
               break
        else:
             print('opcion no valida. intentelo de nuevo.')
if __name__ == '__main__':
     main()