
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "KBU4D"
    hexID = "SZKDIODEBRIDGEKBU4D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'KBU4A', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'KBU4D', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Vishay_KBU', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88656/kbu4.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 140V Vrms, 4.0A If, KBU package', 'kicadSymbolki_fp_filters': 'Diode*Bridge*Vishay*KBU*'}])
    newPart['name'].append('KBU4D')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

