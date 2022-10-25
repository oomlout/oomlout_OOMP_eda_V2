
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx"
    oIndex = "4081"
    hexID = "SZK4XXX481"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4081', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/cd40/cd4073bms-81bms-82bms.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'CMOS And2', 'kicadSymbolki_description': 'Quad And 2 inputs', 'kicadSymbolki_fp_filters': 'DIP?14*'}])
    newPart['name'].append('4xxx : 4081')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

