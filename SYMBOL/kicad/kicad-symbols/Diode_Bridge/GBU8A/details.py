
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "GBU8A"
    hexID = "SZKDIODEBRIDGEGBU8A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'GBU4A', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'GBU8A', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Vishay_GBU', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88656/gbu8a.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 35V Vrms, 8.0A If, GBU package', 'kicadSymbolki_fp_filters': 'Diode*Bridge*Vishay*GBU*'}])
    newPart['name'].append('Diode_Bridge : GBU8A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

