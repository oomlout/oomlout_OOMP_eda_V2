
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD7224LN"
    hexID = "SZKANALOGDACAD7224LN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD7224KN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7224LN', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD7224.pdf', 'kicadSymbolki_keywords': '8bit DAC Dual Single Supply', 'kicadSymbolki_description': '8bit DAC, Dual or Single Supply, DIP-18', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('AD7224LN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

