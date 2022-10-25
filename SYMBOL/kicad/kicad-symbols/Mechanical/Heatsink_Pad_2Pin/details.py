
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Mechanical"
    oIndex = "Heatsink_Pad_2Pin"
    hexID = "SZKMECHANICALHPAD2PIN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'HS', 'kicadSymbolValue': 'Heatsink_Pad_2Pin', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'thermal heat temperature', 'kicadSymbolki_description': 'Heatsink with electrical connection, 2 pin', 'kicadSymbolki_fp_filters': 'Heatsink_*'}])
    newPart['name'].append('Mechanical : Heatsink_Pad_2Pin')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

