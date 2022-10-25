
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "PE-68386NL"
    hexID = "SZKTRPE68386NL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PA2001NL', 'kicadSymbolReference': 'T', 'kicadSymbolValue': 'PE-68386NL', 'kicadSymbolFootprint': 'Transformer_SMD:Pulse_PA2001NL', 'kicadSymbolDatasheet': 'https://productfinder.pulseeng.com/products/datasheets/SPM2007_61.pdf', 'kicadSymbolki_keywords': 'pulse', 'kicadSymbolki_description': 'SMT Gate Drive Transformer, 1:1', 'kicadSymbolki_fp_filters': 'Pulse*PA2001NL*'}])
    newPart['name'].append('Transformer : PE-68386NL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

