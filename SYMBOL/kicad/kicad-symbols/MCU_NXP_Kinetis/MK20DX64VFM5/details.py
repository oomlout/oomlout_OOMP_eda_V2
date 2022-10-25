
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MK20DX64VFM5"
    hexID = "SZKMCUNXPKINETISMK2DX64VFM5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MK20DX128VFM5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MK20DX64VFM5', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.45x3.45mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/K20P32M50SF0.pdf', 'kicadSymbolki_keywords': 'Kinetis KL27 ARM Cortex M4', 'kicadSymbolki_description': 'Kinetis K20 series, 50-MHz/32-bit ARM Cortex-M4, 64 kB flash/32 kB FlexNVM, 16 kB SRAM/2 kB FlexRAM, USB FS Device/OTG, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*5x5mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MK20DX64VFM5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

