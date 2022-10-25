
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MCP1804x-2502xMT"
    hexID = "SZKREGULATORLINEARMCP184X252XMT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP1804x-1802xMT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1804x-2502xMT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-89-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20002200D.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo fixed positive', 'kicadSymbolki_description': '150mA, 28V LDO Regulator With Shutdown, 2.5V Fixed Output, SOT-89-5', 'kicadSymbolki_fp_filters': 'SOT?89*'}])
    newPart['name'].append('Regulator_Linear : MCP1804x-2502xMT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

