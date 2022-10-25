
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08AC8xFJE"
    hexID = "SZKMCUNXPS8MC9S8AC8XFJE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC9S08AC60xFJE', 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08AC8xFJE', 'kicadSymbolFootprint': 'Package_QFP:LQFP-32_7x7mm_P0.8mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/microcontrollers/doc/data_sheet/MC9S08AC16.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit Flexis Microcontroller, S08 core, 8kB Flash, 768B RAM, LQFP-32', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.8mm*'}])
    newPart['name'].append('MCU_NXP_S08 : MC9S08AC8xFJE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

