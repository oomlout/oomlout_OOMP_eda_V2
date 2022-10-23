
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAMD"
    oIndex = "ATSAMD21J16B-C"
    hexID = "SZKMCUMCHIPSAMDATSAMD21J16BC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATSAMD21J15B-C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAMD21J16B-C', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-64_5x5mm_Layout8x8_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/SAM_D21_DA1_Family_Data%20Sheet_DS40001882E.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M0+ MCU Microcontroller', 'kicadSymbolki_description': 'SAM D21 Microchip SMART ARM-based Flash MCU, 48Mhz, 64K Flash w/ 2K RWW, 8K SRAM, UFBGA-64', 'kicadSymbolki_fp_filters': 'UFBGA*5x5mm*Layout8x8*P0.5mm*'}])
    newPart['name'].append('ATSAMD21J16B-C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

