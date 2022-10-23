
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Amplifier"
    oIndex = "SGL0622Z"
    hexID = "SZKRFAMPLIFIERSGL622Z"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SGL0622Z', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_2x2mm_P0.5mm_EP0.6x1.2mm', 'kicadSymbolDatasheet': 'https://www.qorvo.com/products/d/da001879', 'kicadSymbolki_keywords': 'rf gain block', 'kicadSymbolki_description': '5 MHz to 4000 MHz, Low-Noise SiGe HBT MMIC Amplifier, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('SGL0622Z')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

