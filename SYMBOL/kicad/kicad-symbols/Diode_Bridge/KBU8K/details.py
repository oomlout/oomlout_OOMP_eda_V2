
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "KBU8K"
    hexID = "SZKDIODEBRIDGEKBU8K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'KBU4A', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'KBU8K', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Vishay_KBU', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88656/kbu8.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 560V Vrms, 8.0A If, KBU package', 'kicadSymbolki_fp_filters': 'Diode*Bridge*Vishay*KBU*'}])
    newPart['name'].append('KBU8K')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

