
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MAX1275"
    hexID = "SZKANALOGADCMAX1275"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX1274', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX1275', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX1274-MAX1275.pdf', 'kicadSymbolki_keywords': '12bit ADC 1CH diff differential', 'kicadSymbolki_description': '1.8Msps, Single-Supply, Low-Power, True-Differential, 12-Bit ADCs, unipolar input', 'kicadSymbolki_fp_filters': '*QFN*4x4mm*P0.8mm*'}])
    newPart['name'].append('MAX1275')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

