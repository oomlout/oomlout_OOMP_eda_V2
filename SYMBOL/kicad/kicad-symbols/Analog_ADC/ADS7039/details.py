
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS7039"
    hexID = "SZKANALOGADCADS739"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADS7040xDCU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS7039', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_2.3x2mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads7039-q1.pdf', 'kicadSymbolki_keywords': '10 bit SAR ADC', 'kicadSymbolki_description': 'Small-Size, Low-Power, 10-Bit, 2-MSPS, SAR ADC', 'kicadSymbolki_fp_filters': 'VSSOP*8*2.3x2mm*P0.5mm*'}])
    newPart['name'].append('Analog_ADC : ADS7039')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

