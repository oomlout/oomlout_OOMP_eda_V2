
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADC1173"
    hexID = "SZKANALOGADCADC1173"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADC1173', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/adc1173.pdf', 'kicadSymbolki_keywords': 'ADC CAN VIDEO', 'kicadSymbolki_description': 'Fast ADC  (15 Mhz), TSSOP-24'}])
    newPart['name'].append('Analog_ADC : ADC1173')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

