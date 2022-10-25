
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08QA2CFQE"
    hexID = "SZKMCUNXPS8MC9S8QA2CFQE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC9S08QA4CFQE', 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08QA2CFQE', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_4x4mm_P0.8mm_EP2.5x3.6mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/microcontrollers/doc/ref_manual/MC9S08QA4RM.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit Small Package Microcontroller, S08 core, 2kB Flash, 160B RAM, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*4x4mm*P0.8mm*'}])
    newPart['name'].append('MCU_NXP_S08 : MC9S08QA2CFQE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

