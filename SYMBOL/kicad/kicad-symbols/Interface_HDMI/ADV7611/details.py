
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_HDMI"
    oIndex = "ADV7611"
    hexID = "SZKINTERFACEHDMIADV7611"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADV7611', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64-1EP_10x10mm_P0.5mm_EP5x5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/adv7611.pdf', 'kicadSymbolki_keywords': 'hdmi', 'kicadSymbolki_description': 'Low Power 165MHz HDMI Receiver, LQFP-64', 'kicadSymbolki_fp_filters': 'LQFP*1EP*10x10mm*P0.5mm*'}])
    newPart['name'].append('ADV7611')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

