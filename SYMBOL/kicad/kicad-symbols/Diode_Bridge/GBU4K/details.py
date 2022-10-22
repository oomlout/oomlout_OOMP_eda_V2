
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "GBU4K"
    hexID = "SZKDIODEBRIDGEGBU4K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'GBU4A', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'GBU4K', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Vishay_GBU', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88656/gbu4a.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 560V Vrms, 4.0A If, GBU package', 'kicadSymbolki_fp_filters': 'Diode*Bridge*Vishay*GBU*'}])
    newPart['name'].append('GBU4K')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

