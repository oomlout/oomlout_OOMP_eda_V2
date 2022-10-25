
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAME"
    oIndex = "ATSAME70N20A-AN"
    hexID = "SZKMCUMCHIPSAMEATSAME7N2AAN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATSAME70N21A-AN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAME70N20A-AN', 'kicadSymbolFootprint': 'Package_QFP:LQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/SAM-E70-S70-V70-V71-Family-Data-Sheet-DS60001527D.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M7 MCU Microcontroller', 'kicadSymbolki_description': 'SAM E70 Microchip SMART ARM Cortex-M7-based MCU, 1024K Flash, 384K SRAM, LQFP100', 'kicadSymbolki_fp_filters': 'LQFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_SAME : ATSAME70N20A-AN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

