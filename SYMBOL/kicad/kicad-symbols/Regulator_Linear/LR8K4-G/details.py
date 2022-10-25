
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LR8K4-G"
    hexID = "SZKREGULATORLINEARLR8K4G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LR8K4-G', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005399B.pdf', 'kicadSymbolki_keywords': 'High-Voltage Regulator Adjustable Positive', 'kicadSymbolki_description': '30mA 450V High-Voltage Linear Regulator (Adjustable), TO-252 (D-PAK)', 'kicadSymbolki_fp_filters': 'TO*252*'}])
    newPart['name'].append('Regulator_Linear : LR8K4-G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

