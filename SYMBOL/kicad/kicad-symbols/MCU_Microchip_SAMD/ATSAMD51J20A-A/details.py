
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAMD"
    oIndex = "ATSAMD51J20A-A"
    hexID = "SZKMCUMCHIPSAMDATSAMD51J2AA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATSAMD51J18A-A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAMD51J20A-A', 'kicadSymbolFootprint': 'Package_QFP:TQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/60001507E.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M4F MCU Microcontroller', 'kicadSymbolki_description': 'SAM D51 Microchip SMART ARM Cortex-M4F-based MCU, 1024K Flash, 256K SRAM, TQFP-64', 'kicadSymbolki_fp_filters': 'TQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_SAMD : ATSAMD51J20A-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

