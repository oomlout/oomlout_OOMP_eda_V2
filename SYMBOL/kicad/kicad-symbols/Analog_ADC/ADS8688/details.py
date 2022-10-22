
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS8688"
    hexID = "SZKANALOGADCADS8688"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS8688', 'kicadSymbolFootprint': 'Package_SO:TSSOP-38_4.4x9.7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads8688.pdf', 'kicadSymbolki_keywords': 'adc analog digital spi bipolar input', 'kicadSymbolki_description': '16-Bit, 500-kSPS, 8-Channels, Single-Supply, SAR ADC with Bipolar Input Range, TSSOP-38', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x9.7mm*P0.5mm*'}])
    newPart['name'].append('ADS8688')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

