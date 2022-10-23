
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Video"
    oIndex = "TDA8702T"
    hexID = "SZKVIDEOTDA872T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TDA8702', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDA8702T', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'philips/tda8702.pdf', 'kicadSymbolki_keywords': 'DAC CNA VIDEO', 'kicadSymbolki_description': '8bit Video DAC (32 MHz), SOIC-16', 'kicadSymbolki_fp_filters': 'DIP* PDIP* SO* SOIC*'}])
    newPart['name'].append('TDA8702T')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

