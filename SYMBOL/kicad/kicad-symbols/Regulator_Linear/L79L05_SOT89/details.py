
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "L79L05_SOT89"
    hexID = "SZKREGULATORLINEARL79L5SOT89"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L79L05_SOT89', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-89-3', 'kicadSymbolDatasheet': 'http://www.farnell.com/datasheets/1827870.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator 100mA Negative', 'kicadSymbolki_description': 'Negative 100mA -30V Linear Regulator, Fixed Output -5V, SOT-89', 'kicadSymbolki_fp_filters': 'SOT?89*'}])
    newPart['name'].append('Regulator_Linear : L79L05_SOT89')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

