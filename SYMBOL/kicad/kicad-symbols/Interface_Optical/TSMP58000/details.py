
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Optical"
    oIndex = "TSMP58000"
    hexID = "SZKINTERFACEOPTICALTSMP58"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSMP58138', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSMP58000', 'kicadSymbolFootprint': 'OptoDevice:Vishay_MINICAST-3Pin', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/82485/tsmp58000.pdf', 'kicadSymbolki_keywords': 'opto IR receiver', 'kicadSymbolki_description': 'Photo Module (Amplify&Condition) for PCM Remote Control Systems', 'kicadSymbolki_fp_filters': 'Vishay*MINICAST*'}])
    newPart['name'].append('TSMP58000')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

