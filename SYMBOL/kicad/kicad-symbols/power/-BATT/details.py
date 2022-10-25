
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "power"
    oIndex = "-BATT"
    hexID = "SZKPOWERBATT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': '#PWR', 'kicadSymbolValue': '-BATT', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'power-flag battery', 'kicadSymbolki_description': 'Power symbol creates a global label with name "-BATT"'}])
    newPart['name'].append('power : -BATT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

