
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "VS-KBPC604"
    hexID = "SZKDIODEBRIDGEVSKBPC64"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'VS-KBPC6005', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'VS-KBPC604', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Vishay_KBPC6', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/93585/vs-kbpc1series.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 125V Vrms, 6.0A If, KBPC6 package', 'kicadSymbolki_fp_filters': 'D*Bridge*Vishay*KBPC6*'}])
    newPart['name'].append('VS-KBPC604')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

