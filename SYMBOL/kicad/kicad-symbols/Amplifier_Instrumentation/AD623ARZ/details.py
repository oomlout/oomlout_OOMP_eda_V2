
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Instrumentation"
    oIndex = "AD623ARZ"
    hexID = "SZKAMPLIFIERINSTRUMENTATIONAD623ARZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD623AR', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD623ARZ', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD623.pdf', 'kicadSymbolki_keywords': 'ad623 instumentation amplifier soic-8', 'kicadSymbolki_description': 'Single Supply, Rail to Rail, Instumentation Amplifier, RoHS, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC-8*'}])
    newPart['name'].append('Amplifier_Instrumentation : AD623ARZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

