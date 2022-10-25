
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "DB15_Female"
    hexID = "SZKCNDB15FEMALE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'DB15_Female', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'female D-SUB connector', 'kicadSymbolki_description': '15-pin female D-SUB connector (low-density/2 columns)', 'kicadSymbolki_fp_filters': 'DSUB*Female*'}])
    newPart['name'].append('Connector : DB15_Female')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

