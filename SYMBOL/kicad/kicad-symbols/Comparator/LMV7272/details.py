
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "LMV7272"
    hexID = "SZKCOMPARATORLMV7272"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMV7272', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-8_1.5195x1.5195mm_Layout3x3_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmv7272.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'cmp', 'kicadSymbolki_description': 'Dual, 1.8V Low Power, Rail-to-Rail Input, Push-Pull Output Comparator, DSBGA-8', 'kicadSymbolki_fp_filters': 'Texas*DSBGA*1.5195x1.5195*Layout3x3*P0.5mm*'}])
    newPart['name'].append('Comparator : LMV7272')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

