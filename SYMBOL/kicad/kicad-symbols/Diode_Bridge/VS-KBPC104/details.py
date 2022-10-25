
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "VS-KBPC104"
    hexID = "SZKDIODEBRIDGEVSKBPC14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'VS-KBPC1005', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'VS-KBPC104', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Vishay_KBPC1', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/93585/vs-kbpc1series.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 125V Vrms, 3.0A If, KBPC1 package', 'kicadSymbolki_fp_filters': 'D*Bridge*Vishay*KBPC1*'}])
    newPart['name'].append('Diode_Bridge : VS-KBPC104')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

