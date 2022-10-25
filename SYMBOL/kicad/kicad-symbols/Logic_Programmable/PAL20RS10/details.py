
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_Programmable"
    oIndex = "PAL20RS10"
    hexID = "SZKLOGICPROGRAABLEPAL2RS1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PAL20RS10', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'PAL PLD 20RS10', 'kicadSymbolki_description': 'Programmable Logic Array, DIP-24 (Narrow)', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('Logic_Programmable : PAL20RS10')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

