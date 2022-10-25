
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Instrumentation"
    oIndex = "AD8421"
    hexID = "SZKAMPLIFIERINSTRUMENTATIONAD8421"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD8236', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8421', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8421.pdf', 'kicadSymbolki_keywords': 'single instumentation amplifier', 'kicadSymbolki_description': 'Single Low Power Instrumentation Amplifier, SOIC-8/MSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Instrumentation : AD8421')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

