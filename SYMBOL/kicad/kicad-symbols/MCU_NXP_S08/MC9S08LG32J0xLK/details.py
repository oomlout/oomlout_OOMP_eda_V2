
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08LG32J0xLK"
    hexID = "SZKMCUNXPS8MC9S8LG32JXLK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08LG32J0xLK', 'kicadSymbolFootprint': 'Package_QFP:TQFP-80_14x14mm_P0.65mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/microcontrollers/doc/ref_manual/MC9S08LG32RM.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit Segment LCD Microcontroller, S08 core, 32kB Flash, 1984B RAM, LQFP-80', 'kicadSymbolki_fp_filters': 'TQFP*14x14mm*P0.65mm*'}])
    newPart['name'].append('MCU_NXP_S08 : MC9S08LG32J0xLK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

