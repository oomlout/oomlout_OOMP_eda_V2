
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "MAX7375AXR805"
    hexID = "SZKOCSMAX7375AXR85"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX7375AXR805', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-323_SC-70', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX7375.pdf', 'kicadSymbolki_keywords': 'Silicon Clock Oscillator 8MHz 8000kHz', 'kicadSymbolki_description': 'Silicon Clock Oscillator 8MHz, SC-70-3', 'kicadSymbolki_fp_filters': '*SC?70*'}])
    newPart['name'].append('Oscillator : MAX7375AXR805')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

