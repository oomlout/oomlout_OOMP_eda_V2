
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "M25PX32-VMP"
    hexID = "SZKMEMORYFLASHM25PX32VMP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'M25PX32-VMP', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-S-8-1EP_6x5mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.micron.com/~/media/documents/products/data-sheet/nor-flash/serial-nor/m25px/m25px32.pdf', 'kicadSymbolki_keywords': 'NOR Serial Flash Embedded Memory', 'kicadSymbolki_description': '32Mb, Dual I/O, 4KB Subsector Erase, 3V Serial Flash Memory with 75 MHz SPI Bus Interface, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*6x5mm*P1.27mm*'}])
    newPart['name'].append('Memory_Flash : M25PX32-VMP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

