
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "power"
    oIndex = "+3.3VDAC"
    hexID = "SZKPOWER+33VDAC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': '#PWR', 'kicadSymbolValue': '+3.3VDAC', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'power-flag', 'kicadSymbolki_description': 'Power symbol creates a global label with name "+3.3VDAC"'}])
    newPart['name'].append('power : +3.3VDAC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

