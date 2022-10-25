
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "LTC1406IGN"
    hexID = "SZKANALOGADCLTC146IGN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC1406CGN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC1406IGN', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1406f.pdf', 'kicadSymbolki_keywords': 'Low Power ADC 8bit 20Msps', 'kicadSymbolki_description': 'ADC 8bit Low Power 20Msps, SSOP-24', 'kicadSymbolki_fp_filters': 'SSOP*'}])
    newPart['name'].append('Analog_ADC : LTC1406IGN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

