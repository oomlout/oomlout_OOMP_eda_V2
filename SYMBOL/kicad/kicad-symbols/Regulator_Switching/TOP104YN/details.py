
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TOP104YN"
    hexID = "SZKREGULATORSWITCHINGTOP14YN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TOP100YN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TOP104YN', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/top100.pdf', 'kicadSymbolki_keywords': 'Three-terminal Off-line PWM Switch', 'kicadSymbolki_description': 'TOPSwitch Family, 60W Max Output Power, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Regulator_Switching : TOP104YN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

