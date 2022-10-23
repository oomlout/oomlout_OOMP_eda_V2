
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "628128_DIP32_SSOP32"
    hexID = "SZKMEMORYRAM628128DIP32SS32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '628128_DIP32_SSOP32', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.futurlec.com/Datasheet/Memory/628128.pdf', 'kicadSymbolki_keywords': 'RAM SRAM CMOS MEMORY', 'kicadSymbolki_description': '128K x 8 High-Speed CMOS Static RAM, 55/70ns, DIP-32/SSOP-32', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm* SSOP*11.305x20.495mm*P1.27mm*'}])
    newPart['name'].append('628128_DIP32_SSOP32')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

