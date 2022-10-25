
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08AW48xFGE"
    hexID = "SZKMCUNXPS8MC9S8AW48XFGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC9S08AC128xFGE', 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08AW48xFGE', 'kicadSymbolFootprint': 'Package_QFP:LQFP-44_10x10mm_P0.8mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/microcontrollers/doc/data_sheet/MC9S08AW60.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit General Purpose Microcontroller, S08 core, 48kB Flash, 2kB RAM, LQFP-44', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.8mm*'}])
    newPart['name'].append('MCU_NXP_S08 : MC9S08AW48xFGE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

