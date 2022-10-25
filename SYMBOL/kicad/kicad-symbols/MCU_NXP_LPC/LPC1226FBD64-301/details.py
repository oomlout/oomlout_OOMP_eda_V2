
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_LPC"
    oIndex = "LPC1226FBD64-301"
    hexID = "SZKMCUNXPLPCLPC1226FBD6431"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LPC1224FBD64-101', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LPC1226FBD64-301', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/LPC122X.pdf', 'kicadSymbolki_keywords': 'ARM, 32-bit, Cortex-M0, M0, NXP, microcontroller', 'kicadSymbolki_description': 'LPC122x 32-bit ARM Cortex-M0 microcontroller, 96 kB FLASH, 8 kB SRAM, LQFP-64', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_LPC : LPC1226FBD64-301')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

