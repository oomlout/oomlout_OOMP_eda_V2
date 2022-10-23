
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "628128_TSOP32"
    hexID = "SZKMEMORYRAM628128TS32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '628128_TSOP32', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.futurlec.com/Datasheet/Memory/628128.pdf', 'kicadSymbolki_keywords': 'RAM SRAM CMOS MEMORY', 'kicadSymbolki_description': '128K x 8 High-Speed CMOS Static RAM, 55/70ns, TSOP-I-32', 'kicadSymbolki_fp_filters': 'TSOP?I*11.8x8mm*P0.5mm* TSOP?I*18.4x8mm*P0.5mm*'}])
    newPart['name'].append('628128_TSOP32')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

