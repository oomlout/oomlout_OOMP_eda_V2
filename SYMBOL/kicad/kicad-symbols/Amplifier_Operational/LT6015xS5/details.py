
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LT6015xS5"
    hexID = "SZKAMPLIFIEROPERATIONALLT615XS5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP6L91T-EOT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT6015xS5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/601567ff.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': '3.2MHz, 0.8V/us, Low Power, Over-The-Top Precision Op Amp, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Amplifier_Operational : LT6015xS5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

