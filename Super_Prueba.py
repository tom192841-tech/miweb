### El Motor de Suscripiciones Saas###

usuarios = [
    {"nombre": "Brais", "plan": "Premium", "precio_base": 49.99, "cupon": "MOURE20", "activo": True},
    {"nombre": "Alan", "plan": "Basic", "precio_base": 19.99, "cupon": None, "activo": True},
    {"nombre": "Facundo", "plan": "Premium", "precio_base": 49.99, "cupon": "INVALIDO", "activo": False},
    {"nombre": "Matias", "plan": "Enterprise", "precio_base": 199.99, "cupon": "PRO50", "activo": True},
]

CUPONES = {
    "MOURE20":lambda valor: valor - (valor * 20) / 100,
    "PRO50":lambda valor: valor - (valor * 50) / 100,
}

def procesar_facturacion(lista_usuarios):
    # 2. Hacé el filtro acá usando List Comprehension, and, y operadores de comparación
    usuarios_filtrados = [user for user in lista_usuarios if user["activo"] == True and user["precio_base"] > 20]
    reporte_final = []
    
    # 3. Recorré los usuarios filtrados
    for usuario in usuarios_filtrados:
        precio_final = usuario["precio_base"] 
        # 4. Bloque try-except para procesar cupones
        try:
            if usuario["cupon"] is not None:
                cupon:str = usuario["cupon"]
                precio_final = CUPONES[cupon](precio_final)
        except KeyError:
            print(f"⚠ Cupón '{usuario['cupon']}' inválido para {usuario['nombre']}. Se cobrará tarifa completa.")
        precio_final += ((precio_final * 21) / 100)
        precio_final = round(precio_final, 2)
        reporte_final.append({"nombre": usuario["nombre"], "total_a_pagar": precio_final})
        
    return reporte_final

# --- BLOQUE DE PRUEBA ---
usuarios = [
    {"nombre": "Brais", "plan": "Premium", "precio_base": 49.99, "cupon": "MOURE20", "activo": True},
    {"nombre": "Alan", "plan": "Basic", "precio_base": 19.99, "cupon": None, "activo": True},
    {"nombre": "Facundo", "plan": "Premium", "precio_base": 49.99, "cupon": "INVALIDO", "activo": False},
    {"nombre": "Matias", "plan": "Enterprise", "precio_base": 199.99, "cupon": "PRO50", "activo": True},
]

print("--- Iniciando Procesamiento de Facturación SaaS ---")
resultado = procesar_facturacion(usuarios)

print("\n--- REPORTE DE COBROS GENERADO ---")
print(resultado)