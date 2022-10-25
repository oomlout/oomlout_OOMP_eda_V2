
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "DB15_Female_HighDensity_MountingHoles"
    hexID = "SZKCNDB15FEMALEHIGHDENSITYHOLS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'DB15_Female_HighDensity_MountingHoles', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'connector db15 female D-SUB VGA', 'kicadSymbolki_description': '15-pin female D-SUB connector, High density (3 columns), Triple Row, Generic, VGA-connector, Mounting Hole', 'kicadSymbolki_fp_filters': 'DSUB*Female*'}])
    newPart['name'].append('Connector : DB15_Female_HighDensity_MountingHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

