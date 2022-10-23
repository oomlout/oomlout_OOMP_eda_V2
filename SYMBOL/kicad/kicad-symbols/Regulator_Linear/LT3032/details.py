
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT3032"
    hexID = "SZKREGULATORLINEARLT332"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3032', 'kicadSymbolFootprint': 'Package_DFN_QFN:Linear_DE14MA', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3032ff.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'LDO low noise', 'kicadSymbolki_description': '150mA, Dual Low Dropout Linear Regulator, Positive/Negative Low Noise, Adjustable Output, DFN-14', 'kicadSymbolki_fp_filters': 'Linear*DE14MA*'}])
    newPart['name'].append('LT3032')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

