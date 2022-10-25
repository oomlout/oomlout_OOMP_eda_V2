
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "MT48LC32M8A2P"
    hexID = "SZKMEMORYRAMMT48LC32M8A2P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MT48LC32M8A2TG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MT48LC32M8A2P', 'kicadSymbolFootprint': 'Package_SO:TSOP-II-54_22.2x10.16mm_P0.8mm', 'kicadSymbolDatasheet': 'https://www.micron.com/-/media/client/global/documents/products/data-sheet/dram/256mb_sdr.pdf', 'kicadSymbolki_keywords': 'SDRAM Synchronous DRAM PC100 PC133 256Mb 32Mbx8 MEMORY', 'kicadSymbolki_description': '256M – (32M x 8 bit) Synchronous DRAM (SDRAM), TSOP-II-54', 'kicadSymbolki_fp_filters': 'TSOP?II*22.2x10.16mm*P0.8mm*'}])
    newPart['name'].append('Memory_RAM : MT48LC32M8A2P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

