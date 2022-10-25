
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Instrumentation"
    oIndex = "AD8236ARMZ"
    hexID = "SZKAMPLIFIERINSTRUMENTATIONAD8236ARMZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD8422ARMZ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8236ARMZ', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8236.pdf', 'kicadSymbolki_keywords': 'ad8236 instumentation amplifier msop-8', 'kicadSymbolki_description': 'Micropower Instumentation Amplifier with Zero Crossover Distortion, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP-8*'}])
    newPart['name'].append('Amplifier_Instrumentation : AD8236ARMZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

