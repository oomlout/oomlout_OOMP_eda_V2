
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "PA0173NL"
    hexID = "SZKTRPA173NL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PA2005NL', 'kicadSymbolReference': 'T', 'kicadSymbolValue': 'PA0173NL', 'kicadSymbolFootprint': 'Transformer_SMD:Pulse_PA2005NL', 'kicadSymbolDatasheet': 'https://productfinder.pulseeng.com/products/datasheets/SPM2007_61.pdf', 'kicadSymbolki_keywords': 'pulse', 'kicadSymbolki_description': 'SMT Gate Drive Transformer, 1:1:1', 'kicadSymbolki_fp_filters': 'Pulse*PA2005NL*'}])
    newPart['name'].append('PA0173NL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

