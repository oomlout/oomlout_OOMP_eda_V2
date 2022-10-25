
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "AT45DB161-JC"
    hexID = "SZKMEMORYFLASHAT45DB161JC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT45DB161-JC', 'kicadSymbolFootprint': 'Package_LCC:PLCC-32_11.4x14.0mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/doc0807.pdf', 'kicadSymbolki_keywords': 'Atmel DataFlash', 'kicadSymbolki_description': '16Mb Serial DataFlash, 2.7V Vcc, PLCC-32', 'kicadSymbolki_fp_filters': 'PLCC?32*11.4x14.0mm*P1.27mm*'}])
    newPart['name'].append('Memory_Flash : AT45DB161-JC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

