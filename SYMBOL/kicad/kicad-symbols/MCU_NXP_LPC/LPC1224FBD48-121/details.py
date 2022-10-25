
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_LPC"
    oIndex = "LPC1224FBD48-121"
    hexID = "SZKMCUNXPLPCLPC1224FBD48121"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LPC1224FBD48-101', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LPC1224FBD48-121', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/LPC122X.pdf', 'kicadSymbolki_keywords': 'ARM, 32-bit, Cortex-M0, M0, NXP, microcontroller', 'kicadSymbolki_description': 'LPC122x 32-bit ARM Cortex-M0 microcontroller, 48 kB FLASH, 4 kB SRAM, LQFP-48', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_LPC : LPC1224FBD48-121')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

