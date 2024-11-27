def validar_ComunitatValenciana(id, igpcv, denominacion, provincia, municipio, utmeste, utmnorte, codclasificacion, clasificacion, codcategoria, categoria):
    if not denominacion == "" and not provincia == "" and not municipio == "" and not utmeste == "" and not utmnorte == "":
        if (not codclasificacion == "" or not clasificacion == "") and not (not codclasificacion == "" and not clasificacion == ""):
            return 1
        else:
            # Imprimir que el elemento 'id' no es válido porque le falta la clasificación
            print(f"El elemento con ID {id} no es válido porque le falta la clasificación.")
            return 0
    else:
        # Imprimir que el elemento 'id' no es válido porque le falta algún atributo necesario
        campos_faltantes = []
        if denominacion == "":
            campos_faltantes.append("denominación")
        if provincia == "":
            campos_faltantes.append("provincia")
        if municipio == "":
            campos_faltantes.append("municipio")
        if utmeste == "":
            campos_faltantes.append("utmeste")
        if utmnorte == "":
            campos_faltantes.append("utmnorte")
        
        # Mostrar los campos faltantes
        print(f"El elemento con ID {id} no es válido porque le falta(n) los siguientes campo(s): {', '.join(campos_faltantes)}.")
        return 0
