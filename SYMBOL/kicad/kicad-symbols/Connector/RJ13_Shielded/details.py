
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ13_Shielded"
    hexID = "SZKCNRJ13SHED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '6P4C_Shielded', 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ13_Shielded', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '6P4C RJ female connector', 'kicadSymbolki_description': 'RJ connector, 6P4C (6 positions 4 connected), Shielded', 'kicadSymbolki_fp_filters': '6P4C* RJ13* RJ14*'}])
    newPart['name'].append('Connector : RJ13_Shielded')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

