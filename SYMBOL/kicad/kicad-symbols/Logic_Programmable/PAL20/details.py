
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_Programmable"
    oIndex = "PAL20"
    hexID = "SZKLOGICPROGRAABLEPAL2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PAL20', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'logic programmable PAL', 'kicadSymbolki_description': 'generic 20-pin Programmable Array Logic (PAL) device'}])
    newPart['name'].append('Logic_Programmable : PAL20')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

