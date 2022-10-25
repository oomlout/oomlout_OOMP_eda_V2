
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "AS4C4M16SA"
    hexID = "SZKMEMORYRAMAS4C4M16SA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS4C4M16SA', 'kicadSymbolFootprint': 'Package_SO:TSOP-II-54_22.2x10.16mm_P0.8mm', 'kicadSymbolDatasheet': 'https://www.alliancememory.com/wp-content/uploads/pdf/dram/64M-AS4C4M16SA-CI_v3.0_March%202015.pdf', 'kicadSymbolki_keywords': 'SDRAM Synchronous DRAM PC166 PC143 64Mb 16Mbx4 MEMORY', 'kicadSymbolki_description': '64M – (4M x 16 bit) Synchronous DRAM (SDRAM), TSOP-II-54', 'kicadSymbolki_fp_filters': 'TSOP?II*22.2x10.16mm*P0.8mm*'}])
    newPart['name'].append('Memory_RAM : AS4C4M16SA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

