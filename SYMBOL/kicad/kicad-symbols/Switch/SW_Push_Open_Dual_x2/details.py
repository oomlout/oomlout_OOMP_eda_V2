
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_Push_Open_Dual_x2"
    hexID = "SZKSWITCHSWPUSHOPENDUALX2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_Push_Open_Dual_x2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'switch normally-closed pushbutton push-button', 'kicadSymbolki_description': 'Push button switch, push-to-open, generic, two pins'}])
    newPart['name'].append('Switch : SW_Push_Open_Dual_x2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

