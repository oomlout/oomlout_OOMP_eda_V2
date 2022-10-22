
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "DF01S1"
    hexID = "SZKDIODEBRIDGEDF1S1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ABS2', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'DF01S1', 'kicadSymbolFootprint': 'Diode_SMD:Diode_Bridge_OnSemi_SDIP-4L', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pdf/datasheet/df10s1-d.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Bridge Rectifier, 70V Vrms, 1.0A If, SMDIP-4', 'kicadSymbolki_fp_filters': 'Diode*Bridge*OnSemi*SDIP*4L*'}])
    newPart['name'].append('DF01S1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

