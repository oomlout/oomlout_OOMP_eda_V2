
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "LTC1598IG"
    hexID = "SZKANALOGADCLTC1598IG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC1598CG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC1598IG', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/15948fb.pdf', 'kicadSymbolki_keywords': '12bit ADC 4 Channel', 'kicadSymbolki_description': 'Micropower 12-bit 8 Channel ADC, Serial IO, SSOP-24', 'kicadSymbolki_fp_filters': 'SSOP*'}])
    newPart['name'].append('LTC1598IG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

