
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Instrumentation"
    oIndex = "AD623ARMZ"
    hexID = "SZKAMPLIFIERINSTRUMENTATIONAD623ARMZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD623ARM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD623ARMZ', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD623.pdf', 'kicadSymbolki_keywords': 'ad623 instumentation amplifier msop-8', 'kicadSymbolki_description': 'Single Supply, Rail to Rail, Instumentation Amplifier, RoHS, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP-8*'}])
    newPart['name'].append('Amplifier_Instrumentation : AD623ARMZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

