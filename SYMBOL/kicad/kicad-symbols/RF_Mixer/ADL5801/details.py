
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Mixer"
    oIndex = "ADL5801"
    hexID = "SZKRFMIXERADL581"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADL5801', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-VQ-24-1EP_4x4mm_P0.5mm_EP2.642x2.642mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADL5801.pdf', 'kicadSymbolki_keywords': 'mixer active', 'kicadSymbolki_description': '10 MHz to 6 GHz Active Mixer, LFCSP-24', 'kicadSymbolki_fp_filters': 'LFCSP*4x4mm*P0.5mm*EP2.642x2.642mm*'}])
    newPart['name'].append('RF_Mixer : ADL5801')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

