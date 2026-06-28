class Personaje:
    # 1. Definí acá tu constructor __init__
    def __init__(self, nombre, profesion, vida):
        self.nombre = nombre
        self.profesion = profesion
        self.vida = vida
    # 2. Desarrollá los métodos acá abajo
    
    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:return print("Estas Muerto")
        print(f"Has sufrido {cantidad} de daño")
    def curar(self, cantidad):
        self.vida += cantidad
        if self.vida <= 0:return print("Estas Muerto")
        return print(f"Te has curado {cantidad} de vida")
    
    def mostrar_estado(self):
        if self.vida <= 0:return print("Estas Muerto")
        return print(f"Estado Actual: N:{self.nombre}, P:{self.profesion}, HP:{self.vida},Vivo:Si")


# --- Bloque de Prueba ---
# Creamos un personaje (instanciación)
heroe = Personaje("Aragorn", "Guerrero", 100)

print("--- Estado Inicial ---")
heroe.mostrar_estado()

print("\n--- ¡El héroe entra en combate! ---")
heroe.recibir_daño(40)
heroe.mostrar_estado()

print("\n--- Usando una poción de curación ---")
heroe.curar(20)
heroe.mostrar_estado()

print("\n--- Ataque crítico fulminante ---")
heroe.recibir_daño(90) # Debería dejarlo en 0 de vida y esta_vivo = False
heroe.mostrar_estado()

print("\n--- Intentando revivirlo con curación básica ---")
heroe.curar(10) # No debería dejarlo curarse porque ya cayó en combate