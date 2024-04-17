class Jugador:
    def _init_(self, id_jugador, nombre, edad, categoria):
        self.id_jugador = id_jugador
        self.nombre = nombre
        self.edad = edad
        self.categoria = categoria
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_perdidos = 0
        self.puntos_a_favor = 0
    
    def registrar_partido(self, puntos_ganados, puntos_perdidos):
        self.partidos_jugados += 1
        if puntos_ganados > puntos_perdidos:
            self.partidos_ganados += 1
        else:
            self.partidos_perdidos += 1
        self.puntos_a_favor += puntos_ganados - puntos_perdidos

class TorneoTenisMesa:
    def _init_(self):
        self.jugadores = []
    
    def registrar_jugador(self, id_jugador, nombre, edad, categoria):
        if (categoria == "Novato" and 15 <= edad <= 16) or \
           (categoria == "Intermedio" and 17 <= edad <= 20) or \
           (categoria == "Avanzado" and edad > 20):
            jugador = Jugador(id_jugador, nombre, edad, categoria)
            self.jugadores.append(jugador)
            print(f"Jugador {nombre} registrado correctamente en la categoría {categoria}.")
        else:
            print("El jugador no cumple con los requisitos de edad para la categoría especificada.")

    def iniciar_juegos(self, categoria):
        jugadores_categoria = [jugador for jugador in self.jugadores if jugador.categoria == categoria]
        if len(jugadores_categoria) < 5:
            print("No hay suficientes jugadores inscritos en la categoría para iniciar los juegos.")
            return
        # Lógica para llevar a cabo los juegos y registrar resultados
    
    def obtener_ganador(self, categoria):
        jugadores_categoria = [jugador for jugador in self.jugadores if jugador]
        print(jugadores_categoria and categoria)