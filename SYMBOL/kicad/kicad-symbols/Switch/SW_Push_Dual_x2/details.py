
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_Push_Dual_x2"
    hexID = "SZKSWITCHSWPUSHDUALX2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_Push_Dual_x2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'switch normally-open pushbutton push-button', 'kicadSymbolki_description': 'Push button switch, generic, separate symbols, four pins'}])
    newPart['name'].append('Switch : SW_Push_Dual_x2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

