
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS7029"
    hexID = "SZKANALOGADCADS729"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADS7040xDCU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS7029', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_2.3x2mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads7029-q1.pdf', 'kicadSymbolki_keywords': '8 bit SAR ADC', 'kicadSymbolki_description': 'Small-Size, Low-Power, 8-Bit, 2-MSPS, SAR ADC', 'kicadSymbolki_fp_filters': 'VSSOP*8*2.3x2mm*P0.5mm*'}])
    newPart['name'].append('ADS7029')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

