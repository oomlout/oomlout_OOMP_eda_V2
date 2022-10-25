
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL26Z256VMP4"
    hexID = "SZKMCUNXPKINETISMKL26Z256VMP4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL26Z256VMP4', 'kicadSymbolFootprint': 'Package_BGA:XFBGA-64_5.0x5.0mm_Layout8x8_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL26P121M48SF4.pdf', 'kicadSymbolki_keywords': 'Kinetis KL26 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL26 series, 48-MHz/32-bit ARM Cortex-M0+, 256 kB flash, 32 kB SRAM, USB FS Device/OTG, XFBGA-64', 'kicadSymbolki_fp_filters': 'XFBGA*5.0x5.0mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MKL26Z256VMP4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

