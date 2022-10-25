
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "LMV7275"
    hexID = "SZKCOMPARATORLMV7275"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LMV331', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMV7275', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmv7275.pdf', 'kicadSymbolki_keywords': 'cmp', 'kicadSymbolki_description': 'Single, 1.8V Low Power, Rail-to-Rail Input, Open Collector Output Comparator, SOT-23-5/SC-70-5', 'kicadSymbolki_fp_filters': 'SOT?23* *SC?70*'}])
    newPart['name'].append('Comparator : LMV7275')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

