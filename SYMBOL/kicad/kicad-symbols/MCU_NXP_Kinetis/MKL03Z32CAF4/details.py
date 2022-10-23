
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL03Z32CAF4"
    hexID = "SZKMCUNXPKINETISMKL3Z32CAF4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL03Z32CAF4', 'kicadSymbolFootprint': 'Package_CSP:WLCSP-20_1.994x1.609mm_Layout5x4_P0.4mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL03P24M48SF0.pdf', 'kicadSymbolki_keywords': 'Kinetis KL03 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL03 series, 48-MHz/32-bit ARM Cortex-M0+, 32 kB flash, 2 kB SRAM, WLCSP-20', 'kicadSymbolki_fp_filters': 'WLCSP*1.994x1.609mm*P0.4mm*'}])
    newPart['name'].append('MKL03Z32CAF4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

