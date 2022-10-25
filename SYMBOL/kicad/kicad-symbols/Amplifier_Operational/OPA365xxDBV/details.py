
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA365xxDBV"
    hexID = "SZKAMPLIFIEROPERATIONALOPA365XXDBV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP6L91T-EOT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA365xxDBV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/opa365.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': '50-MHz, Zero-Crossover, Low-Distortion, High CMRR, RRI/O, Single-Supply, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Amplifier_Operational : OPA365xxDBV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

