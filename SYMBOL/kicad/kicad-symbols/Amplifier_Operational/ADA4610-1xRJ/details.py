
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "ADA4610-1xRJ"
    hexID = "SZKAMPLIFIEROPERATIONALADA4611XRJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP6L91T-EOT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADA4610-1xRJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4610-1_4610-2_4610-4.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Low Noise, Precision, Rail-to-Rail Output, JFET Single Op Amp, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Amplifier_Operational : ADA4610-1xRJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

