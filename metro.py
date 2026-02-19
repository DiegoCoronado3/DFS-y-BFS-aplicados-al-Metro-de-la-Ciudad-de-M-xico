"""
Grafo del Metro de la Ciudad de México
Modelo: No dirigido (bidireccional), No ponderado
Incluye todas las 12 líneas y estaciones con transbordos
"""

class MetroCDMX:
    def __init__(self):
        self.grafo = {}
        self._construir_grafo()
    
    def agregar_arista(self, estacion1, estacion2):
        """Agrega una arista bidireccional entre dos estaciones"""
        if estacion1 not in self.grafo:
            self.grafo[estacion1] = []
        if estacion2 not in self.grafo:
            self.grafo[estacion2] = []
        
        if estacion2 not in self.grafo[estacion1]:
            self.grafo[estacion1].append(estacion2)
        if estacion1 not in self.grafo[estacion2]:
            self.grafo[estacion2].append(estacion1)
    
    def _construir_grafo(self):
        """Construye el grafo completo del Metro CDMX"""
        
        # LÍNEA 1 (Rosa) - Observatorio a Pantitlán
        linea1 = [
            "Observatorio", "Tacubaya", "Juanacatlan", "Chapultepec",
            "Sevilla", "Insurgentes", "Cuauhtemoc", "Balderas",
            "Salto del Agua", "Isabel la Catolica", "Pino Suarez",
            "Merced", "Candelaria", "San Lazaro", "Moctezuma",
            "Balbuena", "Boulevard Puerto Aereo", "Gomez Farias",
            "Zaragoza", "Pantitlan"
        ]
        for i in range(len(linea1) - 1):
            self.agregar_arista(linea1[i], linea1[i + 1])
        
        # LÍNEA 2 (Azul) - Cuatro Caminos a Tasqueña
        linea2 = [
            "Cuatro Caminos", "Panteones", "Tacuba", "Cuitlahuac",
            "Popotla", "Colegio Militar", "Normal", "San Cosme",
            "Revolucion", "Hidalgo", "Bellas Artes", "Allende",
            "Zocalo", "Pino Suarez", "San Antonio Abad", "Chabacano",
            "Viaducto", "Xola", "Villa de Cortes", "Nativitas",
            "Portales", "Ermita", "General Anaya", "Tasqueña"
        ]
        for i in range(len(linea2) - 1):
            self.agregar_arista(linea2[i], linea2[i + 1])
        
        # LÍNEA 3 (Verde) - Indios Verdes a Universidad
        linea3 = [
            "Indios Verdes", "Deportivo 18 de Marzo", "Potrero",
            "La Raza", "Tlatelolco", "Guerrero", "Hidalgo",
            "Juarez", "Balderas", "Niños Heroes", "Hospital General",
            "Centro Medico", "Etiopia", "Eugenia", "Division del Norte",
            "Zapata", "Coyoacan", "Viveros", "Miguel Angel de Quevedo",
            "Copilco", "Universidad"
        ]
        for i in range(len(linea3) - 1):
            self.agregar_arista(linea3[i], linea3[i + 1])
        
        # LÍNEA 4 (Cian) - Martín Carrera a Santa Anita
        linea4 = [
            "Martin Carrera", "Talisman", "Bondojito", "Consulado",
            "Canal del Norte", "Morelos", "Candelaria", "Fray Servando",
            "Jamaica", "Santa Anita"
        ]
        for i in range(len(linea4) - 1):
            self.agregar_arista(linea4[i], linea4[i + 1])
        
        # LÍNEA 5 (Amarilla) - Politécnico a Pantitlán
        linea5 = [
            "Politecnico", "Instituto del Petroleo", "Autobuses del Norte",
            "La Raza", "Misterios", "Valle Gomez", "Consulado",
            "Eduardo Molina", "Aragon", "Oceania", "Terminal Aerea",
            "Hangares", "Pantitlan"
        ]
        for i in range(len(linea5) - 1):
            self.agregar_arista(linea5[i], linea5[i + 1])
        
        # LÍNEA 6 (Roja) - El Rosario a Martín Carrera
        linea6 = [
            "El Rosario", "Tezozómoc", "Azcapotzalco", "Ferrería",
            "Norte 45", "Vallejo", "Instituto del Petróleo", "Lindavista",
            "Deportivo 18 de Marzo", "La Villa-Basílica", "Martín Carrera"
        ]
        for i in range(len(linea6) - 1):
            self.agregar_arista(linea6[i], linea6[i + 1])
        
        # LÍNEA 7 (Naranja) - El Rosario a Barranca del Muerto
        linea7 = [
            "El Rosario", "Aquiles Serdan", "Camarones", "Refineria",
            "Tacuba", "San Joaquin", "Polanco", "Auditorio",
            "Constituyentes", "Tacubaya", "San Pedro de los Pinos",
            "San Antonio", "Mixcoac", "Barranca del Muerto"
        ]
        for i in range(len(linea7) - 1):
            self.agregar_arista(linea7[i], linea7[i + 1])
        
        # LÍNEA 8 (Verde-Naranja) - Garibaldi a Constitución de 1917
        linea8 = [
            "Garibaldi", "Bellas Artes", "San Juan de Letran",
            "Salto del Agua", "Doctores", "Obrera", "Chabacano",
            "La Viga", "Santa Anita", "Coyuya", "Iztacalco",
            "Apatlaco", "Aculco", "Escuadron 201", "Atlalilco",
            "Iztapalapa", "Cerro de la Estrella", "UAM-I",
            "Constitucion de 1917"
        ]
        for i in range(len(linea8) - 1):
            self.agregar_arista(linea8[i], linea8[i + 1])
        
        # LÍNEA 9 (Café) - Tacubaya a Pantitlán
        linea9 = [
            "Tacubaya", "Patriotismo", "Chilpancingo", "Centro Medico",
            "Lazaro Cardenas", "Chabacano", "Jamaica", "Mixiuhca",
            "Velodromo", "Ciudad Deportiva", "Puebla", "Pantitlan"
        ]
        for i in range(len(linea9) - 1):
            self.agregar_arista(linea9[i], linea9[i + 1])
        
        # LÍNEA A (Morada) - Pantitlán a La Paz
        lineaA = [
            "Pantitlan", "Agricola Oriental", "Canal de San Juan",
            "Tepalcates", "Guelatao", "Peñon Viejo", "Acatitla",
            "Santa Marta", "Los Reyes", "La Paz"
        ]
        for i in range(len(lineaA) - 1):
            self.agregar_arista(lineaA[i], lineaA[i + 1])
        
        # LÍNEA B (Verde-Gris) - Buenavista a Ciudad Azteca
        lineaB = [
            "Buenavista", "Guerrero", "Garibaldi", "Lagunilla",
            "Tepito", "Morelos", "San Lazaro", "Ricardo Flores Magon",
            "Romero Rubio", "Oceania", "Deportivo Oceania",
            "Bosque de Aragon", "Villa de Aragon", "Nezahualcoyotl",
            "Impulsora", "Rio de los Remedios", "Muzquiz",
            "Ecatepec", "Olimpica", "Plaza Aragon", "Ciudad Azteca"
        ]
        for i in range(len(lineaB) - 1):
            self.agregar_arista(lineaB[i], lineaB[i + 1])
        
        # LÍNEA 12 (Dorada) - Mixcoac a Tláhuac
        linea12 = [
            "Mixcoac", "Insurgentes Sur", "Hospital 20 de Noviembre",
            "Zapata", "Parque de los Venados", "Eje Central",
            "Ermita", "Mexicaltzingo", "Atlalilco", "Culhuacan",
            "San Andres Tomatlan", "Lomas Estrella", "Calle 11",
            "Periferico Oriente", "Tezonco", "Olivos", "Nopalera",
            "Zapotitlan", "Tlaltenco", "Tlahuac"
        ]
        for i in range(len(linea12) - 1):
            self.agregar_arista(linea12[i], linea12[i + 1])
    
    def obtener_vecinos(self, estacion):
        """Retorna las estaciones adyacentes a una estación dada"""
        return self.grafo.get(estacion, [])
    
    def obtener_estaciones(self):
        """Retorna todas las estaciones del metro"""
        return sorted(self.grafo.keys())
    
    def es_transbordo(self, estacion):
        """Verifica si una estación es transbordo (más de 2 conexiones)"""
        # Las estaciones de transbordo tienen más conexiones debido a múltiples líneas
        return len(self.grafo.get(estacion, [])) > 2
    
    def obtener_transbordos(self):
        """Retorna todas las estaciones de transbordo"""
        transbordos = []
        for estacion in self.grafo:
            if self.es_transbordo(estacion):
                transbordos.append(estacion)
        return sorted(transbordos)
    
    def mostrar_estacion(self, estacion):
        """Muestra información detallada de una estación"""
        if estacion in self.grafo:
            print(f"\nEstación: {estacion}")
            print(f"Conexiones adyacentes ({len(self.grafo[estacion])}):")
            for vecino in sorted(self.grafo[estacion]):
                print(f"  → {vecino}")
        else:
            print(f"Estación '{estacion}' no encontrada")





        