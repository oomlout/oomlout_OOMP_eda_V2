
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_DPST_Temperature"
    hexID = "SZKSWITCHSWDPSTTEMPERATURE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_DPST_Temperature', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'temperature switch dual double-pole single-throw OFF-ON', 'kicadSymbolki_description': 'Double Pole Single Throw (DPST) Switch, temperature dependent'}])
    newPart['name'].append('Switch : SW_DPST_Temperature')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

