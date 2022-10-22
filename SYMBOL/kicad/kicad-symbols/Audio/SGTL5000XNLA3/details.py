
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "SGTL5000XNLA3"
    hexID = "SZKAUDIOSGTL5XNLA3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SGTL5000XNLA3', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-20-1EP_3x3mm_P0.4mm_EP1.65x1.65mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/SGTL5000.pdf', 'kicadSymbolki_keywords': 'Codec', 'kicadSymbolki_description': 'Low Power Stereo Codec with Headphone Amp, QFN-20', 'kicadSymbolki_fp_filters': 'QFN*1EP*3x3mm*P0.4mm*'}])
    newPart['name'].append('SGTL5000XNLA3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

