
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Valve"
    oIndex = "STABI"
    hexID = "SZKVASTABI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STABI', 'kicadSymbolFootprint': 'Valve:Valve_Glimm', 'kicadSymbolDatasheet': '', 'kicadSymbolki_fp_filters': 'VALVE*GLIMM*'}])
    newPart['name'].append('Valve : STABI')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

