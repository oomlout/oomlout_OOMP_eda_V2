
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_SPDT_MSM"
    hexID = "SZKSWITCHSWSPDTMSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_SPDT_MSM', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'switch spdt single-pole double-throw ON-OFF-ON', 'kicadSymbolki_description': 'Switch, single pole double throw, center OFF position'}])
    newPart['name'].append('Switch : SW_SPDT_MSM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

