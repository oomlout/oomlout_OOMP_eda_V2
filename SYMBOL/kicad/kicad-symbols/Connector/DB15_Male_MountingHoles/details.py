
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "DB15_Male_MountingHoles"
    hexID = "SZKCNDB15MALEHOLS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'DB15_Male_MountingHoles', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'male D-SUB connector', 'kicadSymbolki_description': '15-pin male D-SUB connector (low-density/2 columns), Mounting Hole', 'kicadSymbolki_fp_filters': 'DSUB*Male*'}])
    newPart['name'].append('Connector : DB15_Male_MountingHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

