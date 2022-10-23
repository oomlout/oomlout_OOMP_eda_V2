
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_PLL"
    oIndex = "ADF4350"
    hexID = "SZKTIMERPLLADF435"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADF4351', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADF4350', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-32-1EP_5x5mm_P0.5mm_EP3.25x3.25mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADF4350.pdf', 'kicadSymbolki_keywords': 'fractional-N PLL', 'kicadSymbolki_description': '137.5-4400MHz fractional-N PLL, LFCSP-32', 'kicadSymbolki_fp_filters': 'LFCSP*32*1EP*5x5mm*P0.5mm*EP3.25x3.25mm*'}])
    newPart['name'].append('ADF4350')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

