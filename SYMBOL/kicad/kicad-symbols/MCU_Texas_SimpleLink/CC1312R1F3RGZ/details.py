
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_SimpleLink"
    oIndex = "CC1312R1F3RGZ"
    hexID = "SZKMCUTEXASSIMPLELINKCC1312R1F3RGZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CC1312R1F3RGZ', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-48-1EP_7x7mm_P0.5mm_EP5.15x5.15mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/cc1312r.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M4 MCU Microcontroller', 'kicadSymbolki_description': 'ARM Cortex-M4 SimpleLink High-Performance Sub-1GHz Wireless MCU, 48MHz, 352KB Flash, 80KB SRAM, 8KB Cache SRAM, 1.8-3.6V, 30 GPIO, VQFN-48', 'kicadSymbolki_fp_filters': 'VQFN*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('CC1312R1F3RGZ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

