
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "MCP6401T-xOT"
    hexID = "SZKAMPLIFIEROPERATIONALMCP641TXOT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP6L91T-EOT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP6401T-xOT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/22229d.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': '1 MHz, 45 µA Op Amps, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Amplifier_Operational : MCP6401T-xOT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

