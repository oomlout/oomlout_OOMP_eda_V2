
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_SP3T"
    hexID = "SZKSWITCHSWSP3T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_SP3T', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'switch sp3t ON-ON-ON', 'kicadSymbolki_description': 'Switch, three position, single pole triple throw, 3 position switch, SP3T', 'kicadSymbolki_fp_filters': 'SW* SP3T*'}])
    newPart['name'].append('Switch : SW_SP3T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

