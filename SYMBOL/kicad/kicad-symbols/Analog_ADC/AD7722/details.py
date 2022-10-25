
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "AD7722"
    hexID = "SZKANALOGADCAD7722"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7722', 'kicadSymbolFootprint': 'Package_QFP:MQFP-44_10x10mm_P0.8mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD7722.pdf', 'kicadSymbolki_keywords': 'adc 1ch 16bit parallel serial', 'kicadSymbolki_description': '16-Bit, 195 kSPS CMOS, Sigma-Delta ADC, MQFP-44', 'kicadSymbolki_fp_filters': 'MQFP*10x10mm*P0.8mm*'}])
    newPart['name'].append('Analog_ADC : AD7722')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

