
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74CBTLV3861"
    hexID = "SZK74XX74CBTLV3861"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74CBTLV3861', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74cbtlv3861', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'bus', 'kicadSymbolki_description': 'Low-voltage 10-bit FET Bus switch', 'kicadSymbolki_fp_filters': 'DIP?24*'}])
    newPart['name'].append('74xx : 74CBTLV3861')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

