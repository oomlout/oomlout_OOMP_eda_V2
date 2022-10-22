
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Instrumentation"
    oIndex = "AD8421BRMZ"
    hexID = "SZKAMPLIFIERINSTRUMENTATIONAD8421BRMZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD8422ARMZ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8421BRMZ', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8421.pdf', 'kicadSymbolki_keywords': 'ad8421 instumentation amplifier msop-8', 'kicadSymbolki_description': 'Low Power, Instumentation Amplifier, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP-8*'}])
    newPart['name'].append('AD8421BRMZ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

