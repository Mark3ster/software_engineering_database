from database import crear_tabla, guardar_preferencia, obtener_preferencias


crear_tabla()

guardar_preferencia(1, "tema", "oscuro")
guardar_preferencia(1, "idioma", "español")
guardar_preferencia(1, "notificaciones", "activadas")

preferencias = obtener_preferencias(1)

print("Preferencias del usuario 1:")

for preferencia in preferencias:
    print(preferencia[0], ":", preferencia[1])

