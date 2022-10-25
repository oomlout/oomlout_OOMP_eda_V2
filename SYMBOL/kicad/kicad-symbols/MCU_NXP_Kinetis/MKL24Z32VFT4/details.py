
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL24Z32VFT4"
    hexID = "SZKMCUNXPKINETISMKL24Z32VFT4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MKL24Z64VFT4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL24Z32VFT4', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.15x5.15mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL24P80M48SF0.pdf', 'kicadSymbolki_keywords': 'Kinetis KL24 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL24 series, 48-MHz/32-bit ARM Cortex-M0+, 32 kB flash, 4 kB SRAM, USB FS Device/OTG, QFN-48', 'kicadSymbolki_fp_filters': 'QFN*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MKL24Z32VFT4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

