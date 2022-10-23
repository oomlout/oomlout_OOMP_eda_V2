
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "GD25D10CT"
    hexID = "SZKMEMORYFLASHGD25D1CT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'GD25D10CT', 'kicadSymbolFootprint': 'Package_SO:SOP-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.elm-tech.com/en/products/spi-flash-memory/gd25d10/gd25d10.pdf', 'kicadSymbolki_keywords': 'SPI DSPI QSPI 1Mbit 3.0V', 'kicadSymbolki_description': '1Mbit, 3.0V Standard and Dual Serial Flash, SOP-8', 'kicadSymbolki_fp_filters': 'SOP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('GD25D10CT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

