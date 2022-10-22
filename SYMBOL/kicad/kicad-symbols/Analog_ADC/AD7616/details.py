
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "AD7616"
    hexID = "SZKANALOGADCAD7616"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7616', 'kicadSymbolFootprint': 'Package_QFP:LQFP-80_14x14mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD7616.pdf', 'kicadSymbolki_keywords': '16bit DAS ADC 16channel 1MSPS', 'kicadSymbolki_description': '16-Channel DAS with 16-Bit, Bipolar Input, Dual Simultaneous Sampling ADC, 2x1MSPS ADC, Serial and parallel IO, LQFP-80', 'kicadSymbolki_fp_filters': 'LQFP*14x14mm*P0.65mm*'}])
    newPart['name'].append('AD7616')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

