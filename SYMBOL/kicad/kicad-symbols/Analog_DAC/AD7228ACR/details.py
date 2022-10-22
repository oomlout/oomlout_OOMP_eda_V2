
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD7228ACR"
    hexID = "SZKANALOGDACAD7228ACR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD7228ABR', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7228ACR', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD7228.pdf', 'kicadSymbolki_keywords': '8bit DAC 8CH', 'kicadSymbolki_description': '8bit DAC 8 Channel, Single Reference, SOIC-24', 'kicadSymbolki_fp_filters': 'SO*'}])
    newPart['name'].append('AD7228ACR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

