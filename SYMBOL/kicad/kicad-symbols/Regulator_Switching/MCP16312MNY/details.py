
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MCP16312MNY"
    hexID = "SZKREGULATORSWITCHINGMCP16312MNY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP16311MNY', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP16312MNY', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x2mm_P0.5mm_EP1.75x1.45mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005255B.pdf', 'kicadSymbolki_keywords': 'switching buck converter power-supply voltage regulator', 'kicadSymbolki_description': '1A Output Voltage, 30V Input, integrated switch step-down regulator, PWM modulation, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : MCP16312MNY')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

