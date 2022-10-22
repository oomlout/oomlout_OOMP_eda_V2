
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "LTC2508IDKD-32"
    hexID = "SZKANALOGADCLTC258IDKD32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC2508CDKD-32', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC2508IDKD-32', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-24-1EP_4x7mm_P0.5mm_EP2.64x6.44mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/250832fc.pdf', 'kicadSymbolki_keywords': 'LT ADC 32bit', 'kicadSymbolki_description': '32-Bit Oversampling ADC with Configurable Digital Filter, -40°C to 85°C, DFN-24 package', 'kicadSymbolki_fp_filters': 'DFN*1EP*4x7mm*P0.5mm*'}])
    newPart['name'].append('LTC2508IDKD-32')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

