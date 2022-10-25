
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAMD"
    oIndex = "ATSAMD21J15B-M"
    hexID = "SZKMCUMCHIPSAMDATSAMD21J15BM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATSAMD21J15A-M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAMD21J15B-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP4.7x4.7mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/SAM_D21_DA1_Family_Data%20Sheet_DS40001882E.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M0+ MCU Microcontroller', 'kicadSymbolki_description': 'SAM D21 Microchip SMART ARM-based Flash MCU, 48Mhz, 32K Flash w/ 1K RWW, 4K SRAM, QFN-64', 'kicadSymbolki_fp_filters': 'QFN*9x9mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_SAMD : ATSAMD21J15B-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

