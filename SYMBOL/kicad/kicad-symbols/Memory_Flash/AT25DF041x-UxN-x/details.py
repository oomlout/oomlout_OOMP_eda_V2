
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "AT25DF041x-UxN-x"
    hexID = "SZKMEMORYFLASHAT25DF41XUXNX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT25DF041x-UxN-x', 'kicadSymbolFootprint': 'Package_CSP:WLCSP-8_1.58x1.63x0.35mm_Layout3x5_P0.35x0.4mm_Ball0.25mm_Pad0.25mm_NSMD', 'kicadSymbolDatasheet': 'http://www.adestotech.com/wp-content/uploads/DS-AT25DF041B_040.pdf', 'kicadSymbolki_keywords': 'SPI DSPI 4Mbit 1.65V', 'kicadSymbolki_description': '4-Mbit, 1.65V Minimum SPI Serial Flash Memory with Dual-I/O, WLCSP-8', 'kicadSymbolki_fp_filters': 'WLCSP?8*1.58x1.63*Layout3x5*P0.35x0.4mm*Ball0.25mm*'}])
    newPart['name'].append('Memory_Flash : AT25DF041x-UxN-x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

