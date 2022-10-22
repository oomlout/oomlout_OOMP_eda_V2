
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "B380C1500G"
    hexID = "SZKDIODEBRIDGEB38C15G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B40C1500G', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'B380C1500G', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Round_D9.8mm', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/88501/b40c1500g.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Glass Passivated Single-Phase Bridge Rectifier, 380V Vrms, 1.5A If, WOG package', 'kicadSymbolki_fp_filters': 'D*Bridge*Round*D9.8mm*'}])
    newPart['name'].append('B380C1500G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

