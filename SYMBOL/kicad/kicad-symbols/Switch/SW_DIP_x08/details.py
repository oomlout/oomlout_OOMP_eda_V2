
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_DIP_x08"
    hexID = "SZKSWITCHSWDIPX8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_DIP_x08', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'dip switch', 'kicadSymbolki_description': '8x DIP Switch, Single Pole Single Throw (SPST) switch, small symbol', 'kicadSymbolki_fp_filters': 'SW?DIP?x8*'}])
    newPart['name'].append('Switch : SW_DIP_x08')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

