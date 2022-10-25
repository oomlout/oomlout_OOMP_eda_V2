
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM26480SQ"
    hexID = "SZKREGULATORSWITCHINGLM2648SQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM26480SQ', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm26480.pdf', 'kicadSymbolki_keywords': 'Dual Buck Regulator LDO 2MHz 1.5A 300mA', 'kicadSymbolki_description': 'Dual 1.5A 2MHz Buck Regulators and Dual 300mA LDOs, WQFN-24', 'kicadSymbolki_fp_filters': 'WQFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : LM26480SQ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

