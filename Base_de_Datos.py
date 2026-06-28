inventario = [
    {"id": 1, "nombre": "PC", "precio": 90, "cantidad": 2, "categoria": "Tecnologia"},
    {"id": 2, "nombre": "TV", "precio": 799.99, "cantidad": 5, "categoria": "Tecnologia"},
    {"id": 3, "nombre": "Jabon", "precio": 5, "cantidad": 10, "categoria": "Limpieza"},
    {"id": 4, "nombre": "Juguete", "precio": 20, "cantidad": 7, "categoria": "Juguetes"},
    {"id": 5, "nombre": "Afiche", "precio": 10, "cantidad": 20, "categoria": "Papeleria"},
]

def obtener_categorias(lista_inventario):
    categories = set()
    for obj in lista_inventario:
        categories.add(obj["categoria"])
    return categories

def filtrar_por_precio(lista_inventario, precio_maximo):
    lista_filtrada = []
    for obj in lista_inventario:
        if obj["precio"] <= precio_maximo:
            lista_filtrada.append(obj) 
    return lista_filtrada

def actualizar_stock(lista_inventario, id_producto, cantidad_vendida):
    for obj in lista_inventario:
        if obj["id"] == id_producto:
            # ¡Lo encontramos! Ahora validamos stock
            if obj["cantidad"] >= cantidad_vendida:
                obj["cantidad"] -= cantidad_vendida # Restamos el stock real
                print(f"¡Venta exitosa! Stock restante de {obj['nombre']}: {obj['cantidad']}")
                return # Cortamos la función porque ya cumplió su objetivo
            else:
                print(f"No hay stock suficiente de {obj['nombre']}. Desea llevar menos?")
                return
                
    # Si el bucle termina y nunca entró al 'if obj["id"] == id_producto', significa que no existe
    print(f"Error: El producto con ID {id_producto} no existe.")

# --- Pruebas ---
print("Categorías únicas:", obtener_categorias(inventario))
print("Productos baratos:", filtrar_por_precio(inventario, 50.0))

print("\n--- Simulando Ventas ---")
actualizar_stock(inventario, 1, 2)  # Debería restar stock con éxito
actualizar_stock(inventario, 2, 10) # Debería avisar que no hay stock suficiente
actualizar_stock(inventario, 99, 1) # Debería avisar que no existe el ID