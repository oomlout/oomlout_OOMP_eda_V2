
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "VS-KBPC1005"
    hexID = "SZKDIODEBRIDGEVSKBPC15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'VS-KBPC1005', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Vishay_KBPC1', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/93585/vs-kbpc1series.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 20V Vrms, 3.0A If, KBPC1 package', 'kicadSymbolki_fp_filters': 'D*Bridge*Vishay*KBPC1*'}])
    newPart['name'].append('VS-KBPC1005')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

