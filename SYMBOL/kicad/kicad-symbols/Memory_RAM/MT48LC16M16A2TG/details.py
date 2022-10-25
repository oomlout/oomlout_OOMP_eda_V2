
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "MT48LC16M16A2TG"
    hexID = "SZKMEMORYRAMMT48LC16M16A2TG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MT48LC16M16A2TG', 'kicadSymbolFootprint': 'Package_SO:TSOP-II-54_22.2x10.16mm_P0.8mm', 'kicadSymbolDatasheet': 'https://www.micron.com/-/media/client/global/documents/products/data-sheet/dram/256mb_sdr.pdf', 'kicadSymbolki_keywords': 'SDRAM Synchronous DRAM PC100 PC133 256Mb 16Mbx16 MEMORY', 'kicadSymbolki_description': '256M – (16M x 16 bit) Synchronous DRAM (SDRAM), TSOP-II-54', 'kicadSymbolki_fp_filters': 'TSOP?II*22.2x10.16mm*P0.8mm*'}])
    newPart['name'].append('Memory_RAM : MT48LC16M16A2TG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

