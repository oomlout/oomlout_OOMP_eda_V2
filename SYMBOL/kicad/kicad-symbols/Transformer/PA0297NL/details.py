
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "PA0297NL"
    hexID = "SZKTRPA297NL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PA2002NL', 'kicadSymbolReference': 'T', 'kicadSymbolValue': 'PA0297NL', 'kicadSymbolFootprint': 'Transformer_SMD:Pulse_PA2002NL-PA2008NL-PA2009NL', 'kicadSymbolDatasheet': 'https://productfinder.pulseeng.com/products/datasheets/SPM2007_61.pdf', 'kicadSymbolki_keywords': 'pulse', 'kicadSymbolki_description': 'SMT Gate Drive Transformer, 2:1:1', 'kicadSymbolki_fp_filters': 'Pulse*PA2002NL*PA2008NL*PA2009NL*'}])
    newPart['name'].append('Transformer : PA0297NL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

