
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx"
    oIndex = "4017"
    hexID = "SZK4XXX417"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4017', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/cd40/cd4017bms-22bms.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'CNT CNT10', 'kicadSymbolki_description': 'Johnson Counter ( 10 outputs )', 'kicadSymbolki_fp_filters': 'DIP?16*'}])
    newPart['name'].append('4xxx : 4017')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

