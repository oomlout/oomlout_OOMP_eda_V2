
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "MCP6401T-xLT"
    hexID = "SZKAMPLIFIEROPERATIONALMCP641TXLT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP6001x-LT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP6401T-xLT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/22229d.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': '1 MHz, 45 µA Op Amps, SC-70-5', 'kicadSymbolki_fp_filters': '*SC?70*'}])
    newPart['name'].append('Amplifier_Operational : MCP6401T-xLT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

