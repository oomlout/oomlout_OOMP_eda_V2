
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM3407MY"
    hexID = "SZKREGULATORSWITCHINGLM347MY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM3407MY', 'kicadSymbolFootprint': 'Package_SO:MSOP-8-1EP_3x3mm_P0.65mm_EP1.73x1.85mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm3407.pdf', 'kicadSymbolki_keywords': 'LED Step-Down Switching Regulator', 'kicadSymbolki_description': 'LED Lighting CC Floating Buck Switching Regulator, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*1EP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Switching : LM3407MY')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

