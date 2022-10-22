
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "LTC1865-MS"
    hexID = "SZKANALOGADCLTC1865MS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC1865L-MS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC1865-MS', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/18645fb.pdf', 'kicadSymbolki_keywords': 'sigma-delta adc 2ch', 'kicadSymbolki_description': 'Dual channel 16-bit Analog to Digital Converter, 5V supply, 150ksps, SPI interface', 'kicadSymbolki_fp_filters': 'MSOP-10*'}])
    newPart['name'].append('LTC1865-MS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

