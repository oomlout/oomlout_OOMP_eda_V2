
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "KBU4J"
    hexID = "SZKDIODEBRIDGEKBU4J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'KBU4A', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'KBU4J', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Vishay_KBU', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88656/kbu4.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 420V Vrms, 4.0A If, KBU package', 'kicadSymbolki_fp_filters': 'Diode*Bridge*Vishay*KBU*'}])
    newPart['name'].append('Diode_Bridge : KBU4J')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

