
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "GBU6B"
    hexID = "SZKDIODEBRIDGEGBU6B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'GBU4A', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'GBU6B', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Vishay_GBU', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88656/gbu6a.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 70V Vrms, 6.0A If, GBU package', 'kicadSymbolki_fp_filters': 'Diode*Bridge*Vishay*GBU*'}])
    newPart['name'].append('GBU6B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

