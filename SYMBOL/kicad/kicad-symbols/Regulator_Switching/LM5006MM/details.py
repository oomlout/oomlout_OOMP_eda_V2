
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5006MM"
    hexID = "SZKREGULATORSWITCHINGLM56"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5006MM', 'kicadSymbolFootprint': 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5006.pdf', 'kicadSymbolki_keywords': 'Constant On-Time Buck Switching Regulator', 'kicadSymbolki_description': '600mA, 80V Constant On-Time Buck Switching Regulator, MSOP-10', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : LM5006MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

