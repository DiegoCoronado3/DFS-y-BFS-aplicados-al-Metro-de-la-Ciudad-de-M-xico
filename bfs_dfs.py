from collections import deque
from metro import MetroCDMX

class AlgoritmosBusqueda:
    def __init__(self, metro):
        self.metro = metro
        self.grafo = metro.grafo
    
    def bfs(self, origen, destino):
        """
        Búsqueda en Anchura (BFS - Breadth-First Search)
        
        Retorna:
            - ruta: lista ordenada de estaciones desde origen hasta destino
            - saltos: número de aristas (k-1 donde k es longitud de ruta)
            - nodos_expandidos: número de nodos visitados durante la búsqueda
        """
        if origen not in self.grafo:
            return None, 0, 0, f"Estación origen '{origen}' no existe"
        if destino not in self.grafo:
            return None, 0, 0, f"Estación destino '{destino}' no existe"
        
        if origen == destino:
            return [origen], 0, 1, "Origen y destino son iguales"
        
        # Estructuras de datos para BFS
        cola = deque([origen])
        visitados = {origen}
        padres = {origen: None}
        nodos_expandidos = 0
        
        encontrado = False
        
        # Búsqueda BFS
        while cola and not encontrado:
            actual = cola.popleft()
            nodos_expandidos += 1
            
            # Explorar vecinos
            for vecino in self.grafo[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = actual
                    cola.append(vecino)
                    
                    if vecino == destino:
                        encontrado = True
                        break
        
        # Reconstruir ruta
        if destino not in padres:
            return None, 0, nodos_expandidos, "No existe ruta"
        
        ruta = []
        actual = destino
        while actual is not None:
            ruta.append(actual)
            actual = padres[actual]
        ruta.reverse()
        
        saltos = len(ruta) - 1
        
        return ruta, saltos, nodos_expandidos, "Éxito"
    
    def dfs(self, origen, destino):
        """
        Búsqueda en Profundidad (DFS - Depth-First Search)
        
        Retorna:
            - ruta: lista ordenada de estaciones desde origen hasta destino
            - saltos: número de aristas (k-1 donde k es longitud de ruta)
            - nodos_expandidos: número de nodos visitados durante la búsqueda
        """
        if origen not in self.grafo:
            return None, 0, 0, f"Estación origen '{origen}' no existe"
        if destino not in self.grafo:
            return None, 0, 0, f"Estación destino '{destino}' no existe"
        
        if origen == destino:
            return [origen], 0, 1, "Origen y destino son iguales"
        
        # Estructuras de datos para DFS
        pila = [origen]
        visitados = {origen}
        padres = {origen: None}
        nodos_expandidos = 0
        
        encontrado = False
        
        # Búsqueda DFS
        while pila and not encontrado:
            actual = pila.pop()
            nodos_expandidos += 1
            
            # Explorar vecinos
            for vecino in self.grafo[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = actual
                    pila.append(vecino)
                    
                    if vecino == destino:
                        encontrado = True
                        break
        
        # Reconstruir ruta
        if destino not in padres:
            return None, 0, nodos_expandidos, "No existe ruta"
        
        ruta = []
        actual = destino
        while actual is not None:
            ruta.append(actual)
            actual = padres[actual]
        ruta.reverse()
        
        saltos = len(ruta) - 1
        
        return ruta, saltos, nodos_expandidos, "Éxito"


def imprimir_resultado(algoritmo, origen, destino, ruta, saltos, nodos_expandidos, estado):
    """Imprime el resultado de una búsqueda en formato estandarizado"""
    print(f"\n{'='*80}")
    print(f"ALGORITMO: {algoritmo}")
    print(f"Origen: {origen}")
    print(f"Destino: {destino}")
    print(f"{'='*80}")
    
    if ruta is None:
        print(f" Estado: {estado}")
        print(f"Nodos expandidos/visitados: {nodos_expandidos}")
    else:
        print(f" Estado: {estado}")
        print(f"\nRuta encontrada:")
        for i, estacion in enumerate(ruta):
            if i == 0:
                print(f"  {i+1}. {estacion} (ORIGEN)")
            elif i == len(ruta) - 1:
                print(f"  {i+1}. {estacion} (DESTINO)")
            else:
                print(f"  {i+1}. {estacion}")
        
        print(f"\n MÉTRICAS:")
        print(f"  • Longitud en aristas (saltos): {saltos}")
        print(f"  • Número de estaciones en la ruta: {len(ruta)}")
        print(f"  • Nodos expandidos/visitados: {nodos_expandidos}")



def ejecutar_pruebas_obligatorias():
    """Ejecuta los 3 casos de prueba obligatorios con BFS y DFS"""
    
    print("="*80)
    print(" PRUEBAS OBLIGATORIAS - ALGORITMOS BFS Y DFS")
    print(" Metro de la Ciudad de México")
    print("="*80)
    
    # Inicializar grafo
    metro = MetroCDMX()
    algoritmos = AlgoritmosBusqueda(metro)
    
    # Casos de prueba obligatorios
    casos_prueba = [
        ("Observatorio", "Ciudad Azteca"),
        ("Indios Verdes", "Velodromo"),
        ("UAM-I", "El Rosario")
    ]
    
    resultados_comparativos = []
    
    for i, (origen, destino) in enumerate(casos_prueba, 1):
        print(f"\n\n{'#'*80}")
        print(f"# CASO DE PRUEBA {i}: {origen} → {destino}")
        print(f"{'#'*80}")
        
        # Ejecutar BFS
        ruta_bfs, saltos_bfs, nodos_bfs, estado_bfs = algoritmos.bfs(origen, destino)
        imprimir_resultado("BFS", origen, destino, 
                          ruta_bfs, saltos_bfs, nodos_bfs, estado_bfs)
        
        # Ejecutar DFS
        ruta_dfs, saltos_dfs, nodos_dfs, estado_dfs = algoritmos.dfs(origen, destino)
        imprimir_resultado("DFS", origen, destino, 
                          ruta_dfs, saltos_dfs, nodos_dfs, estado_dfs)
        
        # Comparación
        print(f"\n{'─'*80}")
        print(f"COMPARACIÓN BFS vs DFS - Caso {i}")
        print(f"{'─'*80}")
        
        if ruta_bfs and ruta_dfs:
            print(f"Saltos BFS: {saltos_bfs} | Saltos DFS: {saltos_dfs}")
            print(f"Nodos expandidos BFS: {nodos_bfs} | Nodos expandidos DFS: {nodos_dfs}")
            
            if saltos_bfs < saltos_dfs:
                print(f" BFS encontró ruta más corta ({saltos_bfs} vs {saltos_dfs} saltos)")
            elif saltos_bfs > saltos_dfs:
                print(f" DFS encontró ruta más corta ({saltos_dfs} vs {saltos_bfs} saltos)")
            else:
                print(f" Ambos encontraron rutas de igual longitud ({saltos_bfs} saltos)")
            
            if nodos_bfs < nodos_dfs:
                print(f" BFS expandió menos nodos ({nodos_bfs} vs {nodos_dfs})")
            elif nodos_bfs > nodos_dfs:
                print(f" DFS expandió menos nodos ({nodos_dfs} vs {nodos_bfs})")
            else:
                print(f"  Ambos expandieron igual número de nodos ({nodos_bfs})")
            
            resultados_comparativos.append({
                'caso': f"{origen} → {destino}",
                'saltos_bfs': saltos_bfs,
                'saltos_dfs': saltos_dfs,
                'nodos_bfs': nodos_bfs,
                'nodos_dfs': nodos_dfs
            })
    
    # Resumen final
    print(f"\n\n{'='*80}")
    print(" RESUMEN COMPARATIVO DE TODOS LOS CASOS")
    print(f"{'='*80}\n")
    
    print(f"{'Caso':<40} {'Saltos BFS':<12} {'Saltos DFS':<12} {'Nodos BFS':<12} {'Nodos DFS':<12}")
    print(f"{'-'*40} {'-'*12} {'-'*12} {'-'*12} {'-'*12}")
    
    for resultado in resultados_comparativos:
        print(f"{resultado['caso']:<40} {resultado['saltos_bfs']:<12} "
              f"{resultado['saltos_dfs']:<12} {resultado['nodos_bfs']:<12} "
              f"{resultado['nodos_dfs']:<12}")
    
def modo_interactivo(algoritmos):
    """Permite al usuario ingresar origen y destino manualmente"""
    while True:
        print("\n" + "="*50)
        print(" MODO INTERACTIVO - METRO CDMX")
        print("="*50)
        print("Escribe el nombre exacto de la estación (o 'salir' para volver).")
        
        origen = input("\nEstación Origen: ").strip()
        if origen.lower() == 'salir': break
        
        destino = input("Estación Destino: ").strip()
        if destino.lower() == 'salir': break

        # Validación rápida antes de correr algoritmos
        if origen not in algoritmos.grafo:
            print(f"Error: La estación '{origen}' no existe en la base de datos.")
            print("   (Verifica mayúsculas y/ ortografia, ej: 'Indios Verdes', 'UAM-I')")
            continue
        if destino not in algoritmos.grafo:
            print(f"Error: La estación '{destino}' no existe en la base de datos.")
            continue

        print(f"\nCalculando ruta de {origen} a {destino}...")

        # Ejecutar BFS
        ruta_bfs, saltos_bfs, nodos_bfs, estado_bfs = algoritmos.bfs(origen, destino)
        imprimir_resultado("BFS", origen, destino, ruta_bfs, saltos_bfs, nodos_bfs, estado_bfs)

        # Ejecutar DFS
        ruta_dfs, saltos_dfs, nodos_dfs, estado_dfs = algoritmos.dfs(origen, destino)
        imprimir_resultado("DFS", origen, destino, ruta_dfs, saltos_dfs, nodos_dfs, estado_dfs)


         # Comparación
        print(f"\n{'─'*80}")
        print(f"COMPARACIÓN BFS vs DFS")
        print(f"{'─'*80}")
        
        if ruta_bfs and ruta_dfs:
            
            if saltos_bfs < saltos_dfs:
                print(f" BFS encontró ruta más corta ({saltos_bfs} vs {saltos_dfs} saltos)")
            elif saltos_bfs > saltos_dfs:
                print(f" DFS encontró ruta más corta ({saltos_dfs} vs {saltos_bfs} saltos)")
            else:
                print(f" Ambos encontraron rutas de igual longitud ({saltos_bfs} saltos)")
            
            if nodos_bfs < nodos_dfs:
                print(f" BFS expandió menos nodos ({nodos_bfs} vs {nodos_dfs})")
            elif nodos_bfs > nodos_dfs:
                print(f" DFS expandió menos nodos ({nodos_dfs} vs {nodos_bfs})")
            else:
                print(f"  Ambos expandieron igual número de nodos ({nodos_bfs})")
        

        input("\nPresiona Enter para continuar...")

def menu_principal():
    metro = MetroCDMX()
    algoritmos = AlgoritmosBusqueda(metro)

    while True:
        print("\n" + "#"*50)
        print(" METRO CDMX")
        print("#"*50)
        print("1. Ejecucion de pruebas obligatorias")
        print("2. Ingresar Origen y Destino")
        print("3. Ver lista de todas las estaciones")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción (1-4): ")

        if opcion == '1':
            ejecutar_pruebas_obligatorias() 
            input("\nPruebas finalizadas. Presiona Enter para volver al menú.")
            
        elif opcion == '2':
            modo_interactivo(algoritmos)
            
        elif opcion == '3':
            print("\n--- ESTACIONES DISPONIBLES ---")
            estaciones = metro.obtener_estaciones()
            for i, est in enumerate(estaciones):
                print(f"{est:<30}", end="\n" if (i+1) % 3 == 0 else "")
            print("\n")
            input("Presiona Enter para continuar...")
            
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()

