
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MK20FX512VMD12"
    hexID = "SZKMCUNXPKINETISMK2FX512VMD12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MK20FX512VMD12', 'kicadSymbolFootprint': 'Package_BGA:BGA-144_13.0x13.0mm_Layout12x12_P1.0mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/K20P144M120SF3.pdf', 'kicadSymbolki_keywords': 'Kinetis K20 ARM Cortex M4', 'kicadSymbolki_description': 'Kinetis K20 series, 120-MHz/32-bit ARM Cortex-M4, 512 kB flash, 512 kB FlexNVM, 128 kB SRAM, 16 kB FlexRAM, USB HS+FS Device/OTG, MAPBGA-144', 'kicadSymbolki_fp_filters': 'BGA*13.0x13.0mm*Layout12x12*P1.0mm*'}])
    newPart['name'].append('MK20FX512VMD12')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

