
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "SST25VF080B-50-4x-S2Ax"
    hexID = "SZKMEMORYFLASHSST25VF8B54XS2AX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SST25VF080B-50-4x-S2Ax', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_5.275x5.275mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005045C.pdf', 'kicadSymbolki_keywords': 'flash memory spi', 'kicadSymbolki_description': '8-Mbit, 2.7 to 3.6V, SPI Flash Memory, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*5.275x5.275mm*P1.27mm*'}])
    newPart['name'].append('Memory_Flash : SST25VF080B-50-4x-S2Ax')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

