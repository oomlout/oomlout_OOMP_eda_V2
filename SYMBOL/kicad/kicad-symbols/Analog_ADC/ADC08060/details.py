
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADC08060"
    hexID = "SZKANALOGADCADC86"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADC08060', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/adc08060.pdf', 'kicadSymbolki_keywords': 'ADC CAN VIDEO', 'kicadSymbolki_description': 'Fast ADC  (20 .. 60 Mhz), TSSOP-24'}])
    newPart['name'].append('Analog_ADC : ADC08060')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

