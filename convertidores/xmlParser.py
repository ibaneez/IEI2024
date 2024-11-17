import xml.etree.ElementTree as ET
# To modify - receiving any file
file = 'monumentos.xml'
tree = ET.parse(file)
root = tree.getroot()

for tipoMonumento in root.iter('tipoMonumento'):
    print(tipoMonumento.atrib)