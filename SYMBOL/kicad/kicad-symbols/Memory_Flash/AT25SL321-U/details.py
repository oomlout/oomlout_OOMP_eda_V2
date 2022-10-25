
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "AT25SL321-U"
    hexID = "SZKMEMORYFLASHAT25SL321U"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT25SL321-U', 'kicadSymbolFootprint': 'Package_CSP:WLCSP-8_1.551x2.284mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.adestotech.com/wp-content/uploads/AT25SL321_112.pdf', 'kicadSymbolki_keywords': 'SPI DSPI QSPI 32Mbit 1.7V', 'kicadSymbolki_description': '32-Mbit, 1.7V 2.5V Minimum SPI Serial Flash Memory with Dual-I/O and Quad-I/O Support, WLCSP-8', 'kicadSymbolki_fp_filters': 'WLCSP*1.551x2.284mm*P0.5mm*'}])
    newPart['name'].append('Memory_Flash : AT25SL321-U')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

