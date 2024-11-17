

| INTEGRACIÓN E INTEROPERABILIDAD. CURSO 2024-25 |  |
| :---- | :---- |
| PLANTILLA DE DEFINICIÓN DE *MAPPING* SEMÁNTICO | Equipo de prácticas: 21.04 |

**Esquema origen:** EUS 

M \= Monumento  
L \= Localidad  
P \= Provincia

| Dato esquema global | Dato(s) esquema origen  | Transformación(es) | Comentarios |
| :---- | :---- | :---- | :---- |
| M.nombre | documentName | Copiar |  |
| M.tipo \= “Yacimiento arqueológico” | documentName  | Convertir |  |
| M.tipo \= “Iglesia-Ermita” | documentName | Convertir |  |
| M.tipo \= “Monasterio-Convento” | documentName | Convertir |  |
| M.tipo \= “Castillo-Fortaleza-Torre” | documentName | Convertir |  |
| M.tipo \= “Edificio Singular” | documentName | Convertir |  |
| M.tipo \= “Puente” | documentName | Convertir |  |
| M.tipo \= “Otros” | documentName | Convertir |  |
| M.dirección | address | Copiar |  |
| M.codigo\_postal | postalCode | Copiar |  |
| M.longitud | lonwgs84 | Copiar |  |
| M.latitud | latwgs84 | Copiar |  |
| M.descripcion | documentDescription | Copiar |  |
| L.codigo | municipalityCode | Copiar |  |
| L.nombre | municipalityName | Copiar |  |
| P.codigo | terrritorycode | Copiar |  |
| P.nombre | territory | Copiar |  |

**Esquema origen:** CLE 

M \= Monumento  
L \= Localidad  
P \= Provincia

| Dato esquema global | Dato(s) esquema origen  | Transformación(es) | Comentarios |
| :---- | :---- | :---- | :---- |
| M.nombre | nombre | Copiar |  |
| M.tipo \= “Yacimiento arqueológico” | tipoMonumento=”Yacimientos arqueológicos”   | Convertir |  |
| M.tipo \= “Iglesia-Ermita” | tipoMonumento=”Iglesias y Ermitas”  tipoMonumento=”Catedrales” tipoMonumento=”Sinagogas” | Convertir |  |
| M.tipo \= “Monasterio-Convento” | tipoMonumento=”Monasterios”  tipoMonumento=”Santuarios” | Convertir |  |
| M.tipo \= “Castillo-Fortaleza-Torre” | tipoMonumento=”Castillos” tipoMonumento=”Casas Nobles”  tipoMonumento=”Torres” | Convertir |  |
| M.tipo \= “Edificio Singular” | tipoMonumento=”Reales Sitios”  tipoMonumento=”Palacio” tipoMonumento=”Casa consistorial” | Convertir |  |
| M.tipo \= “Puente” | tipoMonumento=”Puente”  | Convertir |  |
| M.tipo \= “Otros” | tipoMonumento=”Plazas Mayores” tipoMonumento=”Molinos” tipoMonumento=”Hórreos” tipoMonumento=”Murallas y puertas” tipoMonumento=”Esculturas” tipoMonumento=”Otros edificios” tipoMonumento=”Conjunto Etnológico” tipoMonumento=”Paraje Pintoresco” | Convertir |  |
| M.dirección | calle | Copiar |  |
| M.codigo\_postal | codigoPostal | Copiar |  |
| M.longitud | longitud | Copiar |  |
| M.latitud | latitud | Copiar |  |
| M.descripcion | descripcion | Copiar |  |
| L.codigo |  | Auto-asignado |  |
| L.nombre | localidad | Copiar |  |
| P.codigo |  | Auto-asignado |  |
| P.nombre | provincia | Copiar |  |

**Esquema origen:** CV

M \= Monumento  
L \= Localidad  
P \= Provincia

| Dato esquema global | Dato(s) esquema origen  | Transformación(es) | Comentarios |
| :---- | :---- | :---- | :---- |
| M.nombre | DENOMINACION | Copiar |  |
| M.tipo \= “Yacimiento arqueológico” | CATEGORIA=“Zona arqueológica”, “Zona paleontológica”  | Convertir |  |
| M.tipo \= “Iglesia-Ermita” | (DENOMINACION.contains(“Iglesia”) || DENOMINACION.contains(“Ermita”)) && CATEGORIA=“Monumento” | Convertir |  |
| M.tipo \= “Monasterio-Convento” | (DENOMINACION.contains(“Monasterio”) || DENOMINACION.contains(“Convento”)) && CATEGORIA=“Monumento” | Convertir |  |
| M.tipo \= “Castillo-Fortaleza-Torre” | CATEGORIA=“Monumento”, “Zona arqueológica” | Convertir |  |
| M.tipo \= “Edificio Singular” | \- |  |  |
| M.tipo \= “Puente” | CATEGORIA=”Monumento” |  |  |
| M.tipo \= “Otros” | CATEGORIA="Conjunto histórico", "Sitio histórico", "Jardín histórico", "Archivo", "Espacio etnológico", "Parque cultural", "Monumento de interés local", "Fondo de museo (primera)",”Individual (mueble)”, “” | Convertir |  |
| M.dirección | UTMESTE, UTMNORTE | Convertir |  |
| M.codigo\_postal | UTMESTE, UTMNORTE | Convertir |  |
| M.longitud | UTMESTE | Convertir |  |
| M.latitud | UTMNORTE | Convertir |  |
| M.descripcion | DENOMINACION | Copiar \- \-  |  |
| L.codigo | \- |  |  |
| L.nombre | MUNICIPIO | Copiar |  |
| P.codigo | \- |  |  |
| P.nombre | PROVINCIA | Copiar |  |

