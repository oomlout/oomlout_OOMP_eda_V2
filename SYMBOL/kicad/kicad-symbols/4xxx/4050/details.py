
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx"
    oIndex = "4050"
    hexID = "SZK4XXX45"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4050', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/intersil/documents/cd40/cd4050bms.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'CMOS BUFFER', 'kicadSymbolki_description': 'Hex Buffer', 'kicadSymbolki_fp_filters': 'DIP?16*'}])
    newPart['name'].append('4xxx : 4050')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

