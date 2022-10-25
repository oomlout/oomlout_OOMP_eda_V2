
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAMD"
    oIndex = "ATSAMD21G16A-A"
    hexID = "SZKMCUMCHIPSAMDATSAMD21G16AA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATSAMD21G15A-A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAMD21G16A-A', 'kicadSymbolFootprint': 'Package_QFP:TQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/SAM_D21_DA1_Family_Data%20Sheet_DS40001882E.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M0+ MCU Microcontroller', 'kicadSymbolki_description': 'SAM D21 Microchip SMART ARM-based Flash MCU, 48Mhz, 64K Flash, 8K SRAM, TQFP-48', 'kicadSymbolki_fp_filters': 'TQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_SAMD : ATSAMD21G16A-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

