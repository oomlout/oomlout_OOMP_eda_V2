
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "DB9_Female_MountingHoles"
    hexID = "SZKCNDB9FEMALEHOLS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'DB9_Female_MountingHoles', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'connector female D-SUB', 'kicadSymbolki_description': '9-pin female D-SUB connector, Mounting Hole', 'kicadSymbolki_fp_filters': 'DSUB*Female*'}])
    newPart['name'].append('Connector : DB9_Female_MountingHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

