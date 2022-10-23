
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Switch"
    oIndex = "ADG918BCPZ"
    hexID = "SZKRFSWITCHADG918BCPZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADG918BCPZ', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-8-1EP_3x3mm_P0.5mm_EP1.45x1.74mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADG918_919.pdf', 'kicadSymbolki_keywords': 'RF Mux SPDT switch CMOS LVTTL', 'kicadSymbolki_description': 'SPDT DC-4GHz absorbative switch, 43dB isolation at 1GHz, LFCSP-8', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('ADG918BCPZ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

