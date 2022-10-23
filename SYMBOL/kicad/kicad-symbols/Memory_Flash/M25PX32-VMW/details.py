
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "M25PX32-VMW"
    hexID = "SZKMEMORYFLASHM25PX32VMW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'M25PX32-VMW', 'kicadSymbolFootprint': 'Package_SO:SOIC-8W_5.3x5.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.micron.com/~/media/documents/products/data-sheet/nor-flash/serial-nor/m25px/m25px32.pdf', 'kicadSymbolki_keywords': 'NOR Serial Flash Embedded Memory', 'kicadSymbolki_description': '32Mb, Dual I/O, 4KB Subsector Erase, 3V Serial Flash Memory with 75 MHz SPI Bus Interface, SOIC-8W', 'kicadSymbolki_fp_filters': 'SOIC*5.3x5.3mm*P1.27mm*'}])
    newPart['name'].append('M25PX32-VMW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

