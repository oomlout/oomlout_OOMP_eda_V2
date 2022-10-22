
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD7225LR"
    hexID = "SZKANALOGDACAD7225LR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD7225KR', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7225LR', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD7225.pdf', 'kicadSymbolki_keywords': '8bit DAC 4CH', 'kicadSymbolki_description': 'Quad 8bit DAC, Separate Reference Voltage, SO-24', 'kicadSymbolki_fp_filters': 'SO*'}])
    newPart['name'].append('AD7225LR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

