from database import set_preferencia, get_preferencia, delete_preferencia


set_preferencia(1, "tema", "oscuro")
set_preferencia(1, "idioma", "español")
set_preferencia(1, "notificaciones", "activadas")

print("Tema:")
print(get_preferencia(1, "tema"))

print("Idioma:")
print(get_preferencia(1, "idioma"))

delete_preferencia(1, "idioma")

print("Idioma después de borrarlo:")
print(get_preferencia(1, "idioma"))