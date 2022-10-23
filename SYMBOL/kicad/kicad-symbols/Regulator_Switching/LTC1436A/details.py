
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTC1436A"
    hexID = "SZKREGULATORSWITCHINGLTC1436A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC1436A', 'kicadSymbolFootprint': 'Package_SO:SSOP-24_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/14367afb.pdf', 'kicadSymbolki_keywords': 'buck controller 36V', 'kicadSymbolki_description': 'High Efficiency Low Noise Synchronous Step-Down Switching Regulators, SSOP-24', 'kicadSymbolki_fp_filters': 'SSOP*3.9x8.7mm*P0.635mm*'}])
    newPart['name'].append('LTC1436A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

