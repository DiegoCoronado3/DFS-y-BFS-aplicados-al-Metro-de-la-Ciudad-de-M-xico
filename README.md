# DFS-y-BFS-aplicados-al-Metro-de-la-Ciudad-de-Mexico

**Búsqueda en Grafos: BFS y DFS aplicados al Metro CDMX** **Materia:** Inteligencia Artificial  
**Alumno:** Diego Coronado Pérez  
**Grupo:** 10  
**Universidad:** Facultad de Ingeniería, UNAM  

---

### 📂 Estructura de archivos:

* `metro.py`: Contiene la clase `MetroCDMX` que modela la topología de las 12 líneas del metro mediante una lista de adyacencia (diccionarios).
* `bfs_dfs.py`: Script principal que contiene la clase `AlgoritmosBusqueda` con la lógica de BFS/DFS y la interfaz de usuario por consola.

---

## 🛠 Lenguaje y Versión

* **Lenguaje:** Python
* **Versión:** Python 3.8 o superior.
* **Dependencias:** El proyecto utiliza exclusivamente la biblioteca estándar de Python (específicamente `collections.deque` para optimizar las operaciones de la cola en BFS). No requiere la instalación de paquetes de terceros ni entornos virtuales.

---

## 🚀 Cómo compilar y ejecutar

**1. Clona el repositorio:**
```bash

```

**2. Entra al directorio del proyecto:**
```bash

```

**3. Ejecuta el archivo principal:**
```bash
python bfs_dfs.py
```

---

## 🚇 Cómo correr los 3 casos obligatorios

Para facilitar la revisión de la tarea, el programa incluye una opción automatizada que ejecuta los casos requeridos sin necesidad de teclear las estaciones.

Una vez que hayas ejecutado el archivo `bfs_dfs.py` y veas el menú principal en tu pantalla:

1. Selecciona la **Opción 1** (`1. Ejecucion de pruebas obligatorias`) y presiona **Enter**.
2. El sistema calculará e imprimirá automáticamente los resultados, comparando BFS y DFS para las siguientes rutas:
   * **Caso 1:** Observatorio → Ciudad Azteca
   * **Caso 2:** Indios Verdes → Velódromo
   * **Caso 3:** UAM-I → El Rosario

Para cada caso, la consola mostrará la ruta detallada, la longitud en aristas (saltos), y el número de nodos expandidos, finalizando con una tabla de resumen comparativo global.

> **💡 Nota:** Si deseas probar otras rutas libremente, puedes usar la **Opción 2** del menú para ingresar manualmente cualquier origen y destino o bien si quieres ver todas las estaciones del metro puedes usar la **Opción 3** del menú y para finalizar el programa puedes usar la **Opción 4**.
