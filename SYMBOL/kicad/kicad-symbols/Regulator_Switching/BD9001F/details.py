
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "BD9001F"
    hexID = "SZKREGULATORSWITCHINGBD91F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BD9001F', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://rohmfs.rohm.com/en/products/databook/datasheet/ic/power/switching_regulator/bd9778f-e.pdf', 'kicadSymbolki_keywords': 'DC-DC Step-Down Switching Regulator', 'kicadSymbolki_description': '48V 2A, Flexible Step-Down Switching Regulator, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : BD9001F')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

