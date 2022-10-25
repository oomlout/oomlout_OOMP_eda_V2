
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS181"
    hexID = "SZK74XX74LS181"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS181', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '74xx/74F181.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'TTL ALU ARITH', 'kicadSymbolki_description': 'Arithmetic logic unit', 'kicadSymbolki_fp_filters': 'DIP?24*'}])
    newPart['name'].append('74xx : 74LS181')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

