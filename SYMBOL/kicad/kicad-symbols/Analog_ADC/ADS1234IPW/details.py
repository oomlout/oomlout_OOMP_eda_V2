
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS1234IPW"
    hexID = "SZKANALOGADCADS1234IPW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS1234IPW', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads1232.pdf', 'kicadSymbolki_keywords': 'ADC 24bit Sensors Quad Channel', 'kicadSymbolki_description': 'Dual Bridge 24bit ADC for Sensors, TSSOP-28', 'kicadSymbolki_fp_filters': 'TSSOP*'}])
    newPart['name'].append('Analog_ADC : ADS1234IPW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

