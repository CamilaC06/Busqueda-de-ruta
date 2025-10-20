# Busqueda-de-ruta

¿Qué es?

Funciona como una calculadora de rutas en un mapa bidimensional.
El mapa se representa con una matriz donde cada celda puede ser:
- 0: camino libre
- 1: edificio
- 2: agua
- 3: bloque temporal

El usuario puede ingresar coordenadas de inicio y fin válidas.
Se permite agregar obstáculos manualmente antes de empezar.
Los obstáculos temporales se mueven cada cierto tiempo y la ruta se recalcula automáticamente.
Se visualiza el mapa en consola:
- "." camino libre
- "X" obstáculos
- "*" ruta encontrada

Utilicé BFS (Breadth-First Search / búsqueda en amplitud) para encontrar la ruta más corta.
BFS recorre el mapa expandiendo los nodos vecinos hasta llegar al destino, evitando obstáculos y visitando cada celda una sola vez.
Cada vez que se mueve un bloque temporal, la ruta se recalcula dinámicamente.

Aprendizajes:
- Cómo representar un mapa en Python con matrices.
- Cómo validar coordenadas y entradas del usuario para evitar errores.
- Cómo implementar BFS para rutas más cortas en un entorno dinámico, considerando cambios en tiempo real.
- La importancia de estructuras de datos como deque y sets para eficiencia en búsquedas.
- Cómo combinar lógica de juego + visualización CLI de forma clara y dinámica.
