
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "DSP_Texas"
    oIndex = "TMS320LF2406PZ"
    hexID = "SZKDSPTEXASTMS32LF246PZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMS320LF2406PZ', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tms320lf2406.pdf', 'kicadSymbolki_keywords': '16BIT DSP TMS320 Obsolete', 'kicadSymbolki_description': '16bit DSP Controller 32Kx16B Flash 2.5Kx16B RAM, Obsolete NRND, PQFP-100', 'kicadSymbolki_fp_filters': 'PQFP-100*'}])
    newPart['name'].append('TMS320LF2406PZ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

