import xml.etree.ElementTree as ET
import json

# To modify - receiving any file
file = 'datos/monumentos.xml'
tree = ET.parse(file)
root = tree.getroot()

with open('datos/CLEdata.json', 'w', encoding='utf-8') as f:

    for monumento in root.iter('monumento'):
        coords = monumento.find('coordenadas')
        provincia = 'null'
        localidad = 'null'

        poblacion = monumento.find('poblacion')
        if poblacion is not None:
            localidad = poblacion.find('localidad').text
            provincia = poblacion.find('provincia').text

        calle = monumento.find('calle')
        if calle is not None :
            calle = calle.text

        codpost = monumento.find('codigoPostal')
        if codpost is not None :
            codpost = codpost.text

        descripcion = monumento.find('Descripcion')
        if descripcion is not None :
            descripcion = descripcion.text

        item = {
            "name" : monumento.find('nombre').text,
            "type" : monumento.find('tipoMonumento').text,
            "address" : calle,
            "postal code" : codpost,
            "longitude" : coords.find('longitud').text,
            "latitude" : coords.find('latitud').text,
            "description" : descripcion,
            "localName" : localidad,
            "provinceName" : provincia
        }
        json.dump(item, f, ensure_ascii=False, indent=4)


    
