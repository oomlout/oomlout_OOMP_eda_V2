
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL26Z256VMC4"
    hexID = "SZKMCUNXPKINETISMKL26Z256VMC4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL26Z256VMC4', 'kicadSymbolFootprint': 'Package_BGA:XFBGA-121_8x8mm_Layout11x11_P0.65mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL26P121M48SF4.pdf', 'kicadSymbolki_keywords': 'Kinetis KL26 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL26 series, 48-MHz/32-bit ARM Cortex-M0+, 256 kB flash, 32 kB SRAM, USB FS Device/OTG, XFBGA-121', 'kicadSymbolki_fp_filters': 'XFBGA*8x8mm*P0.65mm*'}])
    newPart['name'].append('MKL26Z256VMC4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

