
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTC7138"
    hexID = "SZKREGULATORSWITCHINGLTC7138"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC7138', 'kicadSymbolFootprint': 'Package_SO:Linear_MSOP-12-16-1EP_3x4mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/7138f.pdf', 'kicadSymbolki_keywords': 'buck dc-dc switcher switching', 'kicadSymbolki_description': '400mA High efficiency 140V step-down converter, MSOP-16(12)', 'kicadSymbolki_fp_filters': 'Linear*MSOP*12*16*EP*3x4mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : LTC7138')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

