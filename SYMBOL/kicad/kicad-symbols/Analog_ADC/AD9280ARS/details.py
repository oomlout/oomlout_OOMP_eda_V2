
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "AD9280ARS"
    hexID = "SZKANALOGADCAD928ARS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD9280ARS', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD9280.pdf', 'kicadSymbolki_keywords': 'ADC CAN VIDEO', 'kicadSymbolki_description': 'Video ADC (32 Mhz), SSOP-28'}])
    newPart['name'].append('Analog_ADC : AD9280ARS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

