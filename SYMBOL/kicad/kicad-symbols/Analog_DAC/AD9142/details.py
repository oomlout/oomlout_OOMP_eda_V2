
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD9142"
    hexID = "SZKANALOGDACAD9142"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD9142', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-72-1EP_10x10mm_P0.5mm_EP6.15x6.15mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD9142.pdf', 'kicadSymbolki_keywords': '16bit DAC 2CH', 'kicadSymbolki_description': '1.6GSPS 16bit dual-channel DAC, LFCSP-72', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*10x10mm*P0.5mm*EP6.15x6.15mm*'}])
    newPart['name'].append('AD9142')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

