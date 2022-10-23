
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_PLL"
    oIndex = "ADF4158"
    hexID = "SZKTIMERPLLADF4158"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADF4158', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-24-1EP_4x4mm_P0.5mm_EP2.5x2.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADF4158.pdf', 'kicadSymbolki_keywords': 'fractional-N PLL', 'kicadSymbolki_description': '0.5-6.1GHz fractional-N PLL, LFCSP-24', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('ADF4158')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

