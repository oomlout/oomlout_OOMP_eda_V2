
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL05Z8VLC4"
    hexID = "SZKMCUNXPKINETISMKL5Z8VLC4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MKL05Z32VLC4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL05Z8VLC4', 'kicadSymbolFootprint': 'Package_QFP:LQFP-32_7x7mm_P0.8mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL05P48M48SF1.pdf', 'kicadSymbolki_keywords': 'Kinetis KL05 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL05 series, 48-MHz/32-bit ARM Cortex-M0+, 8 kB flash, 1 kB SRAM, LQFP-32', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.8mm*'}])
    newPart['name'].append('MKL05Z8VLC4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

