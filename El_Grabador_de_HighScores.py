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
                nombre = datos[0]
                puntos = datos[1]
                print(f"👤 {nombre} ---- 🏆 {puntos} pts")
    except FileNotFoundError:
        print("Aún no hay puntuaciones registradas.")


# --- Bloque de Prueba ---
# (Esto borra el archivo viejo antes de empezar para que no se dupliquen en cada prueba)
if os.path.exists("puntuaciones.txt"):
    os.remove("puntuaciones.txt")

print("--- Intentando leer sin datos previos ---")
mostrar_podio() 

print("\n--- Guardando puntuaciones de la partida ---")
guardar_puntuacion("Aragorn", 1500)
guardar_puntuacion("Gandalf", 2800)
guardar_puntuacion("Legolas", 1950)
print("¡Datos guardados con éxito!")

print("\n--- Mostrando el Podio Actual ---")
mostrar_podio()