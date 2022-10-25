
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Valve"
    oIndex = "EF85"
    hexID = "SZKVAEF85"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EF80', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EF85', 'kicadSymbolFootprint': 'Valve:Valve_Noval_P', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'pentode valve', 'kicadSymbolki_description': 'pentode', 'kicadSymbolki_fp_filters': 'VALVE*NOVAL*P*'}])
    newPart['name'].append('Valve : EF85')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

