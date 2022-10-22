
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD7533KP"
    hexID = "SZKANALOGDACAD7533KP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD7533JP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7533KP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD7533.pdf', 'kicadSymbolki_keywords': '10bit DAC 1CH', 'kicadSymbolki_description': '10bit Multiplying DAC, 1 Channel, PLCC-20', 'kicadSymbolki_fp_filters': 'PLCC*'}])
    newPart['name'].append('AD7533KP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

