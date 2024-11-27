class ComunitatValenciana:
    def __init__(self, igpcv, denominacion, provincia, municipio, utmeste, utmnorte, codclasificacion, clasificacion, codcategoria, categoria):
        self.igpcv = igpcv
        self.denominacion = denominacion
        self.provincia = provincia
        self.municipio = municipio
        self.utmeste = utmeste
        self.utmnorte = utmnorte
        self.codclasificacion = codclasificacion
        self.clasificacion = clasificacion
        self.codcategoria = codcategoria
        self.categoria = categoria

def leer_csv(file_path):
    lista = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines[1:]:  # Saltar la primera línea (encabezado)
                partes = line.strip().split(";")
                if len(partes) == 10:
                    comunitat = ComunitatValenciana(
                        partes[0].replace('"', ""),
                        partes[1].replace('"', ""),
                        partes[2].replace('"', ""),
                        partes[3].replace('"', ""),
                        partes[4].replace('"', ""),
                        partes[5].replace('"', ""),
                        partes[6].replace('"', ""),
                        partes[7].replace('"', ""),
                        partes[8].replace('"', ""),
                        partes[9].replace('"', "")
                    )
                    lista.append(comunitat)
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    return lista


def generar_json(lista, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("[\n")
            for i, comunitat in enumerate(lista):
                data = comunitat.to_dict()
                json_entry = "  {\n"
                json_entry += ",\n".join([f'    "{key}": "{value}"' for key, value in data.items()])
                json_entry += "\n  }"
                if i < len(lista) - 1:
                    json_entry += ","
                json_entry += "\n"
                file.write(json_entry)
            file.write("]\n")
        print("El archivo JSON ha sido generado con éxito.")
    except Exception as e:
        print(f"Error al escribir el archivo JSON: {e}")


if __name__ == "__main__":
    carpeta = "C:/Users/usuario/Documents/00 Universidad/GII 24-25/A - IEI - Integración e interoperabilidad/Laboratorio/"
    original = carpeta + "bienes_inmuebles_interes_cultural.csv"
    archivo_json = carpeta + "ComunitatValenciana.json"

    lista = leer_csv(original)
    generar_json(lista, archivo_json)
