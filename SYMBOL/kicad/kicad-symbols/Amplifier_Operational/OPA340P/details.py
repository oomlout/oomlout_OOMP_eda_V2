
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA340P"
    hexID = "SZKAMPLIFIEROPERATIONALOPA34P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP601-xP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA340P', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa340.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Single Single-Supply, Rail-to-Rail Operational Amplifier, MicroAmplifier Series, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Amplifier_Operational : OPA340P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

