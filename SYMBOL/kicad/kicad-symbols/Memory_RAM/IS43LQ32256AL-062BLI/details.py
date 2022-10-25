
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "IS43LQ32256AL-062BLI"
    hexID = "SZKMEMORYRAMIS43LQ32256AL62BLI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IS43LQ32256A-062BLI', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IS43LQ32256AL-062BLI', 'kicadSymbolFootprint': 'Package_BGA:BGA-200_10.0x14.5mm_Layout12x22_P0.80x0.65mm', 'kicadSymbolDatasheet': 'http://www.issi.com/WW/pdf/43-46LQ32256AL-AL.pdf', 'kicadSymbolki_keywords': 'DRAM MEMORY', 'kicadSymbolki_description': '256Mx32 bit Low Power Double Data Rate 4X (LPDDR4X) SDRAM, 1600 MHz, Industrial, BGA-200', 'kicadSymbolki_fp_filters': 'BGA*10.0x14.5mm*P0.80x0.65mm*'}])
    newPart['name'].append('Memory_RAM : IS43LQ32256AL-062BLI')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

