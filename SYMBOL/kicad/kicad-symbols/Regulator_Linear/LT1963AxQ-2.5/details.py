
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1963AxQ-2.5"
    hexID = "SZKREGULATORLINEARLT1963AXQ25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1963AxQ-1.5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1963AxQ-2.5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-5_TabPin3', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1963aff.pdf', 'kicadSymbolki_keywords': 'voltage regulator linear ldo', 'kicadSymbolki_description': '2.5V, 1.5A, Low Noise, Fast Transient Response LDO Regulator, TO-263-5', 'kicadSymbolki_fp_filters': 'TO*263*'}])
    newPart['name'].append('LT1963AxQ-2.5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

