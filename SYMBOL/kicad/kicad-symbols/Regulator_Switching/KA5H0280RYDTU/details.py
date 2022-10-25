
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "KA5H0280RYDTU"
    hexID = "SZKREGULATORSWITCHINGKA5H28RYDTU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'KA5M0265RYDTU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KA5H0280RYDTU', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:ONSemi_TO-220F-4L_Forming', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/KA5L0265R-D.PDF', 'kicadSymbolki_keywords': 'SMPS Controller AC-DC', 'kicadSymbolki_description': '100kHz SMPS Controller, AC-DC, TO-220F-4L(Forming)', 'kicadSymbolki_fp_filters': '*TO*220*4*'}])
    newPart['name'].append('Regulator_Switching : KA5H0280RYDTU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

