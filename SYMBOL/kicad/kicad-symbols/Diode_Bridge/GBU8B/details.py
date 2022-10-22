
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "GBU8B"
    hexID = "SZKDIODEBRIDGEGBU8B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'GBU4A', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'GBU8B', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Vishay_GBU', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88656/gbu8a.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 70V Vrms, 8.0A If, GBU package', 'kicadSymbolki_fp_filters': 'Diode*Bridge*Vishay*GBU*'}])
    newPart['name'].append('GBU8B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

