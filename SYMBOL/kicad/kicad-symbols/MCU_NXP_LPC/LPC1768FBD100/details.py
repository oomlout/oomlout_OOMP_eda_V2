
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_LPC"
    oIndex = "LPC1768FBD100"
    hexID = "SZKMCUNXPLPCLPC1768FBD1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LPC1763FBD100', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LPC1768FBD100', 'kicadSymbolFootprint': 'Package_QFP:LQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/LPC1769_68_67_66_65_64_63.pdf', 'kicadSymbolki_keywords': 'ARM, 32-bit, Cortex-M3, M3, NXP, microcontroller', 'kicadSymbolki_description': '32-bit ARM Cortex-M3 microcontroller, 512KB flash, 64KB RAM, Ethernet, USB', 'kicadSymbolki_fp_filters': '*QFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_LPC : LPC1768FBD100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

