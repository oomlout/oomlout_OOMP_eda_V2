
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "AT25SF081-SSHF-X"
    hexID = "SZKMEMORYFLASHAT25SF81SSHFX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AT25SF081-SSHD-X', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT25SF081-SSHF-X', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.adestotech.com/wp-content/uploads/DS-AT25SF081_045.pdf', 'kicadSymbolki_keywords': 'SPI DSPI QSPI 8Mbit 2.3V', 'kicadSymbolki_description': '8-Mbit, 2.3V Minimum SPI Serial Flash Memory with Dual-I/O and Quad-I/O Support, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC?8*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('AT25SF081-SSHF-X')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

