
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "AVR-TPI-6"
    hexID = "SZKCNAVRTPI6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'AVR-TPI-6', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'AVR TPI Connector', 'kicadSymbolki_description': 'Atmel 6-pin TPI connector', 'kicadSymbolki_fp_filters': 'IDC?Header*2x03* Pin?Header*2x03*'}])
    newPart['name'].append('Connector : AVR-TPI-6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

