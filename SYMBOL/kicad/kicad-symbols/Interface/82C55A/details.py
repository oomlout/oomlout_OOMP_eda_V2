
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "82C55A"
    hexID = "SZKINTERFACE82C55A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '8255', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '82C55A', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://jap.hu/electronic/8255.pdf', 'kicadSymbolki_keywords': '8255 PPI', 'kicadSymbolki_description': 'CHMOS Programmable Peripheral Interface, PDIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm* PDIP*W15.24mm*'}])
    newPart['name'].append('82C55A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

