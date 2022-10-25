
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL27Z64VFM4"
    hexID = "SZKMCUNXPKINETISMKL27Z64VFM4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL27Z64VFM4', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.45x3.45mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL27P64M48SF2.pdf', 'kicadSymbolki_keywords': 'Kinetis KL27 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL27 series, 48-MHz/32-bit ARM Cortex-M0+, 64 kB flash, 16 kB SRAM, USB FS Device (xtal-less)/OTG, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*5x5mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MKL27Z64VFM4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

