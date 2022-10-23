
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Mixer"
    oIndex = "ADL5802"
    hexID = "SZKRFMIXERADL582"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADL5802', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-24-1EP_4x4mm_P0.5mm_EP2.5x2.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADL5802.pdf', 'kicadSymbolki_keywords': 'mixer rf', 'kicadSymbolki_description': '100 MHz to 6 GHz Dual Channel Active Mixer, LFCSP-24', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('ADL5802')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

