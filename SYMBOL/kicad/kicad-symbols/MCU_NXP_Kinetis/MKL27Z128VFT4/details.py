
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL27Z128VFT4"
    hexID = "SZKMCUNXPKINETISMKL27Z128VFT4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MKL27Z256VFT4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL27Z128VFT4', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.15x5.15mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL27P64M48SF6.pdf', 'kicadSymbolki_keywords': 'Kinetis KL27 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL27 series, 48-MHz/32-bit ARM Cortex-M0+, 128 kB flash, 32 kB SRAM, USB FS Device (xtal-less)/OTG, QFN-48', 'kicadSymbolki_fp_filters': 'QFN*7x7mm*P0.5mm*'}])
    newPart['name'].append('MKL27Z128VFT4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

