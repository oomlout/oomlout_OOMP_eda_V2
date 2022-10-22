
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "LTC1748"
    hexID = "SZKANALOGADCLTC1748"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC1742', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC1748', 'kicadSymbolFootprint': 'Package_SO:TSSOP-48_6.1x12.5mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1748fa.pdf', 'kicadSymbolki_keywords': 'ADC analog digital converter pipeline', 'kicadSymbolki_description': '14-Bit, 80Msps, Low Noise, ADC, TSSOP-48', 'kicadSymbolki_fp_filters': 'TSSOP*6.1x12.5mm*P0.5mm*'}])
    newPart['name'].append('LTC1748')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

