
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS8681RUM"
    hexID = "SZKANALOGADCADS8681RUM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS8681RUM', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads8681.pdf', 'kicadSymbolki_keywords': 'ADC SPI analog digital', 'kicadSymbolki_description': '16-Bit, High-Speed, Single-Supply, SAR ADC Data Acquisition System with Programmable, Bipolar Input Ranges, 1MSPS, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.65mm*EP2.7x2.7mm*'}])
    newPart['name'].append('Analog_ADC : ADS8681RUM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

