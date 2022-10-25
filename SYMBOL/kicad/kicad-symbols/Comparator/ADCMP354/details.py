
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "ADCMP354"
    hexID = "SZKCOMPARATORADCMP354"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADCMP350', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADCMP354', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Analog_KS-4', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADCMP350_354_356.pdf', 'kicadSymbolki_keywords': 'cmp collector', 'kicadSymbolki_description': 'Single-input comparator, internal 0.6V reference, Active-High Open-Drain output, KS-4', 'kicadSymbolki_fp_filters': 'Analog*KS?4*'}])
    newPart['name'].append('Comparator : ADCMP354')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

