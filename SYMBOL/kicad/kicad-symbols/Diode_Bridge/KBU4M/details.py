
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "KBU4M"
    hexID = "SZKDIODEBRIDGEKBU4M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'KBU4A', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'KBU4M', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Vishay_KBU', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88656/kbu4.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 700V Vrms, 4.0A If, KBU package', 'kicadSymbolki_fp_filters': 'Diode*Bridge*Vishay*KBU*'}])
    newPart['name'].append('KBU4M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

