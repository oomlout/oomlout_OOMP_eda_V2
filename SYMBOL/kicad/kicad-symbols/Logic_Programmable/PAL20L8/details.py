
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_Programmable"
    oIndex = "PAL20L8"
    hexID = "SZKLOGICPROGRAABLEPAL2L8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PAL20L8', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'PAL PLD 20L8', 'kicadSymbolki_description': 'Programmable Logic Array, DIP-24', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('Logic_Programmable : PAL20L8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

