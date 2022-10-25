
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MCP1703A-1502_SOT223"
    hexID = "SZKREGULATORLINEARMCP173A152SOT223"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP1703A-3302_SOT223', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1703A-1502_SOT223', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005122B.pdf', 'kicadSymbolki_keywords': 'REGULATOR LDO', 'kicadSymbolki_description': 'Low Quiescent Current LDO Regulator, 1.5V, 250mA, Vin<=16V, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*TabPin2*'}])
    newPart['name'].append('Regulator_Linear : MCP1703A-1502_SOT223')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

