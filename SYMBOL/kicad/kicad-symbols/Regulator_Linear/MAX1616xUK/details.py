
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MAX1616xUK"
    hexID = "SZKREGULATORLINEARMAX1616XUK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX1616xUK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX1615-MAX1616.pdf', 'kicadSymbolki_keywords': 'Linear Voltage Regulator', 'kicadSymbolki_description': 'High Voltage, Low Power Linear Regulator for Notebook PCs - Adjustable', 'kicadSymbolki_fp_filters': 'SOT?23?5*'}])
    newPart['name'].append('Regulator_Linear : MAX1616xUK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

