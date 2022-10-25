
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "171050601"
    hexID = "SZKREGULATORSWITCHING171561"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '171050601', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-7_TabPin8', 'kicadSymbolDatasheet': 'https://katalog.we-online.de/pm/datasheet/171050601.pdf', 'kicadSymbolki_keywords': 'power module regulator', 'kicadSymbolki_description': 'MagI3C Power Module, Variable Step Down Regulator Module, 6 to 36V Input Voltage, 0.8 to 6V, 5A Output, TO-263', 'kicadSymbolki_fp_filters': 'TO*263*TabPin8*'}])
    newPart['name'].append('Regulator_Switching : 171050601')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

