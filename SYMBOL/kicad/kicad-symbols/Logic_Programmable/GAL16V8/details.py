
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_Programmable"
    oIndex = "GAL16V8"
    hexID = "SZKLOGICPROGRAABLEGAL16V8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'GAL16V8', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'GAL PLD 16V8', 'kicadSymbolki_description': 'Programmable Logic Array, DIP-20/SOIC-20/PLCC-20', 'kicadSymbolki_fp_filters': 'DIP* PDIP* SOIC* SO* PLCC*'}])
    newPart['name'].append('Logic_Programmable : GAL16V8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

