
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAME"
    oIndex = "ATSAME70Q19A-AN"
    hexID = "SZKMCUMCHIPSAMEATSAME7Q19AAN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATSAME70Q21A-AN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAME70Q19A-AN', 'kicadSymbolFootprint': 'Package_QFP:LQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/SAM-E70-S70-V70-V71-Family-Data-Sheet-DS60001527D.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M7 MCU Microcontroller', 'kicadSymbolki_description': 'SAM E70 Microchip SMART ARM Cortex-M7-based MCU, 512K Flash, 256K SRAM, LQFP144', 'kicadSymbolki_fp_filters': 'LQFP*20x20mm*P0.5mm*'}])
    newPart['name'].append('ATSAME70Q19A-AN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

