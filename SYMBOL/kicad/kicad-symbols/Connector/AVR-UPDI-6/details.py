
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "AVR-UPDI-6"
    hexID = "SZKCNAVRUPDI6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'AVR-UPDI-6', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.microchip.com/webdoc/GUID-9D10622A-5C16-4405-B092-1BDD437B4976/index.html?GUID-9B349315-2842-4189-B88C-49F4E1055D7F', 'kicadSymbolki_keywords': 'AVR UPDI Connector', 'kicadSymbolki_description': 'Atmel 6-pin UPDI connector', 'kicadSymbolki_fp_filters': 'IDC?Header*2x03* Pin?Header*2x03*'}])
    newPart['name'].append('Connector : AVR-UPDI-6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

