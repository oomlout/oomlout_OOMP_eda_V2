
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPU_NXP_68000"
    oIndex = "MC68000FN"
    hexID = "SZKCPUNXP68MC68FN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC68000FN', 'kicadSymbolFootprint': 'Package_LCC:PLCC-68', 'kicadSymbolDatasheet': 'http://www.nxp.com/files/32bit/doc/ref_manual/MC68000UM.pdf', 'kicadSymbolki_keywords': 'MPRO', 'kicadSymbolki_description': 'Microprocessor, 16-bit bus', 'kicadSymbolki_fp_filters': 'PLCC*'}])
    newPart['name'].append('MC68000FN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

