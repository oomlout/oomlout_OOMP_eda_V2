
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_PLL"
    oIndex = "ADF4002BCPZ"
    hexID = "SZKTIMERPLLADF42BCPZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADF4002BCPZ', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-20-1EP_4x4mm_P0.5mm_EP2.1x2.1mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADF4002.pdf', 'kicadSymbolki_keywords': 'Analog Devices PFD', 'kicadSymbolki_description': '400MHz Bandwidth Frequency Synthesizer, LFCSP-20', 'kicadSymbolki_fp_filters': 'LFCSP*4x4mm*P0.5mm*EP2.1x2.1mm*'}])
    newPart['name'].append('Timer_PLL : ADF4002BCPZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

