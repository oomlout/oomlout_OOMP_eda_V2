
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "RMB4S"
    hexID = "SZKDIODEBRIDGERMB4S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MB2S', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'RMB4S', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-269AA', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88705/rmbs.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Miniature Glass Passivated Single-Phase Surface Mount Bridge Rectifiers, 280V Vrms, 0.5A If, TO-269AA', 'kicadSymbolki_fp_filters': 'TO?269AA*'}])
    newPart['name'].append('Diode_Bridge : RMB4S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

