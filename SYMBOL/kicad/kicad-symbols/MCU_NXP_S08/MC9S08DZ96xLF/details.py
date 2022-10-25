
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08DZ96xLF"
    hexID = "SZKMCUNXPS8MC9S8DZ96XLF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC9S08DZ128xLF', 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08DZ96xLF', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/microcontrollers/doc/data_sheet/MC9S08DZ128.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit Cost-Effective Microcontroller, S08 core, 96kB Flash, 6kB RAM, 2kB EEPROM, LQFP-48', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_S08 : MC9S08DZ96xLF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

