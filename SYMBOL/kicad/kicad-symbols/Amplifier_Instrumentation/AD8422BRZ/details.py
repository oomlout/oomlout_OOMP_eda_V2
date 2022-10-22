
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Instrumentation"
    oIndex = "AD8422BRZ"
    hexID = "SZKAMPLIFIERINSTRUMENTATIONAD8422BRZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD8422ARZ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8422BRZ', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8422.pdf', 'kicadSymbolki_keywords': 'ad8422 instumentation amplifier soic-8', 'kicadSymbolki_description': 'Low Power, Rail to Rail, Instumentation Amplifier, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC-8*'}])
    newPart['name'].append('AD8422BRZ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

