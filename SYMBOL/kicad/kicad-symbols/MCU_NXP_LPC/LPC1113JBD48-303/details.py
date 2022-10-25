
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_LPC"
    oIndex = "LPC1113JBD48-303"
    hexID = "SZKMCUNXPLPCLPC1113JBD4833"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LPC1113FBD48-301', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LPC1113JBD48-303', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/LPC111X.pdf', 'kicadSymbolki_keywords': 'ARM, 32-bit, Cortex-M0, M0, NXP, microcontroller', 'kicadSymbolki_description': '32-bit ARM Cortex-M0 microcontroller, 24KB flash, 8KB SRAM, power profile', 'kicadSymbolki_fp_filters': '*QFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_LPC : LPC1113JBD48-303')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

