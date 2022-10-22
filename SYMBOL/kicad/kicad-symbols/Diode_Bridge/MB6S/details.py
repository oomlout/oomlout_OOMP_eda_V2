
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "MB6S"
    hexID = "SZKDIODEBRIDGEMB6S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MB2S', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MB6S', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-269AA', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88573/dfs.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Miniature Glass Passivated Single-Phase Surface Mount Bridge Rectifiers, 700V Vrms, 1.0A If, DFS SMD package', 'kicadSymbolki_fp_filters': 'TO?269AA*'}])
    newPart['name'].append('MB6S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

