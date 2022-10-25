
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "AD7794"
    hexID = "SZKANALOGADCAD7794"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7794', 'kicadSymbolFootprint': 'Package_SO:TSSOP-24_4.4x7.8mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD7794_7795.pdf', 'kicadSymbolki_keywords': 'adc 6ch 24bit serial', 'kicadSymbolki_description': '24-Bit, 6-Channel Sigma-Delta ADC, TSSOP-28', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x7.8mm*P0.65mm*'}])
    newPart['name'].append('Analog_ADC : AD7794')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

