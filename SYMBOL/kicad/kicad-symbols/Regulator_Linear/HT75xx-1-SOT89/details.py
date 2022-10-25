
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "HT75xx-1-SOT89"
    hexID = "SZKREGULATORLINEARHT75XX1SOT89"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HT75xx-1-SOT89', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-89-3', 'kicadSymbolDatasheet': 'https://www.holtek.com/documents/10179/116711/HT75xx-1v250.pdf', 'kicadSymbolki_keywords': '100mA LDO Regulator Fixed Positive', 'kicadSymbolki_description': '100mA Low Dropout Voltage Regulator, Fixed Output, SOT89', 'kicadSymbolki_fp_filters': 'SOT?89*'}])
    newPart['name'].append('Regulator_Linear : HT75xx-1-SOT89')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

