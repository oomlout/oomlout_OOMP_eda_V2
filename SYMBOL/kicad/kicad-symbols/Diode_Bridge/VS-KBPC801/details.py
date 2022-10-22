
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "VS-KBPC801"
    hexID = "SZKDIODEBRIDGEVSKBPC81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'VS-KBPC8005', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'VS-KBPC801', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Vishay_KBPC6', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/93586/kbpc8series.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 40V Vrms, 8.0A If, KBPC6 package', 'kicadSymbolki_fp_filters': 'D*Bridge*Vishay*KBPC6*'}])
    newPart['name'].append('VS-KBPC801')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

