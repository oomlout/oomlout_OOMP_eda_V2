
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LM6171xxN"
    hexID = "SZKAMPLIFIEROPERATIONALLM6171XXN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP601-xP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM6171xxN', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm6171.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Single High Speed Low Power Low Distortion Voltage Feedback Amplifier, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Amplifier_Operational : LM6171xxN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

