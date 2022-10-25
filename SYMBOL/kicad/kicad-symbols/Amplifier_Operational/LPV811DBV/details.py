
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LPV811DBV"
    hexID = "SZKAMPLIFIEROPERATIONALLPV811DBV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP6L91T-EOT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LPV811DBV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lpv812.pdf', 'kicadSymbolki_keywords': 'single opamp low-power rail-to-rail', 'kicadSymbolki_description': 'Single operational amplifier, 8kHz GBW, 425 nA/channel quiescent, 100 fA input bias, 300 uV offset max, 1 uV/C, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Amplifier_Operational : LPV811DBV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

