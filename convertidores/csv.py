# dado un archivo csv se devuelve una lista de líneas 
def dividir_csv_en_lineas():
    with open('../database/t.csv', 'r') as f:
        results = []
        for line in f:
                words = line.strip.split(';')
                results.append(words)
        print(results)
#Dada una línea del csv devuelve un map clave valor de los componentes
def extractor_componentes_desde_linea():
    print("hola")

# Dado el tipo del monumento se convierte a uno de los prediseñados por el esquema de datos
def convertidor_tipo_monumento():
    print("hola")