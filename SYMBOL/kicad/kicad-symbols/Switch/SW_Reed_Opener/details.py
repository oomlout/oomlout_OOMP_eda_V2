
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_Reed_Opener"
    hexID = "SZKSWITCHSWREEDOPENER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_Reed_Opener', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'reed magnetic switch', 'kicadSymbolki_description': 'reed switch, default-closed'}])
    newPart['name'].append('Switch : SW_Reed_Opener')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

