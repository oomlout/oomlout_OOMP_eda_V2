
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTM8063"
    hexID = "SZKREGULATORSWITCHINGLTM863"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTM8063', 'kicadSymbolFootprint': 'Package_BGA:Analog_BGA-28_4.0x6.25mm_Layout4x7_P0.8mm_Ball0.45mm_Pad0.4', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/8063fa.pdf', 'kicadSymbolki_keywords': 'uModule DCDC', 'kicadSymbolki_description': '40VIN, 2A Silent Switcher µModule Regulator, BGA-28', 'kicadSymbolki_fp_filters': 'Analog*BGA*4.0x6.25mm*'}])
    newPart['name'].append('Regulator_Switching : LTM8063')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

