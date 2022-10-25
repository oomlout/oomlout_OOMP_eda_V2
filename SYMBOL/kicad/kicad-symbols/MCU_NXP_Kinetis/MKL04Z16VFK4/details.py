
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL04Z16VFK4"
    hexID = "SZKMCUNXPKINETISMKL4Z16VFK4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MKL04Z32VFK4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL04Z16VFK4', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL04P48M48SF1.pdf', 'kicadSymbolki_keywords': 'Kinetis KL04 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL04 series, 48-MHz/32-bit ARM Cortex-M0+, 16 kB flash, 2 kB SRAM, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MKL04Z16VFK4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

