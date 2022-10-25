
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Conn_Triaxial"
    hexID = "SZKCNCONNTRIAXIAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Conn_Triaxial', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'LEMO triaxial connector differential LVDS', 'kicadSymbolki_description': 'triaxial connector (LEMO 00.302, ...)', 'kicadSymbolki_fp_filters': '*LEMO*'}])
    newPart['name'].append('Connector : Conn_Triaxial')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

