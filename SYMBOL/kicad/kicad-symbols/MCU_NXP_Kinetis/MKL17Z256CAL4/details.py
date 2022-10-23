
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL17Z256CAL4"
    hexID = "SZKMCUNXPKINETISMKL17Z256CAL4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL17Z256CAL4', 'kicadSymbolFootprint': 'Package_CSP:WLCSP-36_2.82x2.67mm_Layout6x6_P0.4mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL17P64M48SF6.pdf', 'kicadSymbolki_keywords': 'Kinetis KL17 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL17 series, 48-MHz/32-bit ARM Cortex-M0+, 256 kB flash, 32 kB SRAM, FlexIO, WLCSP-36', 'kicadSymbolki_fp_filters': 'WLCSP*2.82x2.67mm*P0.4mm*'}])
    newPart['name'].append('MKL17Z256CAL4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

