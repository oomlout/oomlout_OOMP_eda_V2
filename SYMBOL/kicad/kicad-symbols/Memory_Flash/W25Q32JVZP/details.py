
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "W25Q32JVZP"
    hexID = "SZKMEMORYFLASHW25Q32JVZP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'W25Q32JVZP', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_6x5mm_P1.27mm_EP3.4x4.3mm', 'kicadSymbolDatasheet': 'http://www.winbond.com/resource-files/w25q32jv%20revg%2003272018%20plus.pdf', 'kicadSymbolki_keywords': 'flash memory SPI', 'kicadSymbolki_description': '32Mb Serial Flash Memory, Standard/Dual/Quad SPI, DFN-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*6x5mm*P1.27mm*'}])
    newPart['name'].append('W25Q32JVZP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

