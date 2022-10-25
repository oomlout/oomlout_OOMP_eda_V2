
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "AT45DB161B-RC-2.5"
    hexID = "SZKMEMORYFLASHAT45DB161BRC25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AT45DB161-RC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT45DB161B-RC-2.5', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_8.7x18.25mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/doc2224.pdf', 'kicadSymbolki_keywords': 'Atmel DataFlash', 'kicadSymbolki_description': '16Mb Serial DataFlash, 2.5V Vcc, SOIC-28', 'kicadSymbolki_fp_filters': 'SOIC?28*8.7x18.25mm*P1.27mm*'}])
    newPart['name'].append('Memory_Flash : AT45DB161B-RC-2.5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

