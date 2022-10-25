
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL28Z512VDC7"
    hexID = "SZKMCUNXPKINETISMKL28Z512VDC7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL28Z512VDC7', 'kicadSymbolFootprint': 'Package_BGA:XFBGA-121_8x8mm_Layout11x11_P0.65mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/MKL28Z512Vxx7.pdf', 'kicadSymbolki_keywords': 'Kinetis KL28 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL28 series, 72...96-MHz/32-bit ARM Cortex-M0+, 512 kB flash, 128 kB SRAM, USB FS Device (xtal-less), XFBGA-121', 'kicadSymbolki_fp_filters': 'XFBGA*8x8mm*P0.65mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MKL28Z512VDC7')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

