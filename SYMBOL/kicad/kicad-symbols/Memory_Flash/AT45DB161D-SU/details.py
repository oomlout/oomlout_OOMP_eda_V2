
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "AT45DB161D-SU"
    hexID = "SZKMEMORYFLASHAT45DB161DSU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT45DB161D-SU', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_5.275x5.275mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.adestotech.com/wp-content/uploads/doc3500.pdf', 'kicadSymbolki_keywords': 'Adesto Flash Memory DataFlash', 'kicadSymbolki_description': '16Mb Serial DataFlash, 2.5V Vcc, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*P1.27mm*'}])
    newPart['name'].append('Memory_Flash : AT45DB161D-SU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

