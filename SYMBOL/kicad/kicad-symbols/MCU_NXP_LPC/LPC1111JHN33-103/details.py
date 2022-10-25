
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_LPC"
    oIndex = "LPC1111JHN33-103"
    hexID = "SZKMCUNXPLPCLPC1111JHN3313"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LPC1111FHN33-101', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LPC1111JHN33-103', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_7x7mm_P0.65mm_EP4.7x4.7mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.nxp.com/documents/data_sheet/LPC111X.pdf', 'kicadSymbolki_keywords': 'ARM, 32-bit, Cortex-M0, M0, NXP, microcontroller', 'kicadSymbolki_description': '32-bit ARM Cortex-M0 microcontroller, 8KB flash, 2KB SRAM', 'kicadSymbolki_fp_filters': '*QFN*7x7mm*P0.65mm*'}])
    newPart['name'].append('MCU_NXP_LPC : LPC1111JHN33-103')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

