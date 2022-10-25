
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MCP1802x-xx02xOT"
    hexID = "SZKREGULATORLINEARMCP182XXX2XOT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TC1017-xCT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1802x-xx02xOT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22053C.pdf', 'kicadSymbolki_keywords': 'LDO Linear Voltage Regulator', 'kicadSymbolki_description': '150mA, Tiny CMOS LDO With Shutdown, Fixed Voltage, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : MCP1802x-xx02xOT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

