
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "W25X40CLSS"
    hexID = "SZKMEMORYFLASHW25X4CLSS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'W25X40CLSN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'W25X40CLSS', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_5.275x5.275mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.winbond.com/resource-files/W25X40CL_G%2020210505.pdf', 'kicadSymbolki_keywords': 'Memory Flash SPI', 'kicadSymbolki_description': '4Mbit Serial Flash memory, dual I/O SPI, SOIC-8 208mil', 'kicadSymbolki_fp_filters': 'SOIC*5.275x5.275mm*P1.27mm*'}])
    newPart['name'].append('Memory_Flash : W25X40CLSS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

