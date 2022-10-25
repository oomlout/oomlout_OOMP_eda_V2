
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "AD7949BCP"
    hexID = "SZKANALOGADCAD7949BCP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7949BCP', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-20-1EP_4x4mm_P0.5mm_EP2.5x2.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD7949.pdf', 'kicadSymbolki_keywords': 'ADC, SPI', 'kicadSymbolki_description': '14-Bit, 8-Channel, 250 kSPS PulSAR ADC, LFSCP-20', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('Analog_ADC : AD7949BCP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

