
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08JS8CFK"
    hexID = "SZKMCUNXPS8MC9S8JS8CFK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC9S08JS16CFK', 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08JS8CFK', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_5x5mm_P0.65mm_EP3.6x3.6mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/32bit/doc/ref_manual/MC9S08JS16RM.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit USB Microcontroller, S08 core, 8kB Flash, 512B RAM, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.65mm*'}])
    newPart['name'].append('MCU_NXP_S08 : MC9S08JS8CFK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

