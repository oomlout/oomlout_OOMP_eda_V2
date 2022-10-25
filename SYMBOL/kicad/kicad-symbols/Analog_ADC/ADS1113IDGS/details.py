
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS1113IDGS"
    hexID = "SZKANALOGADCADS1113IDGS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADS1013IDGS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS1113IDGS', 'kicadSymbolFootprint': 'Package_SO:TSSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads1113.pdf', 'kicadSymbolki_keywords': '16 bit single channel I2C ADC', 'kicadSymbolki_description': 'Ultra-Small, Low-Power, I2C-Compatible, 860-SPS, 16-Bit ADCs With Internal Reference and Oscillator, VSSOP-10', 'kicadSymbolki_fp_filters': 'TSSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Analog_ADC : ADS1113IDGS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

