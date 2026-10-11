import os

PREFERENCIAS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "preferencias.txt")


def set_preferencia(usuario_id, clave, valor):
    preferencias = []

    try:
        with open(PREFERENCIAS_PATH, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")

                if len(datos) == 3:
                    if datos[0] == str(usuario_id) and datos[1] == clave:
                        continue

                    preferencias.append(linea.strip())
    except FileNotFoundError:
        pass

    with open(PREFERENCIAS_PATH, "w", encoding="utf-8") as archivo:
        for preferencia in preferencias:
            archivo.write(preferencia + "\n")

        archivo.write(f"{usuario_id}|{clave}|{valor}\n")


def get_preferencia(usuario_id, clave):
    try:
        with open(PREFERENCIAS_PATH, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")

                if len(datos) == 3 and datos[0] == str(usuario_id) and datos[1] == clave:
                    return datos[2]
    except FileNotFoundError:
        pass

    return None


def delete_preferencia(usuario_id, clave):
    preferencias = []

    try:
        with open(PREFERENCIAS_PATH, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")

                if len(datos) == 3:
                    if datos[0] == str(usuario_id) and datos[1] == clave:
                        continue

                    preferencias.append(linea.strip())
    except FileNotFoundError:
        print("El archivo preferencias.txt no existe")
        return

    with open(PREFERENCIAS_PATH, "w", encoding="utf-8") as archivo:
        for preferencia in preferencias:
            archivo.write(preferencia + "\n")