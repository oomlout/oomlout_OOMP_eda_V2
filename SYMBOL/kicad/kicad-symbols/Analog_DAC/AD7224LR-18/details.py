
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD7224LR-18"
    hexID = "SZKANALOGDACAD7224LR18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD7224KR-18', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7224LR-18', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD7224.pdf', 'kicadSymbolki_keywords': '8bit DAC Dual Single Supply', 'kicadSymbolki_description': '8bit DAC, Dual or Single Supply, SOIC-18', 'kicadSymbolki_fp_filters': 'SO*'}])
    newPart['name'].append('Analog_DAC : AD7224LR-18')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

