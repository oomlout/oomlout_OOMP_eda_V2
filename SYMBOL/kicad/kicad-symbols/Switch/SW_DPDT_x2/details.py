
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_DPDT_x2"
    hexID = "SZKSWITCHSWDPDTX2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_DPDT_x2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'switch dual-pole double-throw DPDT spdt ON-ON', 'kicadSymbolki_description': 'Switch, dual pole double throw, separate symbols', 'kicadSymbolki_fp_filters': 'SW*DPDT*'}])
    newPart['name'].append('Switch : SW_DPDT_x2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

