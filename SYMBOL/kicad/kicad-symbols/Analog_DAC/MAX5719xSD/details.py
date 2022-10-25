
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MAX5719xSD"
    hexID = "SZKANALOGDACMAX5719XSD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX5717xSD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX5719xSD', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX5717-MAX5719.pdf', 'kicadSymbolki_keywords': 'DAC', 'kicadSymbolki_description': '20-bit Voltage Digital-to-Analog converter, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Analog_DAC : MAX5719xSD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

