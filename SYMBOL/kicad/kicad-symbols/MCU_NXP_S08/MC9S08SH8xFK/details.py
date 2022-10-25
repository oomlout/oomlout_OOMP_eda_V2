
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08SH8xFK"
    hexID = "SZKMCUNXPS8MC9S8SH8XFK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08SH8xFK', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/microcontrollers/doc/data_sheet/MC9S08SH8.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit General Purpose Microcontroller, S08 core, 8kB Flash, 512B RAM, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_S08 : MC9S08SH8xFK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

