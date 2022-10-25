
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MCP1700-1802E_SOT23"
    hexID = "SZKREGULATORLINEARMCP17182ESOT23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP1700-3002E_SOT23', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1700-1802E_SOT23', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20001826D.pdf', 'kicadSymbolki_keywords': 'regulator linear ldo', 'kicadSymbolki_description': '250mA Low Quiscent Current LDO, 1.8V output, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : MCP1700-1802E_SOT23')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

