
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "AD8001AN"
    hexID = "SZKAMPLIFIEROPERATIONALAD81AN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP601-xP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8001AN', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ad8001.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Current Feedback Amplifier, 800 MHz, 50mW, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Amplifier_Operational : AD8001AN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

