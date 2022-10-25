
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "MM74C923"
    hexID = "SZK74XX74C923"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MM74C923', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/snMM74C923', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'encoder', 'kicadSymbolki_description': '20-key encoder', 'kicadSymbolki_fp_filters': 'DIP?20*'}])
    newPart['name'].append('74xx : MM74C923')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

