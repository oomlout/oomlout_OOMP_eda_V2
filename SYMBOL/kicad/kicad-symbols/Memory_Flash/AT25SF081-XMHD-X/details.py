
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "AT25SF081-XMHD-X"
    hexID = "SZKMEMORYFLASHAT25SF81XMHDX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT25SF081-XMHD-X', 'kicadSymbolFootprint': 'Package_SO:TSSOP-8_4.4x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.adestotech.com/wp-content/uploads/DS-AT25SF081_045.pdf', 'kicadSymbolki_keywords': 'SPI DSPI QSPI 8Mbit 2.5V', 'kicadSymbolki_description': '8-Mbit, 2.5V Minimum SPI Serial Flash Memory with Dual-I/O and Quad-I/O Support, TSSOP-8', 'kicadSymbolki_fp_filters': 'TSSOP?8*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Memory_Flash : AT25SF081-XMHD-X')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

