
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS1251"
    hexID = "SZKANALOGADCADS1251"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS1251', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads1251.pdf', 'kicadSymbolki_keywords': 'delta-sigma adc low-power', 'kicadSymbolki_description': 'Single channel 24-bit Analog to Digital Converter, 5V supply, differential input, 20kHz, 2-wire serial interface, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*'}])
    newPart['name'].append('Analog_ADC : ADS1251')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

