
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08MP16xLC"
    hexID = "SZKMCUNXPS8MC9S8MP16XLC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08MP16xLC', 'kicadSymbolFootprint': 'Package_QFP:LQFP-32_7x7mm_P0.8mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/microcontrollers/doc/ref_manual/MC9S08MP16RM.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit General Purpose Microcontroller, S08 core, 16kB Flash, 1kB RAM, LQFP-32', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.8mm*'}])
    newPart['name'].append('MCU_NXP_S08 : MC9S08MP16xLC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

