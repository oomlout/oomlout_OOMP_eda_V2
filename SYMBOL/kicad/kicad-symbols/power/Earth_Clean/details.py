
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "power"
    oIndex = "Earth_Clean"
    hexID = "SZKPOWEREARTHCLEAN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': '#PWR', 'kicadSymbolValue': 'Earth_Clean', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'power-flag ground gnd clean signal', 'kicadSymbolki_description': 'Power symbol creates a global label with name "Earth_Clean"'}])
    newPart['name'].append('power : Earth_Clean')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

