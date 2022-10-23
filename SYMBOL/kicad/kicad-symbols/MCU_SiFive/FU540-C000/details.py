
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiFive"
    oIndex = "FU540-C000"
    hexID = "SZKMCUSIFIVEFU54C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FU540-C000', 'kicadSymbolFootprint': 'Package_BGA:BGA-484_23.0x23.0mm_Layout22x22_P1.0mm', 'kicadSymbolDatasheet': 'https://static.dev.sifive.com/FU540-C000-v1.0.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'SiFive', 'kicadSymbolki_description': '64-bit RISC‑V SoC, BGA-484', 'kicadSymbolki_fp_filters': 'BGA*23.0x23.0mm*P1.0mm*'}])
    newPart['name'].append('FU540-C000')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

