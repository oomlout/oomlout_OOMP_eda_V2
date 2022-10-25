
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAME"
    oIndex = "ATSAME51J18A-A"
    hexID = "SZKMCUMCHIPSAMEATSAME51J18AA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAME51J18A-A', 'kicadSymbolFootprint': 'Package_QFP:TQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/60001507E.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M4F MCU Microcontroller', 'kicadSymbolki_description': 'SAM E51 Microchip SMART ARM Cortex-M4F-based MCU, 256K Flash, 128K SRAM, TQFP-64', 'kicadSymbolki_fp_filters': 'TQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_SAME : ATSAME51J18A-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

