
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "TL3116"
    hexID = "SZKCOMPARATORTL3116"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TL3116', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tl3116.pdf', 'kicadSymbolki_keywords': 'cmp push-pull complementary', 'kicadSymbolki_description': 'Single Ultra-Fast Low-Power Precision Comparators, SOIC-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Comparator : TL3116')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

