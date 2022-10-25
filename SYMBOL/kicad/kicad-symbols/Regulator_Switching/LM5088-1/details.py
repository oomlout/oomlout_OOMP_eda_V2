
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5088-1"
    hexID = "SZKREGULATORSWITCHINGLM5881"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5088-1', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3.4x5mm_Mask3x3mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5088.pdf', 'kicadSymbolki_keywords': 'step down buck high voltage', 'kicadSymbolki_description': 'Wide Input Range Non-Synchronous Buck Controller, Frequency Dithering, 75V, HTSSOP-16', 'kicadSymbolki_fp_filters': 'HTSSOP*1EP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Switching : LM5088-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

