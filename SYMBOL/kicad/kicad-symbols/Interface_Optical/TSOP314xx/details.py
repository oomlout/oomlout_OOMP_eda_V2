
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Optical"
    oIndex = "TSOP314xx"
    hexID = "SZKINTERFACEOPTICALTS314XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSOP17xx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSOP314xx', 'kicadSymbolFootprint': 'OptoDevice:Vishay_CAST-3Pin', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/82492/tsop312.pdf', 'kicadSymbolki_keywords': 'opto IR receiver', 'kicadSymbolki_description': 'Photo Modules for PCM Remote Control Systems', 'kicadSymbolki_fp_filters': 'Vishay*CAST*'}])
    newPart['name'].append('TSOP314xx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

