
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS1018IDGS"
    hexID = "SZKANALOGADCADS118IDGS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS1018IDGS', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads1018.pdf', 'kicadSymbolki_keywords': '12 bit 4 channel SPI ADC', 'kicadSymbolki_description': ' Ultrasmall, Low-Power, SPI-Compatible, 12-Bit, Analog-to-Digital Converter With Internal Reference and Temperature Sensor, VSSOP-10', 'kicadSymbolki_fp_filters': 'TSSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Analog_ADC : ADS1018IDGS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

