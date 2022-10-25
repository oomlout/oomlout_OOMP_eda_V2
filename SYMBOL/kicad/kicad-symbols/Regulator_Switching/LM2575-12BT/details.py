
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2575-12BT"
    hexID = "SZKREGULATORSWITCHINGLM257512BT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2576HVT-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2575-12BT', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_Vertical', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/lm2575.pdf', 'kicadSymbolki_keywords': 'Buck regulator Switcher', 'kicadSymbolki_description': 'Fixed 12V 52kHz Simple 1A Buck Regulator, TO-220-5', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Regulator_Switching : LM2575-12BT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

