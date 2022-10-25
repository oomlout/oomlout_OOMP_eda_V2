
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "IS42S16400J-xC"
    hexID = "SZKMEMORYRAMIS42S164JXC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IS42S16400J-xC', 'kicadSymbolFootprint': 'Package_SO:TSOP-II-54_22.2x10.16mm_P0.8mm', 'kicadSymbolDatasheet': 'http://www.issi.com/WW/pdf/42-45S16400J.pdf', 'kicadSymbolki_keywords': 'DRAM MEMORY', 'kicadSymbolki_description': '64Mb Synchronous DRAM, 1 Mb x 16 b x 4 Banks, Cu leadframe plated with matte Sn, TSOP-II-54', 'kicadSymbolki_fp_filters': 'TSOP?II*22.2x10.16mm*P0.8mm*'}])
    newPart['name'].append('Memory_RAM : IS42S16400J-xC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

