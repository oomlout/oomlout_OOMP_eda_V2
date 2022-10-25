
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "DB25_Male_MountingHoles"
    hexID = "SZKCNDB25MALEHOLS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'DB25_Male_MountingHoles', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'male D-SUB connector', 'kicadSymbolki_description': '25-pin male D-SUB connector, Mounting Hole', 'kicadSymbolki_fp_filters': 'DSUB*Male*'}])
    newPart['name'].append('Connector : DB25_Male_MountingHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

