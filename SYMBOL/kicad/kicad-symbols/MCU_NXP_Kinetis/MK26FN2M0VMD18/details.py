
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MK26FN2M0VMD18"
    hexID = "SZKMCUNXPKINETISMK26FN2MVMD18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MK26FN2M0VMD18', 'kicadSymbolFootprint': 'Package_BGA:BGA-144_13.0x13.0mm_Layout12x12_P1.0mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/K26P169M180SF5.pdf', 'kicadSymbolki_keywords': 'Kinetis K26 ARM Cortex M4', 'kicadSymbolki_description': 'Kinetis K26 series, 180-MHz/32-bit ARM Cortex-M4, 2048 kB flash, 256 kB SRAM, USB HS+FS Device/OTG, MAPBGA-144', 'kicadSymbolki_fp_filters': 'BGA*13.0x13.0mm*Layout12x12*P1.0mm*'}])
    newPart['name'].append('MK26FN2M0VMD18')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

