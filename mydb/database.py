def set_preferencia(usuario_id, clave, valor):
    preferencias = []

    try:
        archivo = open("preferencias.txt", "r")

        for linea in archivo:
            datos = linea.strip().split("|")

            if len(datos) == 3:
                if datos[0] == str(usuario_id) and datos[1] == clave:
                    continue

                preferencias.append(linea.strip())

        archivo.close()

    except FileNotFoundError:
        pass

    archivo = open("preferencias.txt", "w")

    for preferencia in preferencias:
        archivo.write(preferencia + "\n")

    archivo.write(str(usuario_id) + "|" + clave + "|" + valor + "\n")

    archivo.close()


def get_preferencia(usuario_id, clave):
    try:
        archivo = open("preferencias.txt", "r")

        for linea in archivo:
            datos = linea.strip().split("|")

            if len(datos) == 3:
                if datos[0] == str(usuario_id) and datos[1] == clave:
                    archivo.close()
                    return datos[2]

        archivo.close()

    except FileNotFoundError:
        pass

    return None


def delete_preferencia(usuario_id, clave):
    preferencias = []

    try:
        archivo = open("preferencias.txt", "r")

        for linea in archivo:
            datos = linea.strip().split("|")

            if len(datos) == 3:
                if datos[0] == str(usuario_id) and datos[1] == clave:
                    continue

                preferencias.append(linea.strip())

        archivo.close()

    except FileNotFoundError:
        return

    archivo = open("preferencias.txt", "w")

    for preferencia in preferencias:
        archivo.write(preferencia + "\n")

    archivo.close()