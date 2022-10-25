
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "PA2004NL"
    hexID = "SZKTRPA24NL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'T', 'kicadSymbolValue': 'PA2004NL', 'kicadSymbolFootprint': 'Transformer_SMD:Pulse_PA2004NL', 'kicadSymbolDatasheet': 'https://productfinder.pulseeng.com/products/datasheets/P663.pdf', 'kicadSymbolki_keywords': 'pulse', 'kicadSymbolki_description': 'SMT Gate Drive Transformer, 1:1:1', 'kicadSymbolki_fp_filters': 'Pulse*PA2004NL*'}])
    newPart['name'].append('Transformer : PA2004NL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

