
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT1373HVCS8"
    hexID = "SZKREGULATORSWITCHINGLT1373HVCS8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1372CS8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1373HVCS8', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1373fbs.pdf', 'kicadSymbolki_keywords': 'Switching Regulator Adjustable', 'kicadSymbolki_description': '1.5A Low Supply Current High Efficiency Switching Regulators, 250kHz, 42V Switch Voltage, Adjustable Output Voltage, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : LT1373HVCS8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

