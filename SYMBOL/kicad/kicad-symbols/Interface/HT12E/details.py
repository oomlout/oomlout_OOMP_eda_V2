
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "HT12E"
    hexID = "SZKINTERFACEHT12E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HT12E', 'kicadSymbolFootprint': 'Package_SO:SOP-20_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.holtek.com/documents/10179/116711/2_12ev120.pdf', 'kicadSymbolki_keywords': 'Serial Encoder', 'kicadSymbolki_description': '2^12 serial encoder, SOP-20', 'kicadSymbolki_fp_filters': 'SOP*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('HT12E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

