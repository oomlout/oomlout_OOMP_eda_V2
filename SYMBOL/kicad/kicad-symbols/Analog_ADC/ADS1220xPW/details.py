
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS1220xPW"
    hexID = "SZKANALOGADCADS122XPW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADS1120-PW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS1220xPW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads1220.pdf', 'kicadSymbolki_keywords': 'adc spi', 'kicadSymbolki_description': 'Low-power, quad-input, 24-bit analog to digital converter, integrated temperature sensor, SPI interface, TSSOP-16 package', 'kicadSymbolki_fp_filters': '*TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('ADS1220xPW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

