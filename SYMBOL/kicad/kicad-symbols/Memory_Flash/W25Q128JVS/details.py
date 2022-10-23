
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "W25Q128JVS"
    hexID = "SZKMEMORYFLASHW25Q128JVS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'W25Q32JVSS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'W25Q128JVS', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_5.23x5.23mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.winbond.com/resource-files/w25q128jv_dtr%20revc%2003272018%20plus.pdf', 'kicadSymbolki_keywords': 'flash memory SPI QPI DTR', 'kicadSymbolki_description': '128Mb Serial Flash Memory, Standard/Dual/Quad SPI, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*5.23x5.23mm*P1.27mm*'}])
    newPart['name'].append('W25Q128JVS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

