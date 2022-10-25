
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "AT45DB161-TC"
    hexID = "SZKMEMORYFLASHAT45DB161TC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT45DB161-TC', 'kicadSymbolFootprint': 'Package_SO:TSOP-28_11.8x8mm_P0.55mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/doc0807.pdf', 'kicadSymbolki_keywords': 'Atmel DataFlash', 'kicadSymbolki_description': '16Mb Serial DataFlash, 2.7V Vcc, TSOP-28', 'kicadSymbolki_fp_filters': 'TSOP?28*11.8x8mm*P0.55mm*'}])
    newPart['name'].append('Memory_Flash : AT45DB161-TC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

