
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPU_NXP_68000"
    oIndex = "MC68332"
    hexID = "SZKCPUNXP68MC68332"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC68332', 'kicadSymbolFootprint': 'Package_QFP:PQFP-132_24x24mm_P0.635mm', 'kicadSymbolDatasheet': 'http://pdf.datasheetcatalog.com/datasheet/motorola/SPAKMC332AVFC20.pdf', 'kicadSymbolki_keywords': 'MCU 32 bit', 'kicadSymbolki_description': 'MCU 32 bit, PQFP-132', 'kicadSymbolki_fp_filters': 'PQFP*24x24mm*P0.635mm*'}])
    newPart['name'].append('MC68332')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

