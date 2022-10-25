
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "AD7819"
    hexID = "SZKANALOGADCAD7819"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7819', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD7819.pdf', 'kicadSymbolki_keywords': 'CAD', 'kicadSymbolki_description': 'Analog to Digital 8 bits converter, PDIP/SOIC/TSSOP-16'}])
    newPart['name'].append('Analog_ADC : AD7819')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

