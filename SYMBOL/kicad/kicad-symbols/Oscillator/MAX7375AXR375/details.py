
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "MAX7375AXR375"
    hexID = "SZKOCSMAX7375AXR375"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX7375AXR805', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX7375AXR375', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-323_SC-70', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX7375.pdf', 'kicadSymbolki_keywords': 'Silicon Clock Oscillator 3.69MHz 3690kHz', 'kicadSymbolki_description': 'Silicon Clock Oscillator 3.69MHz, SC-70-3', 'kicadSymbolki_fp_filters': '*SC?70*'}])
    newPart['name'].append('MAX7375AXR375')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

