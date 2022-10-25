
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL05Z32VLF4"
    hexID = "SZKMCUNXPKINETISMKL5Z32VLF4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL05Z32VLF4', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL05P48M48SF1.pdf', 'kicadSymbolki_keywords': 'Kinetis KL05 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL05 series, 48-MHz/32-bit ARM Cortex-M0+, 32 kB flash, 4 kB SRAM, LQFP-48', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MKL05Z32VLF4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

