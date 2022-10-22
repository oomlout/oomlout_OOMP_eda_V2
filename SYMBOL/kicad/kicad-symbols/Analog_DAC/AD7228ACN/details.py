
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD7228ACN"
    hexID = "SZKANALOGDACAD7228ACN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD7228ABN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7228ACN', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD7228.pdf', 'kicadSymbolki_keywords': '8bit DAC 8CH', 'kicadSymbolki_description': '8bit DAC 8 Channel, Single Reference, DIP-24', 'kicadSymbolki_fp_filters': 'PDIP* DIP*'}])
    newPart['name'].append('AD7228ACN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

