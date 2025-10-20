#Escape en coordenadas
import random
import time
from collections import deque


#Crear un mapa bidimensional modificable
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
mapa = [[0 for i in range(columnas)]for j in range(filas)]

#Definir obstáculos y camino libre
camino_libre = 0
edificio = 1
agua = 2
bloque_temporal = 3

obstaculos = []

def mostrar_mapa():
    for fila in mapa:
        fila_str = ""
        for celda in fila:
            if celda == 0:       # camino libre
                fila_str += ". "
            elif celda == 9:     # ruta
                fila_str += "* "
            else:                # cualquier obstáculo
                fila_str += "X "
        print(fila_str)
    print()


#lista de coordenadas del mapa
def coordenadas_libres():
    return [
    (i, j)
    for i in range(filas)
    for j in range(columnas)
    if mapa[i][j] == camino_libre
]

#colocar obstaculos aleatorios
def colocar_obstaculo(valor, cantidad):
    libres = coordenadas_libres()
    for a in range(cantidad):
        if not libres:
            break
        coord_aleat = random.choice(libres)
        fila,columna = coord_aleat
        mapa[fila][columna] = valor
        obstaculos.append((fila,columna,valor))
        libres.remove(coord_aleat)

#mover obstaculo temporal
def cambiar_obstaculo_temp():
    #delimitar a solo bloques temporales
    obstaculos_temp = [
        (i, j) 
        for i, j, k in obstaculos
        if k == bloque_temporal
        ]
    
    for  i,j in obstaculos_temp:
            print(f"obstaculo temporal en {i,j}")
            time.sleep(1)

            #borrar obstaculo 
            mapa [i][j] = camino_libre
            obstaculos.remove((i,j,bloque_temporal))

            #colocar nuevo obstáculo
            colocar_obstaculo(bloque_temporal,len(obstaculos_temp))
            print("Mapa actualizado")
            mostrar_mapa()
            
            
#recorrer
def buscar_ruta(inicio, fin):
    movimientos = [(-1,0), (1,0), (0,-1), (0,1)]
    visitados = set()
    queue = deque([(inicio, [inicio])])
    
    while queue:
        (x,y), camino = queue.popleft()
        
        if (x,y) == fin:
            return camino
            
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas:
                if mapa[nx][ny] == camino_libre and (nx, ny) not in visitados:
                    visitados.add((nx, ny))
                    queue.append(((nx, ny), camino + [(nx, ny)]))
    print("No se encontro una ruta")
    return None

def pedir_coords():
    while True:
        coords_inicio = tuple(map(int, input("Ingrese las coordenadas de inicio (x,y): ").split(",")))
        if not (0 <= coords_inicio[0] < filas and 0 <= coords_inicio[1] < columnas):
            print("La coordenada de inicio no es válida. Intenta de nuevo")    
            continue
        
        if mapa[coords_inicio[0]][coords_inicio[1]] != camino_libre:
            print("La coordenada de inicio tiene un obstáculo. Intenta de nuevo")
            continue
        break
        
    while True:
        coords_fin = tuple(map(int, input("Ingrese las coordenadas de fin (x,y): ").split(",")))
        if not (0 <= coords_fin[0] < filas and 0 <= coords_fin[1] < columnas):
            print("La coordenada de fin no es válida. Intenta de nuevo")
            continue
        if mapa[coords_fin[0]][coords_fin[1]] != camino_libre:
            print("La coordenada de fin tiene un obstáculo. Intenta de nuevo")
            continue
        break
    
    return coords_inicio, coords_fin


def agregar_obstaculos_usuario():
    while True:
        entrada = input("Ingresa las coordenadas del obstáculo (x,y) o '.' para terminar: ")
        if entrada == ".":
            break
        try:
            x, y = map(int, entrada.split(","))
            if 0 <= x < filas and 0 <= y < columnas and mapa[x][y] == camino_libre:
                mapa[x][y] = 1  # edificio 
            else:
                print("Coordenadas inválidas u ocupadas.")
        except:
            print("Formato incorrecto, usa x,y")


#colocar obstáculos en el mapa
colocar_obstaculo(edificio, 3)
colocar_obstaculo(agua, 2)
colocar_obstaculo(bloque_temporal, 2)

print("Mapa Inicial")
mostrar_mapa()

#permitir al usuario agregar obstáculos
agregar_obstaculos_usuario()
print("Mapa final antes de iniciar:")
mostrar_mapa()



inicia, finaliza = pedir_coords()      
juego_terminado = False  
        
while not juego_terminado:
    ruta = buscar_ruta(inicia, finaliza)
        
    if ruta:
        print("Mostrando la ruta con '*'")
        for x, y in ruta:
            mapa[x][y] = 9
        mostrar_mapa()  
        juego_terminado = True
    else:
        cambiar_obstaculo_temp()
        time.sleep(2)

print("Ruta encontrada!")