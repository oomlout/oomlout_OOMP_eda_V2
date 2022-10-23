
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "PA0185NL1"
    hexID = "SZKTRPA185NL1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PA3493NL', 'kicadSymbolReference': 'T', 'kicadSymbolValue': 'PA0185NL1', 'kicadSymbolFootprint': 'Transformer_SMD:Pulse_PA3493NL', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'pulse', 'kicadSymbolki_description': 'SMT Gate Drive Transformer, 1.25:1', 'kicadSymbolki_fp_filters': 'Pulse*PA3493NL*'}])
    newPart['name'].append('PA0185NL1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

