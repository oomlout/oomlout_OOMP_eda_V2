
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_LPC"
    oIndex = "LPC1104UK"
    hexID = "SZKMCUNXPLPCLPC114UK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LPC1104UK', 'kicadSymbolFootprint': 'Package_CSP:WLCSP-16_4x4_B2.17x2.32mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/LPC1102_1104.pdf', 'kicadSymbolki_keywords': 'ARM, 32-bit, Cortex-M0, M0, NXP, microcontroller', 'kicadSymbolki_description': '32-bit ARM Cortex-M0 microcontroller, 32kB flash, 8kB SRAM', 'kicadSymbolki_fp_filters': 'WLCSP*4x4*B2.17x2.32mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_LPC : LPC1104UK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

