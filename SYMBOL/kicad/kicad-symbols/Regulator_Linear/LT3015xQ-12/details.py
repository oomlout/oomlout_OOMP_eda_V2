
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT3015xQ-12"
    hexID = "SZKREGULATORLINEARLT315XQ12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT3015xQ-2.5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3015xQ-12', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-5_TabPin3', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3015fb.pdf', 'kicadSymbolki_keywords': 'negative voltage regulator', 'kicadSymbolki_description': '-12V, 1.5A, Low Noise, Negative Linear Regulator with Precision Current Limit, TO-263-5', 'kicadSymbolki_fp_filters': 'TO*263*'}])
    newPart['name'].append('LT3015xQ-12')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

