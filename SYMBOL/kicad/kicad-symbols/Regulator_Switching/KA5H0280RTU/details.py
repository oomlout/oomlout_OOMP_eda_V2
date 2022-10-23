
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "KA5H0280RTU"
    hexID = "SZKREGULATORSWITCHINGKA5H28RTU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'KA5M0265RTU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KA5H0280RTU', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-4_Vertical', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/KA5L0265R-D.PDF', 'kicadSymbolki_keywords': 'SMPS Controller AC-DC', 'kicadSymbolki_description': '100kHz SMPS Controller, AC-DC, TO-220F-4L', 'kicadSymbolki_fp_filters': '*TO*220*4*'}])
    newPart['name'].append('KA5H0280RTU')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

