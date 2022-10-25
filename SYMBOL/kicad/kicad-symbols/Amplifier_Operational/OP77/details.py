
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OP77"
    hexID = "SZKAMPLIFIEROPERATIONALOP77"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'OP07', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OP77', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/OP77.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Next Generation OP07 Ultralow Offset Voltage Operational Amplifier, DIP-8/TO-99-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm* TO*99*'}])
    newPart['name'].append('Amplifier_Operational : OP77')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

