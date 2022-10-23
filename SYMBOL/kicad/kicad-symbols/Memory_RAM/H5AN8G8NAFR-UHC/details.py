
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "H5AN8G8NAFR-UHC"
    hexID = "SZKMEMORYRAMH5AN8G8NAFRUHC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'H5AN8G8NAFR-UHC', 'kicadSymbolFootprint': 'Package_BGA:FBGA-78_7.5x11mm_Layout2x3x13_P0.8mm', 'kicadSymbolDatasheet': 'https://www.skhynix.com/product/filedata/fileDownload.do?seq=7687', 'kicadSymbolki_keywords': 'DDR4 DRAM MEMORY', 'kicadSymbolki_description': '8Gb CMOS Double Data Rate IV Synchronous RAM', 'kicadSymbolki_fp_filters': 'FBGA*7.5x11mm*P0.8mm*'}])
    newPart['name'].append('H5AN8G8NAFR-UHC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

