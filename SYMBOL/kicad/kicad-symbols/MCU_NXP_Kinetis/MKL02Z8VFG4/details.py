
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL02Z8VFG4"
    hexID = "SZKMCUNXPKINETISMKL2Z8VFG4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MKL02Z32VFG4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL02Z8VFG4', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_3x3mm_P0.5mm_EP1.9x1.9mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL02P32M48SF0.pdf', 'kicadSymbolki_keywords': 'Kinetis KL02 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL02 series, 48-MHz/32-bit ARM Cortex-M0+, 8 kB flash, 1 kB SRAM, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('MKL02Z8VFG4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

