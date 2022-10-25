
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "MAX14778"
    hexID = "SZKANALOGSWITCHMAX14778"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX14778', 'kicadSymbolFootprint': 'Package_DFN_QFN:TQFN-20-1EP_5x5mm_P0.65mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX14778.pdf', 'kicadSymbolki_keywords': 'Analog Differential Multiplexer', 'kicadSymbolki_description': 'Dual +-25V Above- and Below-the-Rails 4:1 Analog Multiplexer, TQFN-20', 'kicadSymbolki_fp_filters': 'TQFN*1EP*5x5mm*P0.65mm*'}])
    newPart['name'].append('Analog_Switch : MAX14778')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

