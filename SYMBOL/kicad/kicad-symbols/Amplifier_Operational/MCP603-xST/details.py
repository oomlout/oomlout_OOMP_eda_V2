
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "MCP603-xST"
    hexID = "SZKAMPLIFIEROPERATIONALMCP63XST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP603-xP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP603-xST', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21314g.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Single 2.7V to 6.0V Single Supply CMOS Op Amps, with Chip Select, TSSOP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm* TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Operational : MCP603-xST')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

