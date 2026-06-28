def procesar_registro(datos_crudos):
    try:
        # 1. Separamos por comas
        partes = datos_crudos.split(",")
        
        # Si faltan datos, al intentar acceder a partes[2] Python lanzará IndexError automáticamente.
        # Limpiamos los espacios en blanco de cada parte individualmente:
        nombre = partes[0].strip()
        edad_texto = partes[1].strip()
        correo = partes[2].strip()
        
        # 2. Intentamos convertir la edad (si falla, salta a ValueError)
        edad = int(edad_texto)
        
        # 3. Validamos el correo
        if "@" not in correo: 
            print("Error: El correo no es válido.")
            return # Cortamos la función para que no imprima el éxito
            
        # 4. Si todo salió bien
        print(f"¡Usuario {nombre} (Edad: {edad}) registrado con éxito con el correo {correo}!")
        
    except ValueError:
        print("Error: La edad debe ser un número válido.")
    except IndexError:
        print("Error: Faltan datos en el registro.")

# --- Casos de Prueba ---
print("--- Caso 1: Todo correcto ---")
procesar_registro("  Brais Moure , 25 , moure@dev.com  ") 

print("\n--- Caso 2: Edad mal ingresada ---")
procesar_registro("Juan Pérez, veinticinco, juan@correo.com")

print("\n--- Caso 3: Faltan datos (sin comas suficientes) ---")
procesar_registro("Ana Gómez, ana@correo.com")

print("\n--- Caso 4: Correo sin arroba ---")
procesar_registro("Luis Torres, 30, luistorres.com")