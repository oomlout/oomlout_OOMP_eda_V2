
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS1120-RVA"
    hexID = "SZKANALOGADCADS112RVA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS1120-RVA', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads1120.pdf', 'kicadSymbolki_keywords': 'adc spi', 'kicadSymbolki_description': 'Low-power, quad-input, 16-bit analog to digital converter, integrated temperature sensor, SPI interface, QFN-16 package', 'kicadSymbolki_fp_filters': 'QFN*3.5x3.5mm*P0.50mm*'}])
    newPart['name'].append('ADS1120-RVA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

