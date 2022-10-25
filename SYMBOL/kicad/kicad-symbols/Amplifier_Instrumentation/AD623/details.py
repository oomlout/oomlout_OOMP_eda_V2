
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Instrumentation"
    oIndex = "AD623"
    hexID = "SZKAMPLIFIERINSTRUMENTATIONAD623"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD620', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD623', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD623.pdf', 'kicadSymbolki_keywords': 'single instumentation amplifier', 'kicadSymbolki_description': 'Single Rail-to-Rail, Low Cost Instrumentation Amplifier, DIP-8/SOIC-8/MSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Amplifier_Instrumentation : AD623')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

