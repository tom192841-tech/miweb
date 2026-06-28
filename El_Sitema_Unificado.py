import os

def guardar_puntuacion(nombre_personaje, puntos):
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"{nombre_personaje},{puntos}\n")

def mostrar_podio():
    try:
        with open("puntuaciones.txt", "r") as archivo:
            print("--- PODIO DE HIGHSCORES ---")
            for linea in archivo:
                linea_limpia = linea.strip()
                datos = linea_limpia.split(",")
                print(f"👤 {datos[0]} ---- 🏆 {datos[1]} pts")
    except FileNotFoundError:
        print("Aún no hay puntuaciones registradas.")

# ---------------------------------------------------------
# ✍️ TU NUEVA FUNCIÓN ACÁ
def filtrar_y_registrar(lista_jugadores):
    for user in lista_jugadores:
        if user["puntos"] > 0:
            guardar_puntuacion(user["nombre"],user["puntos"])
            mostrar_podio()
        

# --- Bloque de Prueba ---
if os.path.exists("puntuaciones.txt"):
    os.remove("puntuaciones.txt")

jugadores = [
    {"nombre": "Frodo", "puntos": 500},
    {"nombre": "Sam", "puntos": 1200},
    {"nombre": "Gollum", "puntos": -50},
    {"nombre": "Gimli", "puntos": 0},
    {"nombre": "Boromir", "puntos": 850}
]

print("--- Procesando Partida ---")
filtrar_y_registrar(jugadores)