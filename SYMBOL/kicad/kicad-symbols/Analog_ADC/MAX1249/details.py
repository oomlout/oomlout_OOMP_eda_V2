
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MAX1249"
    hexID = "SZKANALOGADCMAX1249"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX1248', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX1249', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX1248-MAX1249.pdf', 'kicadSymbolki_keywords': '10-Bit ADC Serial 4-Channel Maxim', 'kicadSymbolki_description': '4-Channel 10-Bit ADC with Serial Interface, +2.7V to +5.25V, Low-Power', 'kicadSymbolki_fp_filters': 'DIP* QSOP*'}])
    newPart['name'].append('MAX1249')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

