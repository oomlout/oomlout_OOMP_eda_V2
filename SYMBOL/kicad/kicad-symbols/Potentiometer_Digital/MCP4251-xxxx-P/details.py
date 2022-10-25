
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "MCP4251-xxxx-P"
    hexID = "SZKPOTENTIOMETERDIGITALMCP4251XXXXP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4251-xxxx-P', 'kicadSymbolFootprint': 'Package_DIP:DIP-14_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/22060b.pdf', 'kicadSymbolki_keywords': 'Digital Pot Potentiometer', 'kicadSymbolki_description': 'Dual 8 Bit Digital Pot, SPI, Volatile Memory, PDIP-14', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Potentiometer_Digital : MCP4251-xxxx-P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

