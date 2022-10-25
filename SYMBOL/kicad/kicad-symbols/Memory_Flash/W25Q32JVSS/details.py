
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "W25Q32JVSS"
    hexID = "SZKMEMORYFLASHW25Q32JVSS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'W25Q32JVSS', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_5.23x5.23mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.winbond.com/resource-files/w25q32jv%20revg%2003272018%20plus.pdf', 'kicadSymbolki_keywords': 'flash memory SPI', 'kicadSymbolki_description': '32Mb Serial Flash Memory, Standard/Dual/Quad SPI, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*5.23x5.23mm*P1.27mm*'}])
    newPart['name'].append('Memory_Flash : W25Q32JVSS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

