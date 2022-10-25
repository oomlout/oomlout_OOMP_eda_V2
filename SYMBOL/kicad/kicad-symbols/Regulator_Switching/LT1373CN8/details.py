
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT1373CN8"
    hexID = "SZKREGULATORSWITCHINGLT1373CN8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1372CN8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1373CN8', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1373fbs.pdf', 'kicadSymbolki_keywords': 'Switching Regulator Adjustable', 'kicadSymbolki_description': '1.5A Low Supply Current High Efficiency Switching Regulators, 250kHz, 35V Switch Voltage, Adjustable Output Voltage, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Switching : LT1373CN8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

