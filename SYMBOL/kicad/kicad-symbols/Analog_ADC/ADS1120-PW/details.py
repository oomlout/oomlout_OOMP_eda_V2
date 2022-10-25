
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS1120-PW"
    hexID = "SZKANALOGADCADS112PW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS1120-PW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads1120.pdf', 'kicadSymbolki_keywords': 'adc spi', 'kicadSymbolki_description': 'Low-power, quad-input, 16-bit analog to digital converter, integrated temperature sensor, SPI interface, TSSOP-16 package', 'kicadSymbolki_fp_filters': '*TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Analog_ADC : ADS1120-PW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

