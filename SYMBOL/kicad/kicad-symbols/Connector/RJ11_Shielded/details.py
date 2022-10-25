
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ11_Shielded"
    hexID = "SZKCNRJ11SHED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '6P2C_Shielded', 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ11_Shielded', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '6P2C RJ female connector', 'kicadSymbolki_description': 'RJ connector, 6P2C (6 positions 2 connected), Shielded', 'kicadSymbolki_fp_filters': '6P2C* RJ11*'}])
    newPart['name'].append('Connector : RJ11_Shielded')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

