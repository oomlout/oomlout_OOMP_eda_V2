
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS7043xDCU"
    hexID = "SZKANALOGADCADS743XDCU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADS7040xDCU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS7043xDCU', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_2.3x2mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads7043.pdf', 'kicadSymbolki_keywords': '12 bit SAR ADC', 'kicadSymbolki_description': 'Ultra-Low Power, Ultra-Small Size, 12-Bit, 1-MSPS, SAR ADC', 'kicadSymbolki_fp_filters': 'VSSOP*8*2.3x2mm*P0.5mm*'}])
    newPart['name'].append('Analog_ADC : ADS7043xDCU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

