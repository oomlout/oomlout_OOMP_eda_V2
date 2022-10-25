
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "LMV331"
    hexID = "SZKCOMPARATORLMV331"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMV331', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmv331.pdf', 'kicadSymbolki_keywords': 'single comparator', 'kicadSymbolki_description': 'Single General-Purpose Low-Voltage Comparator, SOT-23-5/SC-70-5', 'kicadSymbolki_fp_filters': 'SOT?23* *SC?70*'}])
    newPart['name'].append('Comparator : LMV331')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

