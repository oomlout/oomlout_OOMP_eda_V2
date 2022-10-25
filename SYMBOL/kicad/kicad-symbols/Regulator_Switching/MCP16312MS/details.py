
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MCP16312MS"
    hexID = "SZKREGULATORSWITCHINGMCP16312MS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP16311MS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP16312MS', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005255B.pdf', 'kicadSymbolki_keywords': 'switching buck converter power-supply voltage regulator', 'kicadSymbolki_description': '1A Output Voltage, 30V Input, integrated switch step-down regulator with, modulation, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Switching : MCP16312MS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

