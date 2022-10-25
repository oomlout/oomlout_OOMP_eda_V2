
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL17Z256VFM4"
    hexID = "SZKMCUNXPKINETISMKL17Z256VFM4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL17Z256VFM4', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.45x3.45mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL17P64M48SF6.pdf', 'kicadSymbolki_keywords': 'Kinetis KL17 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL17 series, 48-MHz/32-bit ARM Cortex-M0+, 256 kB flash, 32 kB SRAM, FlexIO, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*5x5mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MKL17Z256VFM4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

