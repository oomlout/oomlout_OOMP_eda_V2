
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL17Z32VDA4"
    hexID = "SZKMCUNXPKINETISMKL17Z32VDA4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MKL17Z64VDA4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL17Z32VDA4', 'kicadSymbolFootprint': 'Package_BGA:XFBGA-36_3.5x3.5mm_Layout6x6_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL17P64M48SF2.pdf', 'kicadSymbolki_keywords': 'Kinetis KL17 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL17 series, 48-MHz/32-bit ARM Cortex-M0+, 32 kB flash, 8 kB SRAM, FlexIO, XFBGA-36', 'kicadSymbolki_fp_filters': 'XFBGA*3.5x3.5mm*P0.5mm*'}])
    newPart['name'].append('MKL17Z32VDA4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

