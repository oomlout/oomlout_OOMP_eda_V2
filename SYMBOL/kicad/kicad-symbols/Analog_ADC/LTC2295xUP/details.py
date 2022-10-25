
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "LTC2295xUP"
    hexID = "SZKANALOGADCLTC2295XUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC2282xUP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC2295xUP', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP7.15x7.15mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/2295fa.pdf', 'kicadSymbolki_keywords': 'ADC', 'kicadSymbolki_description': 'Dual-Channel, 14-Bit Low Power ADC, 10Msps, QFN-64', 'kicadSymbolki_fp_filters': 'QFN*1EP*9x9mm*P0.5mm*'}])
    newPart['name'].append('Analog_ADC : LTC2295xUP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

