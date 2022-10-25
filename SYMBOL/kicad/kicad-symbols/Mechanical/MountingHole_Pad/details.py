
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Mechanical"
    oIndex = "MountingHole_Pad"
    hexID = "SZKMECHANICALHOLPAD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'H', 'kicadSymbolValue': 'MountingHole_Pad', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'mounting hole', 'kicadSymbolki_description': 'Mounting Hole with connection', 'kicadSymbolki_fp_filters': 'MountingHole*Pad*'}])
    newPart['name'].append('Mechanical : MountingHole_Pad')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

