
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "ADCMP356"
    hexID = "SZKCOMPARATORADCMP356"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADCMP356', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Analog_KS-4', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADCMP350_354_356.pdf', 'kicadSymbolki_keywords': 'cmp', 'kicadSymbolki_description': 'Single-input comparator, internal 0.6V reference, Active-High Push-Pull output, KS-4', 'kicadSymbolki_fp_filters': 'Analog*KS?4*'}])
    newPart['name'].append('ADCMP356')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

