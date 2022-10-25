
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_LPC"
    oIndex = "LPC2141FBD64"
    hexID = "SZKMCUNXPLPCLPC2141FBD64"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LPC2141FBD64', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/LPC2141_42_44_46_48.pdf', 'kicadSymbolki_keywords': 'ARM, 16-bit, 32-bit, ARM7, NXP, microcontroller', 'kicadSymbolki_description': '16-bit/32-bit ARM7TDMI-S microcontroller, 32kB flash, 8kB RAM', 'kicadSymbolki_fp_filters': '*LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_LPC : LPC2141FBD64')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

