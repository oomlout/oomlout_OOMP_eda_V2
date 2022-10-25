
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD7228ACP"
    hexID = "SZKANALOGDACAD7228ACP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD7228ABP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7228ACP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD7228.pdf', 'kicadSymbolki_keywords': '8bit DAC 8CH', 'kicadSymbolki_description': '8bit DAC 8 Channel, Single Reference, PLCC-28', 'kicadSymbolki_fp_filters': 'PLCC*'}])
    newPart['name'].append('Analog_DAC : AD7228ACP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

