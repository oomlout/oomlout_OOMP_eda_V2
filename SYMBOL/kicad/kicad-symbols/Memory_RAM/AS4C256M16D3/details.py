
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "AS4C256M16D3"
    hexID = "SZKMEMORYRAMAS4C256M16D3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS4C256M16D3', 'kicadSymbolFootprint': 'Package_BGA:BGA-96_9.0x13.0mm_Layout2x3x16_P0.8mm', 'kicadSymbolDatasheet': 'https://www.alliancememory.com/wp-content/uploads/pdf/ddr3/4GB-AS4C256M16D3.pdf', 'kicadSymbolki_keywords': 'DDR3 DRAM MEMORY', 'kicadSymbolki_description': '4Gb (256Mx16 bit) Double Data Rate 3 Synchronous DRAM', 'kicadSymbolki_fp_filters': 'BGA*9.0x13.0mm*P0.8mm*'}])
    newPart['name'].append('Memory_RAM : AS4C256M16D3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

