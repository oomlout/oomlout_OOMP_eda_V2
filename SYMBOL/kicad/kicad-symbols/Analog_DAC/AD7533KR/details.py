
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD7533KR"
    hexID = "SZKANALOGDACAD7533KR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7533KR', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD7533.pdf', 'kicadSymbolki_keywords': '10bit DAC 1CH', 'kicadSymbolki_description': '10bit Multiplying DAC, 1 Channel, SOIC-16', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('Analog_DAC : AD7533KR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

