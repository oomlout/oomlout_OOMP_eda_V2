
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT3748xMS"
    hexID = "SZKREGULATORSWITCHINGLT3748XMS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3748xMS', 'kicadSymbolFootprint': 'Package_SO:Linear_MSOP-12-16_3x4mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3748fb.pdf', 'kicadSymbolki_keywords': 'isolated flyback controller', 'kicadSymbolki_description': '100V Isolated Flyback Controller, MSOP-16', 'kicadSymbolki_fp_filters': 'Linear*MSOP*3x4mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : LT3748xMS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

