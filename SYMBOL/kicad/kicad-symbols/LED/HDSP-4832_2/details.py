
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "HDSP-4832_2"
    hexID = "SZKLHDSP48322"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'BAR', 'kicadSymbolValue': 'HDSP-4832_2', 'kicadSymbolFootprint': 'Display:HDSP-4832', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-1798EN', 'kicadSymbolki_keywords': 'display LED array', 'kicadSymbolki_description': 'BAR GRAPH 10 segment block, Mix of high efficiency red, yellow and green', 'kicadSymbolki_fp_filters': 'HDSP?48*'}])
    newPart['name'].append('HDSP-4832_2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

